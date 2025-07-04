.data
strNameId: .asciiz "\n"
printArray: .asciiz "The initial array: "
printLength: .asciiz "The length of the array is: "
strSpace: .asciiz " "
strLine: .asciiz "\n"
arr: .float 43.01, 34.06, 22141.09, 78.9, 64.98, 2126.1, 643.2, 451.4, 423.4, 45.5, 566.0, 0.0
a: .float 0.0

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	subu $sp, $sp, 4		# Allocate space on the stack
	sw $ra, 0($sp)			# Save $ra on the stack 

	la $t1, arr			# t1 = address of arr
	li $s0, 0			# Counter = 0

	l.s $f0, a			# get f0 = a = 0.0

	jal LEN				# Compute the length of the array

	la $a0, printArray
	li $v0, 4
	syscall

	la $a1, arr
	jal DISPLAY

	la $a0, strLine
	li $v0, 4
	syscall

	la $a0, printLength
	li $v0, 4
	syscall

	move $a0, $s0			# Print the length of the array
	li $v0, 1
	syscall

	li $v0, 10
	syscall

LEN:
	lwc1 $f2, 0($t1)		# Load the first float from the array

	c.eq.s $f2, $f0			# Check if the float is 0.0 (end of array)
	bc1t END_FUNC			# If true, go to END_FUNC

	addi $t1, $t1, 4		# Move to the next element
	
	subu $sp, $sp, 4		# Allocate space on the stack
	sw $ra, 0($sp)			# Save $ra on the stack

	jal LEN				# Call the recursive

	lw $ra, 0($sp)			# Load $ra on the stack
	addu $sp, $sp, 4		# Move to the next element

	addi $s0, $s0, 1		# Increase counter

	j $ra				# Return the $ra

DISPLAY:
	lwc1 $f2, 0($a1)

	c.eq.s $f2, $f0			# Check if the float is 0.0 (end of array)
	bc1t END_FUNC			# If true, go to END_FUNC

	mov.s $f12, $f2
	li $v0, 2
	syscall

	la $a0, strSpace
	li $v0, 4
	syscall

	addi $a1, $a1, 4
	j DISPLAY

END_FUNC:
	j $ra

	