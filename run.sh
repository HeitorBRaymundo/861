#!/bin/bash

git clone https://github.com/camsaul/nesasm.git
cd nesasm/source
make
make install
cd ../../

cd $1
nesasm $1.asm
mednafen $1.nes
