.data
	Name:	.asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
	array:	.word 1, 2, 3, 3, 3, 1, 7 ,8, 9, 10
	tempArr:	.space 40
	duplicateArr:.space 50
	prompt:	.asciiz "Duplicated value: "
	Duplicated: .asciiz ", repeated "
	comma1:	.asciiz " times; "
	prompt1: .asciiz "\nUnique values: "
	comma :	.asciiz ", "
	givenArray:	.asciiz "Given array: 1, 2, 3, 3, 3, 1, 7 ,8, 9, 10\n"
.text
.globl main
main:
	la $a0, Name
	li $v0, 4
	syscall
	la $a0, givenArray
	li $v0, 4
	syscall

	la $s0, array
	la $s1, tempArr
	la $s4, duplicateArr
	
	li $s2, 10	#lastIndex = 9
	li $s3, -1	#i = 0
	
	la $a0, prompt
	li $v0, 4
	syscall
	
Loop:
	addi $s3, $s3, 1	#i++
	beq $s3, $s2, endLoop
	
	sll $t3, $s3, 2    
    add $t4, $s0, $t3   
    lw $t1, 0($t4)      # t1 = array[i]
	
	li $t5, 0	#j = 0
	li $t0, 0	#count = 0
	loop2:	
	beq $t5, $s2, endSubloop
	sll $t3, $t5, 2    
    add $t4, $s0, $t3  
    lw $t2, 0($t4)      # t2 = array[j]
	
	bne $t1, $t2, next2
	addi $t0, $t0, 1	#count++
	next2:
	addi $t5, $t5, 1	#j++
	j loop2
	
	endSubloop:
	addi $t6, $t0, -1
	beq $t6, $zero, unique		#check count == 1 or not
	
	move $a0, $t1
	jal checkInsideArray		#check if that value is already in duplicate array or not
	beq $v0, $zero, printDuplicate
	j Loop
printDuplicate:	
	sw $t1, 0($s4)
	addi $s4, $s4, 4
	
	move $a0, $t1	
	li $v0, 1
	syscall
	
	la $a0, Duplicated
	li $v0, 4
	syscall
	
	move $a0, $t0	
	li $v0, 1
	syscall
	
	la $a0, comma1
	li $v0, 4
	syscall
	
	j Loop
unique:
	sw $t1, 0($s1)
	addi $s1, $s1, 4
	j Loop
endLoop:

#print unique
	la $a0, prompt1
	li $v0, 4
	syscall

	la $t0, tempArr
printLoop:	
	lw $a0, 0($t0)
	beq $a0, $zero, endPrint
	li $v0, 1
	syscall
	
	la $a0, comma
	li $v0, 4
	syscall
	
	addi $t0, $t0, 4
	j printLoop
endPrint:
	li $v0, 10
	syscall
	
	
checkInsideArray:
	subu $sp, $sp, 4
	sw $s4, 0($sp)
	
	la $s4, duplicateArr
checkLoop:
	lw $t4, 0($s4)
	beq $t4, $zero, endCheck
	beq $a0, $t4, isContain
	addi $s4, $s4, 4
	j checkLoop
isContain:
	li $v0, 1
	j endCheck1
	
endCheck:
	li $v0, 0
endCheck1:
	lw $s4, 0($sp)
	addi $sp, $sp, 4
	jr $ra