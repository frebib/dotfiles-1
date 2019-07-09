#!/usr/bin/env bash

alias g="git"
{
  IFS=$'\n'

  for git_alias in $(git config --get-regexp alias); do
    final_alias=$(echo $git_alias | sed 's/alias.//g' | awk '{print $1;}')
    alias "g$final_alias"="git $final_alias"
  done
}
g-rm-branch() {
  current_branch=$(git rev-parse --abbrev-ref HEAD)
  if ! git branch | grep -q "master"; then
    echo "No master branch"
    return
  fi
  if [[ "$current_branch" == "master" ]]; then
    echo "Can't delete master branch"
    return
  fi

  echo "Deleting branch $current_branch"
  git checkout master \
    && git branch -D $current_branch

  if git branch --all | grep -q "origin/$current_branch"; then
    echo "Deleting remote branch $current_branch"
    git push origin --delete $current_branch
  fi
}
