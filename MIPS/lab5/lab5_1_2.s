.data
Hex: .asciiz "0x"
Error: .asciiz "Invalid Input\n"
numHex: .space 12
numDec: .word 0
.text 
.globl main
 main:

li $v0, 5
syscall
move $t0, $v0

move $a1, $t0
jal printHex
j main

printHex:
	beq $a1, -1, Exit		# if $a1 = -1 then exit program
	blt $a1, -1, printError		# if $a1 < -1 then jump to error
	bgt $a1, 15, printError		# if $a1 > 15 then jump to error
	blt $a1, 10, printInt 		# if $a1 < 10 then print int
	j printChar			# else print char
	jr $ra				# jump and return to caller

printError:
	la $a0, Error
	li $v0, 4
	syscall
	jr $ra

printInt:
	la $a0, Hex
	li $v0, 4
	syscall

	move $a0, $a1
	li $v0, 1
	syscall
	jr $ra

printChar:
	la $a0, Hex
	li $v0, 4
	syscall

	addi $a1, $a1, 55
	move $a0, $a1
	li $v0, 11
	syscall
	jr $ra

Exit:
	li $v0,10
	syscall