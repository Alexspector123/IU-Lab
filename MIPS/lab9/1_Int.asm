.data
strLine: .asciiz "\n"
arr: .word 43, 6543, 34, 54, 4232, 64, 526, 643, 6435, 423, 4236, 566, 0

.text
.globl main

main:
	la $a1, arr
	li $s0, 0
	jal LEN

	move $a0, $s0
	li $v0, 1
	syscall

	li $v0, 10
	syscall

LEN:
	lw $t2, 0($a1)
	beq $t2, $0, END_FUNC

	add $a1, $a1, 4
	add $s0, $s0, 1
	j LEN

END_FUNC:
	j $ra