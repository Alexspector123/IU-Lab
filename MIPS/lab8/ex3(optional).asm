.data
strNameId: .asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
enterTheRGB: .asciiz "Enter the RGB code: "
printResult: .asciiz "The result is: "
arr: .space 100
strSpace: .asciiz " "

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	la $a0, enterTheRGB
	li $v0, 4
	syscall

	la $a0, arr
	li $a1, 100
	li $v0, 8
	syscall

	la $a0, printResult
	li $v0, 4
	syscall

	la $s0, arr
	li $s1, 2	# for checking
	li $s2, 16
	li $t0, 6	# amount of elements
	li $t1, 0	# for sum
	move $t2, $t0

LOOP1:			
	lb $t4, 0($s0)
	bge $t4, 97, ELSE1
	bge $t4, 65, ELSE2
	bge $t4, 48, ELSE3

ELSE1:
	addi $t4, $t4, -87
	j LOOP2
ELSE2:
	addi $t4, $t4, -55
	j LOOP2
ELSE3:
	addi $t4, $t4, -48
	j LOOP2

LOOP2:
	div $t0, $s1
	mfhi $t3
	bne $t3, $0, LABEL1		# If it is not the second RGB, we will sum = sum + 16*value
	mul $t4, $t4, $s2
	add $t1, $t1, $t4
	addi $s0, $s0, 1
	addi $t0, $t0, -1		# Increase counter
	move $t2, $t0
	li $t3, 1
	beq $t0, $0, EXIT
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

	addi $s0, $s0, 1
	addi $t0, $t0, -1		# Increase counter
	li $t1, 0			# Reset the sum
	move $t2, $t0
	li $t3, 1
	beq $t0, $0, EXIT
	j LOOP1

EXIT:
	li $v0,	10
	syscall