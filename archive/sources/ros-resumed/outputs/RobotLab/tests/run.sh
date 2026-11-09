#!/usr/bin/env bash
set -euo pipefail
robot_repo="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$robot_repo"
python3 -m unittest discover -s tests -v
robot_test_binary="$(mktemp)"
trap 'rm -f -- "$robot_test_binary"' EXIT
g++ -std=c++17 -Wall -Wextra -Werror -Itests/firmware/stubs tests/firmware/test_runtime.cpp -o "$robot_test_binary"
"$robot_test_binary"
