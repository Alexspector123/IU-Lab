.data
	Name:		.asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"
    comma: 		.asciiz ", "
	prompt2:	.asciiz "\nThe second max element: "
	prompt3:	.asciiz ", found in the index "
	array:	.space	60
	prompt:	.asciiz "Enter your array: \n"
	prompt1:.asciiz "The final array: "
	
.text
.globl main
main:

	la $a0, Name
	li $v0, 4
	syscall

	la $s0, array
	li $t1, 15
	li $t5, 3
	
	la $a0, prompt
	li $v0, 4
	syscall
	
inputLoop:
	beq $t1, $zero, end
	li $v0, 5
	syscall
	move $t2, $v0	#t2 = input
	
	div $t3, $t2, $t5	#t3 = t2/3
	mfhi $t4
	beq $t4, $zero, divideByThree	#if t2%3 == 0 --> divideByThree
	
	move $a0, $t2
	jal closestDivideByThree
	move $t2, $v0
	j next1
	
divideByThree:
	move $t2, $t3
next1:
	sw $t2, 0($s0)
	addi $t1, $t1, -1	#size--
	addi $s0, $s0, 4
	j inputLoop
end:
	li $t1, 15
	la $s0, array
	
		
	la $a0, prompt1
	li $v0, 4
	syscall
	
print_loop:
	beq $t1, $zero, end_print
	lw $a0, 0($s0)
	li $v0, 1
	syscall
	
	la $a0, comma
	li $v0, 4
	syscall
	
	addi $s0, $s0, 4
	addi $t1, $t1, -1
	j print_loop
end_print:

#FIND SECOND MAX
	la $a0, prompt2
	li $v0, 4
	syscall
	
	la $a0, array
	li $a1, 15
	jal secondLargest
	move $t0, $v0	#$t0 = secondLargest
	move $a0, $v0
	li $v0, 1
	syscall
	
	la $s0, array
    li $t1, 15		#size = 15
	li $t2, 1		#i = 1
	
	la $a0, prompt3
	li $v0, 4
	syscall
	
printIndexLoop:
	beq $t2, $t1, end_printIndex
	lw $t3, 0($s0)
	beq $t3, $t0, print_index
	j next_index
print_index:
	move $a0, $t2
	li $v0, 1
	syscall
	la $a0, comma
	li $v0, 4
	syscall
next_index:
	addi $t2, $t2, 1		#i++
	addi $s0, $s0, 4
	j printIndexLoop
end_printIndex:
	li $v0, 10
	syscall
	
secondLargest:
	move $t0, $a0	#load array to t0
	move $t1, $a1	#load size to t1

	li $s2, 1	#first index i = 1
	li $s0, 0	#first
	li $s1, -1	#second
	li $s3, -1	

loop:
	beq $s2, $t1, end_loop
	sll $t3, $s2, 2
	add $t4, $t0, $t3
	lw $t2, 0($t4)	#arr[i]
	
	sll $t3, $s0, 2
	add $t4, $t0, $t3
	lw $t3, 0($t4)	#arr[first]
	
	blt $t2, $t3, else1	#check arr[i] < arr[first]
	move $s1, $s0	#second = first
	move $s0, $s2	#first = i
	j next
else1:
	sll $t3, $s1, 2
	add $t4, $t0, $t3
	lw $t3, 0($t4)	#arr[second]

	beq $s1, $s3, do	#if second = -1 --> do
	blt $t3, $t2, do	#if arr[second] < arr[i] --> do
	j next
do: 
	move $s1, $s2	#second = i
	
next:
	addi $s2, $s2, 1	#i++
	j loop
end_loop:
	sll $t3, $s1, 2
	add $t4, $t0, $t3
	lw $t3, 0($t4)	#arr[second]

	move $v0, $t3	#return arr[second]
	jr $ra
	
closestDivideByThree:
	subu $sp, $sp, 20
	sw $t0, 0($sp)
	sw $t1, 4($sp)
	sw $t2, 8($sp)
	sw $t3, 12($sp)
	sw $t5, 16($sp)
	
	move $t0, $a0
	move $t1, $t0
	move $t2, $t0
	
check_loop_1:
	addi $t1, $t1, 1
	div $t3, $t1, 3
	mfhi $t4
	beq $t4, $zero, satisfied_1
	j check_loop_1
satisfied_1:
	move $t5, $t1
	
check_loop_2:
	addi $t2, $t2, -1
	div $t3, $t2, 3
	mfhi $t4
	beq $t4, $zero, satisfied_2
	j check_loop_2

satisfied_2:
	move $t6, $t2
	
	sub $t7, $t5, $t0
	sub $t8, $t0, $t6
	
	blt $t7, $t8, else
	move $v0, $t6
	j end_check
else:
	move $v0, $t5
end_check:
	lw $t0, 0($sp)
	lw $t1, 4($sp)
	lw $t2, 8($sp)
	lw $t3, 12($sp)
	lw $t5, 16($sp)
	addi $sp, $sp, 20
	jr $ra