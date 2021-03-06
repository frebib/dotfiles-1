#!/usr/bin/env bash

pacman-install python

# Check the system python version
python_version=$($SYSTEM_PYTHON -V)
if [[ $python_version != *"3.6"* && $python_version != *"3.7"* ]]; then
  echo "Bad python version: $python_version"
  return 0
fi

# If the python directory already exists, we're done
if [ -d $DF_PYTHON_DIR ]; then
  return 0
fi

# Set up the virtual env
$SYSTEM_PYTHON -m venv $DF_PYTHON_DIR
$DF_PIP install --requirement python-requirements.txt
