.data
strNameId: .asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
readN: .asciiz "Enter the nth term: "
printResult: .asciiz "The result of Harmoni Series is: "

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	la $a0, readN
	li $v0, 4
	syscall

	li $v0, 5
	syscall

	move $t0, $v0
	
	li.d $f0, 0.0
	li.d $f2, 1.0
LOOP:
	mtc1 $t0, $f4
	cvt.d.w $f4, $f4
	div.d $f6, $f2, $f4
	add.d $f0, $f0, $f6
	addi $t0, $t0, -1
	bne $t0, $0, LOOP
EXIT:
	la $a0, printResult
	li $v0, 4
	syscall

	mov.d $f12, $f0
	li $v0, 3
	syscall

	li $v0, 10
	syscall