.data
Hex: .asciiz "0x"
Error: .asciiz "Invalid Input\n"
quit: .asciiz "has quit\n"
numHex: .space 12
numDec: .word 0
.text 
.globl main

main:

li $v0, 5
syscall
move $t0, $v0

move $a3, $t0
jal printHex32
j main

printHex32:
	beq $a3, -1, Exit
	la $a0, Hex
	li $v0, 4
	syscall

	li $t1, 0

ifPrintHex32:
	blt $t1, 8, loopPrintHex32
	j main

loopPrintHex32:
	rol $a3, $a3, 4
	andi $t2, $a3, 0xF

	move $a1, $t2
	jal printHex

	addi $t1, $t1, 1
	j ifPrintHex32

Exit:
	la $a0, quit
	li $v0, 4
	syscall

	li $v0,10
	syscall

printHex:
	blt $a1, 0, printError
	bgt $a1, 15, printError
	blt $a1, 10, printInt

	j printChar
	jr $ra

printError:
	la $a0, Error
	li $v0, 4
	syscall
	jr $ra

printInt:
	move $a0, $a1
	li $v0, 1
	syscall
	jr $ra

printChar:
	addi $a1, $a1, 55
	move $a0, $a1
	li $v0, 11
	syscall
	jr $ra
	