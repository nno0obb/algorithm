#!/usr/bin/env bash

PROBLEMS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no)
      shift
      # --no 이후의 모든 인자를 문제 번호로 수집
      while [[ $# -gt 0 && ! "$1" =~ ^-- ]]; do
        PROBLEMS+=("$1")
        shift
      done
      ;;
    *)
      shift
      ;;
  esac
done

if [ ${#PROBLEMS[@]} -eq 0 ]; then
  echo "Usage: bash git.sh --no <problem_number1> <problem_number2> ..."
  exit 1
fi

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)

# 각 문제 번호에 대해 git add 실행
for PROBLEM in "${PROBLEMS[@]}"; do
  git add "$REPO_ROOT_DIR/problem_solving/boj/$PROBLEM"
done

# commit message 생성 (boj/번호1, boj/번호2, ... 형식)
COMMIT_MSG=""
for PROBLEM in "${PROBLEMS[@]}"; do
  if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="boj/$PROBLEM"
  else
    COMMIT_MSG="$COMMIT_MSG, boj/$PROBLEM"
  fi
done

git commit -m "$COMMIT_MSG"
git push
