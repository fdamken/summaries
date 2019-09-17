#!/bin/bash

set -o errexit
set -o nounset

pml="$1"
shift
echo "> spin $@ $(basename "$pml")" >"$pml.out"
spin $@ $pml >>"$pml.out"
