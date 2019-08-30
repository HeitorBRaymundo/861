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
; Loading Control Buttons
; Store # $ 01 and # $ 00 is for position 4016 to begin sending control data

  ;JSR beep2
  LDX sounds
  CPX #1
  BEQ beep2
  LDX sounds
  CPX #100
  BEQ beep3

volta:
  INC sounds

  LDA #$01
  STA $4016
  LDA #00
  STA $4016
  CLC
  LDA $4016 ;A
  LDA $4016 ;B
  LDA $4016 ;Select
  LDA $4016 ;Start
  AND #1
  BNE Reset2
  LDA $4016 ; Cima
  AND #1
  BNE PacUp1
  LDA $4016 ; Baixo
  AND #1
  BNE PacDown1
  LDA $4016 ; Esquerda
  AND #1
  BNE PacLeft1
  LDA $4016 ; Direita
  AND #1
  BNE PacRight1
  JMP PacMan_movement

PacRight1:
  LDX pacmanLive
  CPX #1
  BNE Forever
  JMP PacRight

PacLeft1:
  LDX pacmanLive
  CPX #1
  BNE Forever
  JMP PacLeft

PacUp1:
  LDX pacmanLive
  CPX #1
  BNE Forever
  JMP PacUp

PacDown1:
  LDX pacmanLive
  CPX #1
  BNE Forever
  JMP PacDown

beep2: ; emite um beep em C# (#$C9)
  LDY #$A1
  STY $4002
  LDY #$00
  STY $4003

  JMP volta

beep3: ; emite um beep em C# (#$C9)
  LDY #$F1
  STY $4002
  LDY #$C5
  STY $400C

  LDA #0
  STA sounds

  JMP volta

PacMan_movement:
  LDA directionPacMan
  CMP #10
  BEQ PacUp1
  CMP #20
  BEQ PacDown1
  CMP #30
  BEQ PacLeft1
  CMP #40
  BEQ PacRight1

 .include "pacman_logic.asm"

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

GhostSpeedCounter:
  CLC
  LDX lowCounter
  INX
  STX lowCounter
  CPX #255
  BNE continueMovement
  CLC
  LDX #0
  STX lowCounter
  LDX highCounter
  INX
  STX highCounter
  CPX #3
  BNE continueMovement
  CLC
  LDX ghostSpeed
  INX
  STX ghostSpeed

continueMovement:
  JMP ghost1_movement

  .include "yellow_ghost.asm"
  .include "blue_ghost.asm"
  .include "orange_ghost.asm"
  .include "red_ghost.asm"

collide:
  ; game over hehe
  JSR beep
  LDA #0
  STA pacmanLive
  LDA #$00
  STA $4015
  JMP Forever

beep: ; emite um beep em C# (#$C9)
  lda #$C9
  sta $4002
  lda #$00
  sta $4003
  rts

;;;;;;;;;;;;;;;;;;;
; END: end of NMI ;
;;;;;;;;;;;;;;;;;;;
End:
  LDA #$02
  STA $4014
  LDA #$01
  STA $4016
  RTI				; return to Forever

;;;;;;;;;;;;;;;;;;
; Initialise PPU ;
;;;;;;;;;;;;;;;;;;
PPUInit:
    LDA #$00	; Charge $ 00 (0) in A
    STA $2003	; Place A, the most significant ($ 00) in $ 2003
    LDA #$02	; Charge $ 02 (2) in A
    STA $4014	; Place A, the most significant ($ 02) at $ 4014.
    LDA #%10001000; Charge the information of control of the PPU in A
    STA $2000	; Place A in $ 2000
    LDA #%00011110; Load mask information from the PPU into A
    STA $2001		; Place A in $ 2001
    RTS			; Return to the parent run

;;;;;;;;;;;;;;;;;;;;;;
; Cancel PPU  Scroll ;
;;;;;;;;;;;;;;;;;;;;;;
CancelScroll:
    LDA $2002	;Read the state of the PPU to reset its latch
    LDA #$00	; Charge $ 00 (0) in A
    STA $2000	; Place A in $ 2000 (Scroll X accurate)
    STA $2006	; Place A in $ 2006 (Scroll Y accurate)
    STA $2005	; Place A in $ 2005 (Tile Table)
    STA $2005	; Place A in $ 2005 (Scroll Y Rough)
    STA $2006	; Place A in $ 2006 (Scroll X Rude)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; code to wait images to load ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
VBlank:
  BIT $2002		; Checks 7h bit of $2002 address (PPU loaded)
  BPL VBlank		; Repet while image is not loaded
  RTS				; Return to parent

;;;;;;;;
; VIEW ;
;;;;;;;;
    .bank 1			; bank 1
    .org $E000		; Write starts at address $E000

Palette:
  ; [background color, color 1, color 2, color 3], [...], ...
  .db $FE,$20,$11,$15, $FE,$05,$15,$25, $FE,$08,$18,$28, $FE,$0A,$1A,$2A
  ; [color of opacity, color 1, color 2, color 3], [...], ...
  .db $FE,$28,$3E,$20, $FE,$12,$3E,$20, $FE,$27,$3E,$20, $FE,$16,$3E,$20


  Sprites:
    .db $80, $00, %00000000, $88  ; 200, 201, 202, 203
    .db $80, $01, %00000000, $80	; 204, 205, 206, 207
    .db $88, $02, %00000000, $88	; 208, 209, 20A, 20B
    .db $88, $03, %00000000, $80	; 20C, 20D, 20E, 20F

    .db $50, $04, %00000000, $58
    .db $50, $05, %00000000, $50
    .db $58, $06, %00000000, $58
    .db $58, $06, %01000000, $50

    .db $60, $04, %00000001, $68
    .db $60, $05, %00000001, $60
    .db $68, $06, %00000001, $68
    .db $68, $06, %01000001, $60

    .db $40, $04, %00000010, $48
    .db $40, $05, %00000010, $40
    .db $48, $06, %00000010, $48
    .db $48, $06, %01000010, $40

    .db $30, $04, %00000011, $38
    .db $30, $05, %00000011, $30
    .db $38, $06, %00000011, $38
    .db $38, $06, %01000011, $30
; [Position Y, Sprite's index , Attributes, Position X]

;;;;;;;;;;;;;;;;;
; Interruptions ;
;;;;;;;;;;;;;;;;;
  .org $FFFA		; Write starts at address $FFFA
  .dw NMI			; Starts the NMI sub-method when the NMI occurs
  .dw Reset		; Launches reset method when the processor starts
  .dw 0			; Do not launch anything when the BRK command occurs


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
  directionPacMan: .ds 1
  count1: .ds 1
  count2: .ds 1
  count3: .ds 1
  count4: .ds 1
  sounds: .ds 1
  highCounter: .ds 1
  lowCounter: .ds 1
  ghostSpeed: .ds 1
  pacmanLive: .ds 1
