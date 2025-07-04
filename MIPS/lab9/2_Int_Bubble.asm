.data
strNameId: .asciiz "\n"
printInitialArray: .asciiz "The initial array: "
printSortedArray: .asciiz "The sorted array: "
strLine: .asciiz "\n"
strSpace: .asciiz " "
arr: .word 43, 6543, 34, 54, 4232, 64, 526, 643, 6435, 423, 4236, 566, 41, 0
sortedArr: .space 1024

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	la $a1, arr			# a1 = address of arr
	li $s0, 0			# s0 = 0
	jal LEN				# Compute the length of the array

	la $a0, printInitialArray
	li $v0, 4
	syscall

	la $a1, arr			# a1 = address of arr
	jal DISPLAY			# Display the array

	la $a0, strLine
	li $v0, 4
	syscall

	la $a1, arr			# a1 = address of arr			
	li $t0, 0			# t0 = 0
	jal SORT			# Sort the array

	la $a0, printSortedArray
	li $v0, 4
	syscall
	
	la $a1, arr			# a1 = address of arr		
	jal DISPLAY			# Display the array

	la $a0, strLine
	li $v0, 4
	syscall

	li $v0, 10
	syscall

LEN:
	lw $t2, 0($a1)			# Load t2 = a[i]
	beq $t2, $0, END_FUNC		# Check if t2 = a[i] = 0, stop the LEN 

	addi $a1, $a1, 4		# Move the next element
	addi $s0, $s0, 1		# Increase counter
	j LEN

SORT:
	j OUTER_LOOP			# Jump to OUTER_LOOP

OUTER_LOOP:
	bge $t0, $s0, END_FUNC		# Check if t0 = s0 = length of the array, stop the OUTER_LOOP
	li $t9, 0			# t9 = 0
	li $t1, 0			# t1 = 0
	j INNER_LOOP			# Jump to INNER_LOOP

INNER_LOOP:			
	sub $t2, $s0, $t0		# t2 = s0 - t0 
	addi $t2, $t2, -1		# t2 = t2 - 1 = the current index

	bge $t1, $t2, CHECK_LOOP	# Check if t1 >= t2, go to CHECK_LOOP
	li $t3, 4			# t3 = 4
	mul $t3, $t3, $t1		# t3 = t3*t1
	add $t3, $a1, $t3		# t3 = a1 + t3 = a[i]

	addi $t1, $t1, 1		# Increase the counter of INNER_LOOP

	lw $t4, 0($t3)
	lw $t5, 4($t3)

	ble $t4, $t5, INNER_LOOP	# if t4 <= t5, skip the swap
	# Swap Variable
	sw $t5, 0($t3)
	sw $t4, 4($t3)
	li $t9, 1			# t9 = 1
	j INNER_LOOP

CHECK_LOOP:
	beq $t9, $0, END_FUNC		# Check if t9 = 0, stop the sort
	addi $t0, $t0, 1		# Increase the counter of OUTER_LOOP
	j OUTER_LOOP

DISPLAY:
	lw $t2, 0($a1)			# Load t2 = a[i]
	beq $t2, $0, END_FUNC		# Check if t2 = 0, go to END_FUNC

	move $a0, $t2			# Print the a[i]
	li $v0, 1
	syscall

	la $a0, strSpace
	li $v0, 4
	syscall

	addi $a1, $a1, 4		# Move to the next element
	j DISPLAY

END_FUNC:
	j $ra