.data
strNameId: .asciiz "\n"
printInitialArray: .asciiz "The initial array: "
printSortedArray: .asciiz "The sorted array: "
strLine: .asciiz "\n"
strSpace: .asciiz " "
arr: .word 43, 6543, 34, 54, 4232, 64, 526, 643, 6435, 423, 4236, 566, 41, 0
sortedArr: .space 1024

.text
.globl main

main:
	la $a0, strNameId
	li $v0, 4
	syscall

	la $a0, printInitialArray
	li $v0, 4
	syscall

	la $a1, arr			# $a1 = address of arr
	jal DISPLAY			# Print the array

	la $a0, strLine
	li $v0, 4
	syscall

	la $a0, arr			# $a0 = address of arr
	li $a1, 0			# Low index of the array which is 0
	li $a2, 13			# High index of the array which is 13
	jal QUICKSORT			# Sort the array by QuickSort

	la $a0, printSortedArray
	li $v0, 4
	syscall

	la $a1, arr			# $a1 = address of arr
	jal DISPLAY			# Print the array

	la $a0, strLine
	li $v0, 4
	syscall

	li $v0, 10
	syscall

SWAP:
	addi $sp, $sp, -16	# Allocate space on the stack

	sw $a0, 0($sp)		# Store array
	sw $a1, 4($sp)		# Store Low
	sw $a2, 8($sp)		# Store High
	sw $t2, 12($sp)		# Store t2 for high

	sll $t1, $a1, 2		# $t1 = Low * 4
	add $t1, $a0, $t1	# $t1 = arr + Low * 4
	lw $s3, 0($t1)		# $s3 = arr[$t1]

	sll $t2, $a2, 2		# $t2 = High * 4
	add $t2, $a0, $t2	# $t2 = arr + High * 4
	lw $s4, 0($t2)		# $s4 = arr[$t2]

	sw $s4, 0($t1)		# arr[$t1] = $s4 (swap a[$t1] and a[$t2])
	sw $s3, 0($t2)		# arr[$t2] = $s3

	lw $t2, 12($sp)		# Load $t2 on the stack	
	addi $sp, $sp, 16
	jr $ra
PARTITION:
	addi $sp, $sp, -16		# Allocate space on the stack
  
	sw $a0, 0($sp)    		# Save array on the stack
	sw $a1, 4($sp)    		# Save low on the stack
 	sw $a2, 8($sp)   		# Save high on the stack
	sw $ra, 12($sp)  		# Save $ra on the stack
    
 	move $s1, $a1		# $s1 = $a1
 	move $s2, $a2		# $s2 = $a2
    
  	sll $t1, $s2, 2		# t1 = high * 4
 	add $t1, $a0, $t1	# t1 = arr + high * 4
	lw $t2, 0($t1)        	# pivot = t2 = arr[high]
    
	addi $t3, $s1, -1	# t3 = i = low - 1
	move $t4, $s1		# t4 = j = low
	addi $t5, $s2, -1	# t5 = high - 1
    
	forloop:
		slt $t6, $t5, $t4	# Check $t6 = 1 if j > high - 1
					#       $t6 = 0 if j <= high - 1
    		bne $t6, $0, endfor	# Check if j > high, go to endfor

    		sll $t1, $t4, 2		# $t1 = low * 4
    		add $t1, $t1, $a0	# $t1 = arr + low * 4
    		lw $t7, 0($t1)		# $t7 = arr[j] = arr[low]
    
    		slt $t8, $t7, $t2	# Check $t8 = 1 if arr[j] > pivot
					# 	$t8 = 0 if arr[j] <= pivot
    		bne $t8, $zero, endfif  # if array[j] <= pivot --> endIf
    
    		addi $t3, $t3, 1	# Increase i++
    		move $a1, $t3
    		move $a2, $t4
    		jal SWAP

		addi $t4, $t4, 1	# j++
		j forloop
    
	endfif:
    		addi $t4, $t4, 1    # j++
    		j forloop

	endfor:
    		addi $a1, $t3, 1	# $a1 = i + 1
    		move $a2, $s2		# $a2 = high
		add $v0, $zero, $a1	# $v0 = $a1
    		jal SWAP            	# Swap(arr[i+1], arr[high])
    
    		lw $ra, 12($sp)		# Return address
    		addi $sp, $sp, 16	# Restore the stack
    		jr $ra
    
QUICKSORT:
		addi $sp, $sp, -16	# Allocate space on the stack

		sw $a0, 0($sp)		# save arr
		sw $a1, 4($sp)		# save low
		sw $a2, 8($sp)		# save high
		sw $ra, 12($sp)  	# Return address

		move $t0, $a2		# $t0 = high

		slt $t1, $a1, $t0	# Check $t1 = 1 if low > high
					# 	$t1 = 0 if low <= high

 		beq $t1, $zero, ENDIF	# if low <= high, go to ENDIF
    
 		jal PARTITION

 		move $s0, $v0    	# pivot $s0 = $v0
    
    		lw $a1, 4($sp)   	# load low
    		addi $a2, $s0, -1  	# pivot - 1
    		jal QUICKSORT    	# quicksort(array, low, pivot - 1)
   
    		addi $a1, $s0, 1  	# pivot + 1
    		lw $a2, 8($sp)  	# load high
    		jal QUICKSORT    	# quicksort(array, pivot + 1, high)
    
ENDIF:
      
    		lw $a0, 0($sp)    	# Restore a0
    		lw $a1, 4($sp)    	# Restore a1
    		lw $a2, 8($sp)		# Restore a2
    		lw $ra, 12($sp)     	# Restore return address
    		addi $sp, $sp, 16       # Restore the stack
    		jr $ra  		# Return the caller

DISPLAY:
	lw $t2, 0($a1)			# Load $t2 = a[i]
	beq $t2, $0, END_FUNC		# Check if $t2 = 0, go to the END_FUNC

	move $a0, $t2			# Print $t2 = a[i]
	li $v0, 1
	syscall

	la $a0, strSpace
	li $v0, 4
	syscall

	addi $a1, $a1, 4		# Move to the next element
	j DISPLAY

END_FUNC:
	j $ra