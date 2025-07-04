.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
input1: .asciiz "Enter the first integer: "
input2: .asciiz "Enter the second integer: "
output: .asciiz "The Multi is: "
strLine: .asciiz "\n"

.text
.globl main

main:
la $a0, strName
li $v0, 4
syscall

la $a0, strID
li $v0, 4
syscall

la $a0, input1
li $v0, 4
syscall
li $v0, 5
syscall
move $t0, $v0

la $a0, input2
li $v0, 4
syscall
li $v0, 5
syscall
move $t1, $v0

li $t2, 0
blt $t1, $0, LOOP1
LOOP:
beq $t1, $0, EXIT
add $t2, $t2, $t0
addi $t1, $t1, -1
j LOOP
LOOP1:
beq $t1, $0, EXIT
sub $t2, $t2, $t0
addi $t1, $t1, 1
j LOOP1
EXIT:
la $a0, output
li $v0, 4
syscall

move $a0, $t2
li $v0, 1
syscall

li $v0, 10
syscall
