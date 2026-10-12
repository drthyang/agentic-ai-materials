"""The native Ollama critic transport: /api/chat with a bounded context."""

from __future__ import annotations

import json

import httpx
import pytest

from athanor.llm.ollama_native import OllamaNativeBackend, PromptTooLong


def _backend(handler, **kw):
    return OllamaNativeBackend(model="gemma4:26b", base_url="http://localhost:11434/v1",
                               transport=httpx.MockTransport(handler), **kw)


def test_posts_to_api_chat_with_num_ctx_not_the_openai_endpoint():
    seen = {}

    def handler(request):
        seen["path"] = request.url.path
        seen["body"] = json.loads(request.content)
        return httpx.Response(200, json={"message": {"role": "assistant", "content": "{}"},
                                         "done_reason": "stop"})

    b = _backend(handler, num_ctx=16384)
    out = b.chat("SYS", [{"role": "user", "content": "review"}], tools=[])
    assert seen["path"] == "/api/chat"  # the /v1 suffix of the config URL is dropped
    assert seen["body"]["options"] == {"num_ctx": 16384}
    assert seen["body"]["stream"] is False
    assert seen["body"]["messages"][0] == {"role": "system", "content": "SYS"}
    assert out.text == "{}" and b.last_latency_s is not None


def test_refuses_a_prompt_that_cannot_fit():
    b = _backend(lambda r: httpx.Response(200, json={"message": {"content": "x"}}), num_ctx=4096)
    with pytest.raises(PromptTooLong):
        b.chat("S", [{"role": "user", "content": "x" * 30_000}], tools=[])


def test_http_errors_raise_so_the_critic_counts_a_failure():
    b = _backend(lambda r: httpx.Response(500, json={"error": "runner died"}))
    with pytest.raises(httpx.HTTPStatusError):
        b.chat("S", [{"role": "user", "content": "x"}], tools=[])


def test_tools_are_not_supported():
    b = _backend(lambda r: httpx.Response(200, json={}))
    with pytest.raises(NotImplementedError):
        b.chat("S", [], tools=[object()])
