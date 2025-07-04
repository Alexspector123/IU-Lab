.data
arr: .word 3, 2, 1, 8, 6, 9, 0, 4, 2, 5, 14, 15, 12, 13, 11, 17, 19, 18, 16, 10
n: .word 20
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ID: ITCSIU22056\n" 
strSpace: .asciiz " "
strLine: .asciiz "\n"
text1: .asciiz "Initial array: "
text2: .asciiz "Reverse array: "
.text
.globl main
main:
la $a0, strName
li $v0, 4
syscall	

la $a0, strID
li $v0, 4
syscall

la $a0, text1
li $v0, 4
syscall

    lw      $s0, n
    la      $t0, arr
loop:
lw      $t1, 0($t0)

move    $a0, $t1
li      $v0, 1      
syscall

la $a0, strSpace
li $v0, 4
syscall

addi    $t0, $t0, 4
    #increment counter
addi    $s0, $s0, -1
bne $s0, $0, loop

la $a0, strLine
li $v0, 4
syscall
la $a0, text2
li $v0, 4
syscall
lw      $s0, n
la      $t0, arr
reverse_loop:
lw      $t1, 76($t0)

move    $a0, $t1
li      $v0, 1      
syscall

la $a0, strSpace
li $v0, 4
syscall

addi    $t0, $t0, -4
addi    $s0, $s0, -1
bne $s0, $0, reverse_loop


exit:
li      $v0, 10
syscall