"""Test configuration for Container Security Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "container-security-agent", "category": "DevOps & Platform Engineering"}
