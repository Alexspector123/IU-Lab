.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
strConmas: .asciiz ", "
strLine: .asciiz "\n"
input: .asciiz "Enter the N, M, X number: "
output: .asciiz "The sequence of number is: " 
numberN: .word 0
numberM: .word 0
numberX: .word 0

.text
.globl main

main:
la $a0, strName	
li $v0, 4		
syscall

la $a0, strID		
li $v0, 4		
syscall

la $a0, input		
li $v0, 4		
syscall

li $v0, 5
syscall
sw $v0, numberN

li $v0, 5
syscall
sw $v0, numberM

li $v0, 5
syscall
sw $v0, numberX

la $a0, output		
li $v0, 4		
syscall

lw $t0, numberN
lw $t1, numberM
li $t2, 1
lw $s0, numberX

move $a0, $t0
li $v0, 1
syscall

la $a0, strConmas
li $v0, 4
syscall
addi $s0, $s0, -1

loop:
mul $t2, $t2, $t1
mul $t3, $t2, $t0
move $a0, $t3
li $v0, 1
syscall
la $a0, strConmas
li $v0, 4
syscall
addi $s0, $s0, -1 
bne $s0, $0, loop

EXIT:
li $v0, 10
syscall