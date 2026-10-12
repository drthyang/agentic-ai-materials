"""The suite's network guard (tests/conftest.py) must actually trip."""

from __future__ import annotations

import httpx
import pytest


def test_real_http_request_is_refused():
    with pytest.raises(RuntimeError, match="hermetic test tried a real HTTP request"):
        httpx.Client().post("http://localhost:11434/api/chat", json={})


def test_mock_transports_still_work():
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(204)))
    assert client.get("http://localhost:11434/api/ps").status_code == 204


def test_the_native_critic_cannot_reach_ollama_from_a_test():
    from athanor.llm.ollama_native import OllamaNativeBackend

    with pytest.raises(RuntimeError, match="hermetic"):
        OllamaNativeBackend(model="gemma4:26b").chat("S", [{"role": "user", "content": "x"}], [])
