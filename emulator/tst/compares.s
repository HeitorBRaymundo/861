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
   ldy #0
   lda #0

   ora $400, Y ; ORA abs, Y

   ora ($20, X) ; ORA X, ind

   ora $44 ; ORA zpg

   ora #$44 ; ORA #

   ora $4400 ; ORA abs

   ora ($44), Y ; ORA ind, Y

   ora $44, X ; ORA zpg, X

   ora $4400, X ; ORA abs, X

   lda #10
   sta $400, Y ; AND abs, Y
   and $400, Y
   lda #0
   sta $400, Y

   and ($44, X) ; AND X, ind

   and $44 ; AND zpg

   and #$44 ; AND #

   and $4400 ; AND abs

   and ($44), Y ; AND ind, Y

   and $44, X ; AND zpg, X

   and $4400, X ; AND abs, X

   eor ($44), Y ; EOR ind, Y

   eor $44 ; EOR zpg

   eor #$44 ; EOR #

   eor $4400 ; EOR abs

   eor ($44, X) ; EOR ind, X

   eor $44, X ; EOR zpg, X

   eor $4400, Y ; EOR abs, Y

   eor $4400, X ; EOR abs, X

   cpy #$44 ; CPY #

   cpy $44 ; CPY zpg

   cpy $4400 ; CPY abs

   cmp ($44, X) ; CMP X, ind

   cmp $44 ; CMP zpg

   cmp #$44 ; CMP #

   cmp $4400 ; CMP abs

   cmp ($44), Y ; CMP ind, Y

   cmp $44, X ; CMP zpg, X

   cmp $4400, Y ; CMP abs, Y

   cmp $4400, X ; CMP abs, X

   cpx #$44 ; CPX #

   cpx $44 ; CPX zpg

   cpx $4400 ; CPX abs

   asl $130 ; Abort execution
   iny

 NMI:
    ;NOTE: NMI code goes here
 IRQ:
    ;NOTE: IRQ code goes here

 ;----------------------------------------------------------------
 ; interrupt vectors
 ;----------------------------------------------------------------

    .org $fffa

    .dw NMI
    .dw Reset
    .dw IRQ
