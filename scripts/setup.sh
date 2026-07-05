#!/bin/bash
set -euo pipefail
echo "Setting up Container Security Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
