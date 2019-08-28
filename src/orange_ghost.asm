RandomSeed3:
    LDA seed3
    ASL A
    ASL A
    CLC
    ADC seed3
    CLC
    ADC #59
    STA seed3
    RTS

ghost3_movement:  ;Orange
    LDA seed3
    AND #03
    CMP #00
    BEQ Ghost3Up
    CMP #01
    BEQ Ghost3Down
    CMP #02
    BEQ Ghost3Left
    CMP #03
    BEQ Ghost3Left

Ghost3Up:   ;Orange
    DEC $230
    DEC $234
    DEC $238
    DEC $23C
    JSR CheckCollisionF3P
    JMP ghost4_movement

Ghost3Down:    ;Orange
    INC $230
    INC $234
    INC $238
    INC $23C
    JSR CheckCollisionF3P
    JMP ghost4_movement

Ghost3Left: ;Orange
    DEC $233
    DEC $237
    DEC $23B
    DEC $23F
    JSR CheckCollisionF3P
    JMP ghost4_movement

Ghost3Right: ;Orange
    INC $233
    INC $237
    INC $23B
    INC $23F
    JSR CheckCollisionF3P
    JMP ghost4_movement


CheckCollisionF3P:
    LDA $207
    CMP $233
    BCS justReturn3
    LDA $203
    CMP $237
    BCC justReturn3
    LDA $200
    CMP $238
    BCS justReturn3
    LDA $208
    CMP $230
    BCC justReturn3
    JMP collide

justReturn3:
    RTS

