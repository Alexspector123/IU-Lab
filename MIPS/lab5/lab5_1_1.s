.data
Hex: .asciiz "0x"
numDec: .word 0
.text 
.globl main
 main:

	li $v0, 5
	syscall
	move $t0, $v0

	la $a0, Hex
	li $v0, 4
	syscall

	li $t1, 9

	ble $t0, $t1, ELSE
	addi $t0, $t0, 55
	move $a0, $t0
	li $v0, 11
	syscall
	j EXIT

ELSE:
	move $a0, $t0
	li $v0, 1
	syscall
	j EXIT

EXIT:
	li $v0,10
	syscall
