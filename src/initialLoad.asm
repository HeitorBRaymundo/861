;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; load the palettes into the memory ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
LoadPalettes:

    LDA $2002 ; Read PPU status to reset your lock
    LDA #$3F   ; Loads the most significant byte value (1111111) at A
    STA $2006; A at $ 2006
    LDA #$00 ; Loads the least significant byte value (00000000) into A
    STA $2006 ; A at $ 2006
    LDY #$00  ; Charges $ 00 (0) on Y

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; loop to load the palettes into the memory ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

LoadPalettesLoop: ; Y was initialized to 0 previously
    LDA Palette, y  ; Load first byte of Palette (+ Y) into A
    STA $2007       ; Store A at $ 2007
    INY             ; Increment Y
    CPY #$20        ; Compare Y with $ 20 (32)
    BNE LoadPalettesLoop   ; Loop while Y <32

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; load the sprites into the memory ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
LoadSprites:
    LDY #$00        ; Place $00 (0) at Y

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; loop to load the sprites into the memory ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
LoadSpritesLoop:
    LDA Sprites, y  ; Loads the first byte of Sprites (+ Y) in A
    STA $0200, y    ; Put A at $ 02YY
    INY
    CPY #80        ; Compare Y with #80 (dec)
    BNE LoadSpritesLoop     ; Loop while Y < 80
    JSR PPUInit     ; Call PPU startup
    jmp Forever

Reset2:
   jmp Reset