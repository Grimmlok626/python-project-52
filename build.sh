#!/usr/bin/env bash
set -e

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# зависимости ставим через uv
make install
make collectstatic
make migrate