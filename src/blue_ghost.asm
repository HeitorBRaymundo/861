RandomSeed2:
    LDA seed2
    ASL A
    ASL A
    ASL A
    CLC
    ADC seed2
    CLC
    ADC #29
    STA seed2
    RTS

ghost2_movement:  ;Blue
    LDA seed2
    AND #03
    CMP #00
    BEQ Ghost2Down
    CMP #01
    BEQ Ghost2Down
    CMP #02
    BEQ Ghost2Left
    CMP #03
    BEQ Ghost2Right

Ghost2Up:   ;Blue
    DEC $220
    DEC $224
    DEC $228
    DEC $22C
    JSR CheckCollisionF2P
    JMP ghost3_movement

Ghost2Down:    ;Blue
    INC $220
    INC $224
    INC $228
    INC $22C
    JSR CheckCollisionF2P
    JMP ghost3_movement

Ghost2Left: ;Blue
    DEC $223
    DEC $227
    DEC $22B
    DEC $22F
    JSR CheckCollisionF2P
    JMP ghost3_movement

Ghost2Right: ;Blue
    INC $223
    INC $227
    INC $22B
    INC $22F
    JSR CheckCollisionF2P
    JMP ghost3_movement

CheckCollisionF2P:
    LDA $207
    CMP $223
    BCS justReturn2
    LDA $203
    CMP $227
    BCC justReturn2
    LDA $200
    CMP $228
    BCS justReturn2
    LDA $208
    CMP $220
    BCC justReturn2
    JMP collide

justReturn2:
    RTS

