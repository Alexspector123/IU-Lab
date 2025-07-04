.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
msg: .asciiz "The value of f is: "
n: .word 5
x: .word 6, 12, -21, 4, 9

.text
.globl main

main:
la $a0, name
li $v0, 4
syscall

la $t1, x
lw $s0, 0($t1)
lw $s1, 4($t1)
lw $s2, 8($t1)
lw $s3, 12($t1)
lw $s4, 16($t1)

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