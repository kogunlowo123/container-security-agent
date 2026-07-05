# Container Security Agent

[![CI](https://github.com/kogunlowo123/container-security-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/container-security-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Container security agent that scans container images for vulnerabilities, validates Dockerfiles against best practices, monitors runtime container behavior for anomalies, enforces image signing policies, and manages container supply chain security.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `scan_image` | Scan container image for CVEs and misconfigurations |
| `lint_dockerfile` | Validate Dockerfile against security best practices |
| `check_runtime_anomalies` | Detect anomalous container behavior (unexpected processes, network connections) |
| `verify_image_signature` | Verify container image signature and provenance |
| `generate_sbom` | Generate Software Bill of Materials for a container image |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/scan/image` | Scan container image |
| `POST` | `/api/v1/scan/dockerfile` | Lint Dockerfile |
| `GET` | `/api/v1/runtime/anomalies` | Check runtime anomalies |
| `POST` | `/api/v1/verify/signature` | Verify image signature |
| `POST` | `/api/v1/sbom/generate` | Generate SBOM |

## Features

- Image Scanning
- Dockerfile Linting
- Runtime Monitoring
- Image Signing
- Sbom Generation

## Integrations

- Trivy
- Snyk
- Falco
- Cosign
- Docker Registry

## Architecture

```
container-security-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── container_security_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Trivy + Snyk + Falco + Cosign**

---

Built as part of the Enterprise AI Agent Platform.
