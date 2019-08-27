;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; code for setup and initial loads go here ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
.include "setup.asm"
.include "initialLoad.asm"

;;;;;;;;;;;;;;;;;;;;;;;;;
; Program infinite loop ;
;;;;;;;;;;;;;;;;;;;;;;;;;
Forever:
    JMP Forever		; Restart Forever before the next interrupt

;;;;;;;;;;;;;;;;;;;;;;;;;
; NMI - Code for images ;
;;;;;;;;;;;;;;;;;;;;;;;;;
NMI:

     UpdateSeed1:

        JSR RandomSeed1
        LDA #0
        STA count1
        JMP Ghost2

     UpdateSeed2:

        JSR RandomSeed2
        LDA #0
        STA count2
        JMP Ghost3

     UpdateSeed3:

        JSR RandomSeed3
        LDA #0
        STA count3
        JMP Ghost4

     UpdateSeed4:

        JSR RandomSeed4
        LDA #0
        STA count4
        JMP ghost1_movement

    Ghost1:
        LDA count1
        CMP #79
        BEQ  UpdateSeed1
        LDA #1
        ADC count1
        STA count1

    Ghost2:
        LDA count2
        CMP #127
        BEQ  UpdateSeed2
        LDA #1
        ADC count2
        STA count2

    Ghost3:
        LDA count3
        CMP #191
        BEQ  UpdateSeed3
        LDA #1
        ADC count3
        STA count3

    Ghost4:
        LDA count4
        CMP #251
        BEQ  UpdateSeed4
        LDA #1
        ADC count4
        STA count4


        JMP ghost1_movement

      .include "ghost1.asm"
      .include "ghost2.asm"
      .include "ghost3.asm"
      .include "ghost4.asm"

    collide:
        ; game over hehe
        JMP 0x000

;;;;;;;;;;;;;;;;;;;
; END: end of NMI ;
;;;;;;;;;;;;;;;;;;;
End:
    LDA #$02
    STA $4014
    LDA #$01
    STA $4016
    RTI				; return to Forever


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; code to wait images to load ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
VBlank:
    BIT $2002		; Checks 7h bit of $2002 address (PPU loaded)
    BPL VBlank		; Repet while image is not loaded
    RTS				; Return to parent

;;;;;;;;;;;;;;;;;
; Interruptions ;
;;;;;;;;;;;;;;;;;
    .org $FFFA		; Write starts at address $FFFA
    .dw NMI			; Starts the NMI sub-method when the NMI occurs
    .dw Reset		; Launches reset method when the processor starts
    .dw 0			; Do not launch anything when the BRK command occurs


Sprites:
.db $80, $00, %00000000, $88  ; 200, 201, 202, 203
.db $80, $01, %00000000, $80    ; 204, 205, 206, 207
.db $88, $02, %00000000, $88    ; 208, 209, 20A, 20B
.db $88, $03, %00000000, $80    ; 20C, 20D, 20E, 20F

;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; write Background sprites ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    .bank 2
    .org $0000

Background:
    .db %00000000
    .db %00111100
    .db %00100100
    .db %00100100
    .db %00111100
    .db %00100000
    .db %00100000
    .db %00000000
    ; least significant bits

    .db %00000000
    .db %00000000
    .db %00000000
    .db %00000000
    .db %00000000
    .db %00000000
    .db %00000000
    .db %00000000
    ; most significant bits

;;;;;;;;;;;;;;;;;;;;;
; SPRITES - GO HERE ;
;;;;;;;;;;;;;;;;;;;;;

    .org $1000		; write of the sprites
    .include "pacman_left_right_sprite.asm"
    .include "ghost_sprites.asm"
    .include "pacman_up_down_sprite.asm"

;;;;;;;;;;;;;
; VARIABLES ;
;;;;;;;;;;;;;

    .bank 0
    .zp
    .org $0000

    seed1: .ds 2
    seed2: .ds 2
    seed3: .ds 2
    seed4: .ds 2
    count1: .ds 1
    count2: .ds 1
    count3: .ds 1
    count4: .ds 1

    directionPacMan: .ds 1