.data
nameId: .asciiz "Phan Tran Thanh Huy\nITCSIU22056"
inputRange: .asciiz "Enter the range: "
inputArray: .asciiz "Enter the array: "
outputArray: .asciiz "Your array is: "
stringSpace: .asciiz " "
stringLine: .asciiz "\n"
printResult: .asciiz "The sum all elements of the array: "
n: .word 0
arr: .space 100

.text
.globl main

main:
	la $a0, nameId		#Print the information of student
	li $v0, 4
	syscall

	la $a0, stringLine
	li $v0, 4
	syscall

	la $a0, inputRange
	li $v0, 4
	syscall

	li $v0, 5		#Enter the range of array
	syscall
	sw $v0, n		#Save v0 to n

	la $a0, inputArray
	li $v0, 4
	syscall

	la $t0, arr		#load the array to t0
	lw $s0, n		#load n to s0

INPUT:				#Enter the array
	li $v0, 5
	syscall
	sw $v0, 0($t0)		#save v0 to t0 
	addi $t0, $t0, 4	#move to the next element of the array
	addi $s0, $s0, -1	#decrease counter
	bne $s0, $0, INPUT	#return if s0 = 0

	la $a0, outputArray
	li $v0, 4
	syscall

	la $t0, arr		#load the array to t0
	lw $s0, n		#load n to s0

OUTPUT:				#Print the array
	lw $t1, 0($t0)		#Load t0 to t1
	move $a0, $t1		#Print the element of the array
	li $v0, 1
	syscall
	la $a0, stringSpace
	li $v0, 4
	syscall
	addi $t0, $t0, 4	#move to the next element of the array
	addi $s0, $s0, -1	#decrease counter
	bne $s0, $0, OUTPUT	#return if s0 = 0

	la $a0, stringLine
	li $v0, 4
	syscall

	la $a0, printResult
	li $v0, 4
	syscall

	la $a0, arr		#load the array to t0
	lw $a1, n		#load n to a1
	jal SUM			#Call the recursive

	move $a0, $v0		#move v0 to a0		
	li $v0, 1		#Print the result
	syscall

	li $v0, 10
	syscall

SUM:				#The recursive function
	addi $sp, $sp, -8
	sw $ra, 0($sp)
	sw $s0, 4($sp)

	li $v0, 0		#load 0 to v0. Using v0 as the sum
	beq $a1, $0, EXIT	#to the EXIT if a1 = 0
	lw $t0, 0($a0)		#load the element of the array to t0
	move $s0, $t0		#move t0 to s0
	addi $a0, $a0, 4	#move to the next element of the array
	addi $a1, $a1, -1	#Decrease counter
	jal SUM			
	add $v0, $v0, $s0	#Compute the sum by adding s0 to v0

EXIT:
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	addi $sp, $sp, 8
	jr $ra