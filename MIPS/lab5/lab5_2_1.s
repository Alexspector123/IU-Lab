.data
strSpace: .asciiz " "
num1: .word 1
num2: .word 1
num3: .word 0
.text
.globl main

main:

lw $s0, num1
move $a0, $s0
li $v0, 1
syscall
la $a0, strSpace
li $v0, 4
syscall
lw $s0, num2
move $a0, $s0
li $v0, 1
syscall
la $a0, strSpace
li $v0, 4
syscall

li $t0, 100
LOOP:
beq $t0, 2, exit
lw $s0, num1
lw $s1, num2
add $s2, $s0, $s1
move $a0, $s2
li $v0, 1
syscall
la $a0, strSpace
li $v0, 4
syscall
sw $s2, num1
sw $s0, num2
addi $t0, $t0, -1
j LOOP

exit:
li $v0, 10
syscall