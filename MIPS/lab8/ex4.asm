.data
strNameId: .asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
readX: .asciiz "Enter the value of x: "
printResult: .asciiz "The result is: "
n: .word 5
a: .float 4.3, -12.4, 6.8, -0.45, 3.6

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	la $a0, readX
	li $v0, 4
	syscall

	la $s0, a
	lw $t0, n
	li.s $f1, 0.0	#sum

	li $v0, 6	# Enter x
	syscall
	mov.s $f2, $f0	# f2 = f0 = x
	
LOOP:
	lwc1 $f3, 0($s0) 		# f3 = a[i]
	mul.s $f1, $f1, $f2		# sum = sum*x
	add.s $f1, $f1, $f3		# sum = sum + a[i] = sum*x + a[i]
	addi $s0, $s0, 4
	addi $t0, $t0, -1		# Increase counter
	beq $t0, $0, EXIT		# If t0 = 0, we stop the loop
	j LOOP

EXIT:
	la $a0, printResult
	li $v0, 4
	syscall

	mov.s $f12, $f1			# Print the result
	li $v0, 2
	syscall

	li $v0, 10
	syscall	