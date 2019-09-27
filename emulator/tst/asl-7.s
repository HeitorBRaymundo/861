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
  ADC #20
  ASL A
  STA $21
  ASL A
  LDX #2
  STA $300, X
  ASL A
  ASL A
  ASL A
  ASL A
  STA $20
  ASL $20
  ASL $20
  ASL $20
  LDA $20
  ADC #1
  STA $300
  ASL $300
  LDA $300
  ADC #1
  LDX #1
  ASL $20, X
  LDA $21
  ADC #1
  INX
  ASL $300, X
  LDA $302
  ADC #1
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
