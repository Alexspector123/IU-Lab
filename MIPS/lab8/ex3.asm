.data
strNameId: .asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
printResult: .asciiz "The result is: "
color: .word 0x00FF0000
strSpace: .asciiz " "

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	la $a0, printResult
	li $v0, 4
	syscall

	lw $s0, color
	li $s1, 2	# for checking
	li $s2, 16
	li $t0, 5	# amount of elements
	li $t1, 0	# for sum
	move $t2, $t0
	li $t3, 1

LOOP1:					# Use to calculate the 16^nth
	beq $t2, $0, LOOP2
	mul $t3, $t3, $s2
	addi $t2, $t2, -1
	j LOOP1

LOOP2:					# Find the value of the hex in the nth position
	div $s0, $t3
	mflo $t4
	mul $t3, $t3, $t4
	sub $s0, $s0, $t3
	div $t0, $s1
	mfhi $t5
	beq $t5, $0, LABEL1		# If it is not the second RGB, we will sum = sum + 16*value
	mul $t4, $t4, $s2
	add $t1, $t1, $t4
	addi $t0, $t0, -1		# Increase counter
	move $t2, $t0
	li $t3, 1
	blt $t0, $0, EXIT
	j LOOP1

LABEL1:
	add $t1, $t1, $t4		# If it is the second RGB, we will sum = sum + 1*value
	mtc1 $t1, $f0			# Convert int to float
	cvt.s.w $f0, $f0
	li.s $f2, 255.0
	div.s $f4, $f0, $f2		# sum(float)/255

	mov.s $f12, $f4			# Print the result
	li $v0, 2
	syscall
	
	la $a0, strSpace
	li $v0, 4
	syscall

	addi $t0, $t0, -1		# Increase counter
	li $t1, 0			# Reset the sum
	move $t2, $t0
	li $t3, 1
	blt $t0, $0, EXIT
	j LOOP1

EXIT:
	li $v0,	10
	syscall