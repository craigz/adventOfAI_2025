#!/bin/bash
# Madame Zelda's Fortune Teller Wrapper
# Usage: ./fortune.sh [personality] [count]
# Can also be invoked via: goose run -t "run the fortune teller"

cd "$(dirname "$0")"

PERSONALITY=${1:-all}
COUNT=${2:-1}

python fortune_teller.py "$PERSONALITY" "$COUNT"
