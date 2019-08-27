SpriteGhostUpRight:
    .db %00000000
    .db %11000000
    .db %11110000
    .db %11111000
    .db %11111100
    .db %11011100
    .db %11111100
    .db %11111100
    ; less significant bit

    .db %11000000
    .db %00110000
    .db %00001000
    .db %01100100
    .db %01100010
    .db %01100010
    .db %00000010
    .db %00000011
    ; most significant bits

SpriteGhostUpLeft:
    .db %00000000
    .db %00000011
    .db %00001111
    .db %00011111
    .db %00111111
    .db %00111101
    .db %00111111
    .db %01111111
    ; less significant bit

    .db %00000011
    .db %00001100
    .db %00010000
    .db %00100110
    .db %01000110
    .db %01000110
    .db %01000000
    .db %10000000
    ; most significant bits

SpriteGhostBottom:
    .db %11111110
    .db %11111110
    .db %11111110
    .db %11111110
    .db %11011100
    .db %10001000
    .db %00000000
    .db %00000000
    ; less significant bit

    .db %00000001
    .db %00000001
    .db %00000001
    .db %00000001
    .db %00100011
    .db %01010101
    .db %10001001
    .db %00000000
    ; most significant bits
