#!/bin/bash
set -e

wget -q -O openrefine-3.1.tar.gz https://github.com/OpenRefine/OpenRefine/releases/download/3.1/openrefine-linux-3.1.tar.gz
mkdir -p $HOME/.openrefine
tar xzf openrefine-3.1.tar.gz -C $HOME/.openrefine
rm openrefine-3.1.tar.gz

mkdir -p $HOME/openrefine

mkdir -p $HOME/.jupyter/

#Although located in binder/,
# this bash file runs in $HOME rather than $HOME/binder
mv jupyter_notebook_config.py $HOME/.jupyter/