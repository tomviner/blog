#!/bin/bash

set -ex

git submodule update --init --recursive --depth=1

make html
