#!/usr/bin/env bash
command -v apt-get 1>/dev/null || return 0
alias aget="sudo apt-get"
alias ai="aget install"
alias as="apt-cache search"
