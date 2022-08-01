#!/bin/bash
cd "$(dirname "$0")/demo"
__GL_SYNC_TO_VBLANK=1 python2 demo.py $*
