#!/usr/bin/env bash
set -uo pipefail

ROOT="/home/ubuntu/Edge-AI"
cd "$ROOT" || exit 1

failures=0
check() {
  local name="$1"
  shift
  if "$@" >/tmp/agent-smoke.out 2>/tmp/agent-smoke.err; then
    printf '[OK] %s\n' "$name"
  else
    printf '[FAIL] %s\n' "$name"
    sed -n '1,8p' /tmp/agent-smoke.err
    failures=$((failures + 1))
  fi
}

check 'workspace path' test "$PWD" = "$ROOT"
check 'ripgrep literal Chinese search' rg -n -F -e '神经网络' -e 'neural' course-index.md courses/neural-networks/course-config.md
check 'ripgrep limited English regex search' rg -n 'neural|neural-network' course-index.md courses/neural-networks/course-config.md
check 'numpy import' python3 -c 'import numpy as np; print(np.__version__)'
check 'XOR lesson script' python3 courses/neural-networks/Code/XOR.py
check 'git status available' git status --short --branch
check 'git remote reachable' git ls-remote --exit-code origin refs/heads/main
check 'Claude local settings use Linux paths' jq -e '.permissions.additionalDirectories | all(.[]; startswith("/"))' .claude/settings.local.json

if command -v gh >/dev/null 2>&1; then
  printf '[INFO] gh exists, but agents should still prefer git unless gh auth is required.\n'
else
  printf '[INFO] gh is not installed; agents should use git for GitHub backup tasks.\n'
fi

if [ "$failures" -eq 0 ]; then
  printf 'Agent environment smoke test passed.\n'
else
  printf 'Agent environment smoke test failed: %s issue(s).\n' "$failures"
fi
exit "$failures"
