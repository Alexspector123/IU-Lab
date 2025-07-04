.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
input: .asciiz "Enter an integer: "
output: .asciiz "The Sum is: "
strLine: .asciiz "\n"
sum: .word 0

.text
.globl main

main:
la $a0, strName
li $v0, 4
syscall

la $a0, strID
li $v0, 4
syscall

li $t0, 1
li $s0, 2

LOOP:
la $a0, input
li $v0, 4
syscall

li $v0, 5
syscall
move $t0, $v0
beq $t0, $0, EXIT

lw $s1, sum

div $t0, $s0
mfhi $t2

beq $t2, $0, CASE
mul $t3, $t0, $t0
mul $t3, $t3, $t0
add $s1, $s1, $t3
sw $s1, sum
j LOOP

CASE:
mul $t3, $t0, $t0
add $s1, $s1, $t3
sw $s1, sum
j LOOP

EXIT:
la $a0, output
li $v0, 4
syscall

lw $a0, sum
li $v0, 1
syscall

li $v0, 10
syscall
