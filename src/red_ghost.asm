RandomSeed4:
    LDA seed4
    ASL A
    ASL A
    CLC
    ADC seed4
    CLC
    ADC #02
    STA seed4
    RTS

ghost4_movement:  ;Red
    LDA seed4
    AND #03
    CMP #00
    BEQ Ghost4Up
    CMP #01
    BEQ Ghost4Down
    CMP #02
    BEQ Ghost4Right
    CMP #03
    BEQ Ghost4Right

Ghost4Up:   ;Red
    DEC $240
    DEC $244
    DEC $248
    DEC $24C
    JSR CheckCollisionF4P
    JMP End

Ghost4Down:    ;Red
    INC $240
    INC $244
    INC $248
    INC $24C
    JSR CheckCollisionF4P
    JMP End

Ghost4Left: ;Red
    DEC $243
    DEC $247
    DEC $24B
    DEC $24F
    JSR CheckCollisionF4P
    JMP End

Ghost4Right: ;Red
    INC $243
    INC $247
    INC $24B
    INC $24F
    JSR CheckCollisionF4P
    JMP End

CheckCollisionF4P:
    LDA $207
    CMP $243
    BCS justReturn4
    LDA $203
    CMP $247
    BCC justReturn4
    LDA $200
    CMP $248
    BCS justReturn4
    LDA $208
    CMP $240
    BCC justReturn4
    JMP collide

justReturn4:
    RTS

