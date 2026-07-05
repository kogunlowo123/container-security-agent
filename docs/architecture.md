# Container Security Agent Architecture

Container security agent that scans container images for vulnerabilities, validates Dockerfiles against best practices, monitors runtime container behavior for anomalies, enforces image signing policies, and manages container supply chain security.

## Domain Tools

- **scan_image**: Scan container image for CVEs and misconfigurations
- **lint_dockerfile**: Validate Dockerfile against security best practices
- **check_runtime_anomalies**: Detect anomalous container behavior (unexpected processes, network connections)
- **verify_image_signature**: Verify container image signature and provenance
- **generate_sbom**: Generate Software Bill of Materials for a container image