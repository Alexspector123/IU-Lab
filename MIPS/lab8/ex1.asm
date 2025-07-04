.data
strNameId: .asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
readX: .asciiz "Enter the value of x: "
readY: .asciiz "Enter the value of y: "
printResult: .asciiz "5.4xy - 12.3y + 18.23x - 8.23 = "
a: .float 5.4
bb: .float 12.3
c: .float 18.23
d: .float 8.23

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	la $a0, readX
	li $v0, 4
	syscall

	li $v0, 6
	syscall
	
	mov.s $f2, $f0

	la $a0, readY
	li $v0, 4
	syscall

	li $v0, 6
	syscall
	
# f2 = x, f0 = y

	l.s $f4, a
	mul.s $f4, $f4, $f2	# 5.4x
	mul.s $f4, $f4, $f0	# 5.4xy
	l.s $f6, bb
	mul.s $f6, $f6, $f0	# 12.3y
	sub.s $f4, $f4, $f6	# 5.4xy - 12.3y
	l.s $f6, c
	mul.s $f6, $f6, $f2	# 18.23x
	add.s $f4, $f4, $f6	#  5.4xy - 12.3y + 18.23x
	l.s $f6, d
	sub.s $f4, $f4, $f6	#  5.4xy - 12.3y + 18.23x - 8.23

	la $a0, printResult
	li $v0, 4
	syscall

	mov.s $f12, $f4
	li $v0, 2
	syscall

	li $v0, 10
	syscall