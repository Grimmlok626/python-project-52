#!/usr/bin/env bash
set -e

# Установка uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Установка hatch
pip install --user hatch
export PATH=$HOME/.local/bin:$PATH

# Проверка наличия hatch
which hatch

# Теперь запускаем установку зависимостей и действия make
make install
make collectstatic
make migrate