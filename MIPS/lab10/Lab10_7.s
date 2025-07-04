.data
	Name:	.asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
	array:	.float 1.0, 55.0, 6.0, 55.0, 2.0, 15.0, 20.0, 22.0, 1.0, 0.0
	array_prompt: .asciiz "The define array: 1.0, 55.0, 6.0, 55.0, 2.0, 15.0, 20.0, 22.0, 1.0, 0.0 \nMax: "
.text
.globl main
main:
	la $a0, Name
	li $v0, 4
	syscall
	
	la $a0, array_prompt
	li $v0, 4
	syscall

	la $a0, array
	li $a1, 10		#size = 10
	jal max
	li $v0, 2
	syscall
	
	li $v0, 10
	syscall
	
max:
	addi $t2, $a1, -1
	l.s $f12, 0($a0)
	beq $t2, $zero, return		#if k == 1
	
	subu $sp, $sp, 12
	sw $a0, 0($sp)	#save array
	sw $a1, 4($sp)	#save size
	sw $ra, 8($sp)	
	
	addi $a0, $a0, 4
	addi $a1, $a1, -1
	jal max
	
	lw $a0, 0($sp)	#load array
	lw $a1, 4($sp)	#load size
	lw $ra, 8($sp)	
	addi $sp, $sp, 12
	
	l.s $f0, 0($a0)		#load v[0]
	
	c.lt.s $f0, $f12	#if v[0] < temp --> return
	bc1t return
	
	mov.s $f12, $f0
	jr $ra
return:	
	jr $ra