RandomSeed1:
    LDA seed1
    ASL A
    ASL A
    CLC
    ADC seed1
    CLC
    ADC #03
    STA seed1
    RTS

ghost1_movement:  ;Yellow
    LDA seed1
    AND #03
    CMP #00
    BEQ Ghost1Down
    CMP #01
    BEQ Ghost1Down
    CMP #02
    BEQ Ghost1Left
    CMP #13
    BEQ Ghost1Right


Ghost1Up:   ;Yellow
    DEC $210
    DEC $214
    DEC $218
    DEC $21C
    JSR CheckCollisionF1P
    JMP ghost2_movement

Ghost1Down:    ;Yellow
    INC $210
    INC $214
    INC $218
    INC $21C
    JSR CheckCollisionF1P
    JMP ghost2_movement

Ghost1Left: ;Yellow
    DEC $213
    DEC $217
    DEC $21B
    DEC $21F
    JSR CheckCollisionF1P
    JMP ghost2_movement

Ghost1Right: ;Yellow
    INC $213
    INC $217
    INC $21B
    INC $21F
    JSR CheckCollisionF1P
    JMP ghost2_movement

CheckCollisionF1P:
    LDA $207
    CMP $213
    BCS justReturn1
    LDA $203
    CMP $217
    BCC justReturn1
    LDA $200
    CMP $218
    BCS justReturn1
    LDA $208
    CMP $210
    BCC justReturn1
    JMP collide

justReturn1:
    RTS

