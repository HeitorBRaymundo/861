; Author: tokumaru
; http://forums.nesdev.com/viewtopic.php?%20p=58138#58138
;----------------------------------------------------------------
; constants
;----------------------------------------------------------------
PRG_COUNT = 1 ;1 = 16KB, 2 = 32KB
MIRRORING = %0001 ;%0000 = horizontal, %0001 = vertical, %1000 = four-screen

;----------------------------------------------------------------
; variables
;----------------------------------------------------------------

   .enum $0000

   ;NOTE: declare variables using the DSB and DSW directives, like this:

   ;MyVariable0 .dsb 1
   ;MyVariable1 .dsb 3

   .ende

   ;NOTE: you can also split the variable declarations into individual pages, like this:

   ;.enum $0100
   ;.ende

   ;.enum $0200
   ;.ende

;----------------------------------------------------------------
; iNES header
;----------------------------------------------------------------

   .db "NES", $1a ;identification of the iNES header
   .db PRG_COUNT ;number of 16KB PRG-ROM pages
   .db $01 ;number of 8KB CHR-ROM pages
   .db $00|MIRRORING ;mapper 0 and mirroring
   .dsb 9, $00 ;clear the remaining bytes

;----------------------------------------------------------------
; program bank(s)
;----------------------------------------------------------------

   .base $10000-(PRG_COUNT*$4000)

Reset:

NMI:
    LDA #$01
    STA $4016
    LDA #00
    STA $4016
    CLC
    LDA $4016 ;A
    LDA $4016 ;B
    LDA $4016 ;Select
    LDA $4016 ;Start
    ;AND #1
    ;BNE Reset2
    LDA $4016 ; Cima
    ;AND #1
    ;BNE PacUp1
    LDA $4016 ; Baixo
    ;AND #1
    ;BNE PacDown1
    LDA $4016 ; Esquerda
    ;AND #1
    ;BNE PacLeft1
    LDA $4016 ; Direita
    ;AND #1
    ;BNE PacRight1
    JMP NMI
    brk


IRQ:

.org $fffa

.dw NMI
.dw Reset
.dw IRQ
