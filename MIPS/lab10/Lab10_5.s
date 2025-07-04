.data
	Name:	.asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
	e: .word 6
	prompt:	.asciiz "Enter a,b,c,d,u and v:\n"
	printResult: .asciiz "The result is: "
.text
.globl main
main:
	la $a0, Name
	li $v0, 4
	syscall
	
	la $a0, prompt
	li $v0, 4
	syscall
	
	li $v0, 6
	syscall
	mov.s $f5, $f0		#f5 = a
	
	li $v0, 6
	syscall
	mov.s $f4, $f0		#f4 = b
	
	li $v0, 6
	syscall
	mov.s $f3, $f0		#f3 = c
	
	li $v0, 6
	syscall
	mov.s $f2, $f0		#f2 = d
	
	li $v0, 6
	syscall
	mov.s $f1, $f0		#f1 = u
	
	li $v0, 6
	syscall				#f0 = v
	
	mov.s $f12, $f1
	jal calculateIntegral
	mov.s $f6, $f12		#F(u)
		
	mov.s $f12, $f0
	jal calculateIntegral
	mov.s $f7, $f12		#F(v)
	
	sub.s $f6, $f6, $f7		#F(u) - F(v)
	
	lw $s0, e
	mtc1 $s0, $f8
	cvt.s.w $f8, $f8
	
	mul.s $f8, $f8, $f8		#e^2
	
	div.s $f6, $f6, $f8		#(F(u) - F(v))/e^2
	
	la $a0, printResult
	li $v0, 4
	syscall

	mov.s $f12, $f6
	li $v0, 2
	syscall
	
	li $v0, 10
	syscall
	
	
calculateIntegral:
	subu $sp, $sp, 8
	s.s $f6, 0($sp)
	s.s $f7, 4($sp)

	li.s $f6, 5.0
	mul.s $f7, $f12, $f12	#x*x
	mul.s $f7, $f7, $f7		#x^4
	mul.s $f7, $f7, $f12	#x^5
	mul.s $f7, $f7, $f5		#ax^5
	div.s $f7, $f7, $f6		#ax^5 / 5
	
	
	li.s $f6, 4.0
	mul.s $f8, $f12, $f12
	mul.s $f8, $f8, $f8		#x^4
	mul.s $f8, $f8, $f4		#bx^4
	div.s $f8, $f8, $f6		#bx^4 / 4
	
	li.s $f6, 3.0
	mul.s $f9, $f12, $f12
	mul.s $f9, $f9, $f12	#x^3
	mul.s $f9, $f9, $f3
	div.s $f9, $f9, $f6		#cx^3 / 3
	
	mul.s $f10, $f12, $f2	#dx
	
	add.s $f10, $f10, $f9
	add.s $f10, $f10, $f8
	add.s $f10, $f10, $f7
	mov.s $f12, $f10
	
	l.s $f6, 0($sp)
	l.s $f7, 4($sp)
	addi $sp, $sp, 8
	jr $ra