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