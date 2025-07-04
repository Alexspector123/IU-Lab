.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
msg: .asciiz "The value of f is: "
ff: .word 0
gg: .word 12
hh: .word -21
ii: .word 4
jj: .word 0

.text
.globl main

main:
la $a0, strName
li $v0, 4
syscall

la $a0, strID
li $v0, 4
syscall

lw $s1, gg
lw $s2, hh
lw $s3, ii

li $v0, 5
syscall
move $s0, $v0

li $v0, 5
syscall
move $s4, $v0

bne $s3, $s4, L1
add $s0, $s1, $s2
b L2

L1: sub $s0, $s0, $s3
L2: sub $s0, $s0, $s4

la $a0, msg
li $v0, 4
syscall

move $a0, $s0
li $v0, 1
syscall

li $v0, 10
syscall