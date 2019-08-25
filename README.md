## About
This repository will be used for code control and storage, of a project aimed at developing a NES-based simulator. More information about the project can be found on the following [link](http://www.ic.unicamp.br/~rodolfo/Cursos/mc861/2019s2/).

## References
Here there are some links that could help on the project development:
1. [Emulator tutorial](http://skilldrick.github.io/easy6502/)
2. [Assembly language wiki](http://wiki.nesdev.com/w/index.php/CPU)
3. [Game development tutorial](http://nintendoage.com/forum/messageview.cfm?catid=22&threadid=7155)
4. [Javascript emulator](https://github.com/takahirox/nes-js)

## How to run

Assuming that you have Mednafen emulator, run the script

```bash
$ ./run.sh <game_name>
```

Where `<game_name>` is the name of the **folder** where your game is in this dir and the `.asm` file in it. This allow you to have multiple games in the directory and run them separately with the same script.

## Example game

To get started, we used the "background" example from [Nerdy nights Week 3 tutorial](http://nintendoage.com/forum/messageview.cfm?catid=22&threadid=4440).

You can run the example with:

```bash
$ ./run.sh background
```

## Contributors
Heitor Banhete\
Henrique Fuschini\
Igor Mateus Omote\
Luiz Eduardo Cartolano
