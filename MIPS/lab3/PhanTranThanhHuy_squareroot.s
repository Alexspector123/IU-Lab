.data
n: .word 0
input: .asciiz "Enter the number: "
output: .asciiz "The result is: "
strLine: .asciiz "\n"
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"

.text
.globl main

main:
la $a0, strName
li $v0, 4
syscall

la $a0, strID
li $v0, 4
syscall

LOOP1:
la $a0, input
li $v0, 4
syscall

li $v0, 7
syscall

mov.d $f2, $f0
cvt.w.d $f2, $f2
mfc1 $t0, $f2
blt $t0, $0, LOOP1

div $t1, $t0, 2  #t1 = n/2
mov.d $f2, $f0
li $t2, 2

mtc1 $t2, $f4
cvt.d.w $f4, $f4


LOOP:
beq $t1, $0, EXIT

div.d $f6, $f0, $f2

add.d $f6, $f6, $f2
div.d $f6, $f6, $f4

mov.d $f2, $f6

addi $t1, $t1, -1
j LOOP

EXIT:
la $a0, output
li $v0, 4
syscall

mov.d $f12, $f2
li $v0, 3
syscall

li $v0, 10
syscall
