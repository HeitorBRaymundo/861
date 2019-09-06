#!/bin/bash

git clone https://github.com/camsaul/nesasm.git
cd nesasm/source
make
make install
cd ../../

cd src/
nesasm pacman_main
mednafen pacman_main.nes
