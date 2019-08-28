    .inesprg 1
    .ineschr 1
    .inesmap 0
    .inesmir 1

    .bank 0
    .org $8000
    .code

Reset:
    SEI
    CLD
    LDX #%01000000
    STX $4017
    LDX #$FF
    TXS
    INX
    STX $2000
    STX $2001
    STX $4010
    JSR VBlank

Clear:
    LDX #40
    STX directionPacMan
    LDX #0
    STX count1
    LDX #0
    STX count2
    LDX #0
    STX count3
    LDX #0
    STX count4
    LDX #0
    STX seed1
    LDX #0
    STX seed2
    LDX #0
    STX seed3
    LDX #0
    STX seed4

    JSR VBlank
    JSR PPUInit
