PacUp:
    LDA #%10000000
    STA $202
    STA $206
    STA $20A
    STA $20E
    LDA #$09
    STA $201
    LDA #$0A
    STA $205
    LDA #$07
    STA $209
    LDA #$08
    STA $20D
    DEC $200
    DEC $204
    DEC $208
    DEC $20C
    LDA #10
    STA directionPacMan
    JMP EndPacMan


PacDown:
    LDA #%00000000
    STA $202
    STA $206
    STA $20A
    STA $20E
    LDA #$07
    STA $201
    LDA #$08
    STA $205
    LDA #$09
    STA $209
    LDA #$0A
    STA $20D
    INC $200
    INC $204
    INC $208
    INC $20C
    LDA #20
    STA directionPacMan
    JMP EndPacMan

PacLeft:
    LDA #%01000000
    STA $202
    STA $206
    STA $20A
    STA $20E
    LDA #$00
    STA $205
    LDA #$01
    STA $201
    LDA #$02
    STA $20D
    LDA #$03
    STA $209
    DEC $203
    DEC $207
    DEC $20B
    DEC $20F
    LDA #30
    STA directionPacMan
    JMP EndPacMan

PacRight:
    LDA #%00000000
    STA $202
    STA $206
    STA $20A
    STA $20E
    LDA #$00
    STA $201
    LDA #$01
    STA $205
    LDA #$02
    STA $209
    LDA #$03
    STA $20D
    INC $203
    INC $207
    INC $20B
    INC $20F
    LDA #40
    STA directionPacMan
    JMP EndPacMan