"""Test-suite guards.

The suite is hermetic: no test may reach a real server. On 2026-10-12 a test
that built an Ollama critic directly sent real requests to localhost:11434
and loaded a 26B model on a shared machine. Every real httpx transport is
therefore blocked here (httpx.MockTransport still works), except in tests
marked ``network``, which are opt-in anyway.
"""

from __future__ import annotations

import httpx
import pytest


@pytest.fixture(autouse=True)
def _no_real_http(request, monkeypatch):
    if request.node.get_closest_marker("network"):
        return

    def refuse(self, req):
        raise RuntimeError(f"hermetic test tried a real HTTP request: {req.method} {req.url}")

    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", refuse)
