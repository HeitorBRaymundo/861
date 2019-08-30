;;;;;;;;;;;;;;;;
; Declarations ;
;;;;;;;;;;;;;;;;
    .inesprg 1      ; 16 KB database of PRG code
    .ineschr 1      ; 1x 8KB CHR database
    .inesmap 0      ; No bank swaps
    .inesmir 1      ; Background mirror


;;;;;;;;;;;;;;;;;;
; Init ;
;;;;;;;;;;;;;;;;;;
    .bank 0         ; Bank 0
    .org $8000      ; Writing starts at $ 8000
    .code           ; Program Start

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Init of the PPU and APU ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
Reset:
    SEI             ; Disable IRQ
    CLD             ; Disable decimal mode
    LDX #%01000000  ; Load% 01000000 (64) into register X
    STX $4017       ; X at $ 4017 to disable APU metronamo
    LDX #$FF        ; Load $ FF (255) into register X
    TXS             ; Initializes the stack with 255
    INX             ; Increments X
    STX $2000       ; X at $ 2000 to disable NMI
    STX $2001       ; X at $ 2000 to disable display
    STX $4010       ; X at $ 2000 to disable DMC

    lda #%00000111  ; enable channels Sq1, Sq2 and Tri
    sta $4015
    lda #%11001111  ; Configure channel Sq1 w/ duty 10 and volume F using internal counter
    sta $4000

    JSR VBlank

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Init of the variables ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
Clear:
    LDX #40
    STX directionPacMan
    LDX #0
    STX count1
    LDX #0
    STX count2
    LDX #0
    STX count3
    LDX #0
    STX count4
    LDX #0
    STX seed1
    LDX #0
    STX seed2
    LDX #0
    STX seed3
    LDX #0
    STX seed4
    LDX #1
    STX ghostSpeed
    LDX #0
    STX lowCounter
    LDX #0
    STX highCounter
    LDX #0
    STX sounds
    LDX #1
    STX pacmanLive
    LDX #32
    STX beepFrequency
 
    JSR VBlank      ; Wait for the image to fully load before continuing
    JSR PPUInit     ; Initialize the PPU before loading the rest.
