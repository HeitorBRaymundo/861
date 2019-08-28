LoadPalettes:

    LDA $2002
    LDA #$3F
    STA $2006
    LDA #$00
    STA $2006
    LDY #$00

LoadPalettesLoop:
    LDA Palette, y
    STA $2007
    INY
    CPY #$20
    BNE LoadPalettesLoop

LoadSprites:
    LDY #$00


LoadSpritesLoop:
    LDA Sprites, y
    STA $0200, y
    INY             
    CPY #80
    BNE LoadSpritesLoop
    JSR PPUInit
