#!/usr/bin/env bash

if ! [ -x /usr/bin/nproc ]; then
    echo "nproc is not installed. Please install it."
    exit 1
fi
CORES=$(nproc)
time mpiexec -np ${CORES} python ./MainParallel.py
