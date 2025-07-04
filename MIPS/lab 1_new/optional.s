.data
strName: .asciiz "Phan Tran Thanh Huy"
strID: .asciiz "ITCSIU22056"
str0: .asciiz "Input your size: "
str1: .asciiz "Input your array: "
str2: .asciiz "Choose your mode: "
strSpace: .asciiz " "
strLine: .asciiz "\n"
strError: .asciiz "Error"
range: .asciiz "Out of range"
mode1Str1: .asciiz "Enter the index: "
mode1Str2: .asciiz "Your number: "
mode2Str1: .asciiz "Enter your 1st index: "
mode2Str2: .asciiz "Enter your 2nd index: "
mode2Str3: .asciiz "Your array: "

arr: .space 15 
n: .word 0

.text
.globl main

main:
la $a0, strName
li $v0, 4
syscall

la $a0, strID
li $v0, 4
syscall

la $a0, str0
li $v0, 4
syscall

li $v0, 5
syscall
sw $v0, n

lw $s0, n
la $t0, arr

loop1:
li $v0, 5
syscall
sw $v0, 0($t0)
addi $t0, $t0, 4
addi $s0, $s0, -1
bne $s0, $0, loop1

lw $s0, n
la $t0, arr

li $t3, 1
li $t4, 2

la $a0, str2
li $v0, 4
syscall

li $v0, 5
syscall

move $t2, $v0

beq $t3, $t2, mode1
beq $t4, $t2, mode2
la $a0, strError
li $v0, 4
syscall
j exit

mode1:
la $a0, mode1Str1
li $v0, 4
syscall
li $v0, 5
syscall
move $t2, $v0
lw $4, n
blt $t2, $0, Else
bgt $t2, $t4, Else
la $a0, mode1Str2
li $v0, 4
syscall
la $t0, arr
li $t3, 4
mul $t3, $t3, $t2
add $t0, $t0, $t3
lw $a0, 0($t0)
li $v0, 1
syscall
j exit

mode2:
la $a0, mode2Str1
li $v0, 4
syscall
li $v0, 5
syscall
move $t2, $v0
la $a0, mode2Str2
li $v0, 4
syscall
li $v0, 5
syscall
move $t3, $v0
lw $t4, size
blt $t2, $0, Else
bgt $t3, $t4, Else
la $t0, arr
li $t4, -1
li $t5, 4
la $a0, mode2Str3
li $v0, 4
syscall
mul $t5, $t5, $t2
add $t0, $t0, $t2
add $t4, $t4, $t2
loopMode2:
lw $t1, 0($t0)
move $a0, $t1
li $v0, 1
syscall
la $a0, strSpace
li $v0, 4
syscall
addi $t0, $t0, 4
addi $t4, $t4, 1
bne $t4, $t3, loopMode2
j exit

Else:
la $a0, range
li $v0, 4
syscall
j exit

exit:
li $v0, 10
syscall
