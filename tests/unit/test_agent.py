"""Container Security Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_scan_image():
    """Test Scan container image for CVEs and misconfigurations."""
    tools = AgentTools()
    result = await tools.scan_image(image="test", severity_threshold="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_lint_dockerfile():
    """Test Validate Dockerfile against security best practices."""
    tools = AgentTools()
    result = await tools.lint_dockerfile(dockerfile_path="test", rules="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_runtime_anomalies():
    """Test Detect anomalous container behavior (unexpected processes, network connections)."""
    tools = AgentTools()
    result = await tools.check_runtime_anomalies(container_id="test", namespace="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_verify_image_signature():
    """Test Verify container image signature and provenance."""
    tools = AgentTools()
    result = await tools.verify_image_signature(image="test", keyref="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.container_security_agent_agent import ContainerSecurityAgentAgent
    agent = ContainerSecurityAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
