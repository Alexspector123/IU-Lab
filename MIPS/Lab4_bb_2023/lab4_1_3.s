.data

.text
.globl main

main:
	li $t1, 0xdeadbeef
	or $t4, $t4, $t1

if:
	blt $t5, 8, loop
	j exit

loop:
	andi $t3, $t4, 0xF
	or $t2, $t2, $t3
	beq $t5, 7, exit
	rol $t2, $t2, 4
	ror $t4, $t4, 4
	addi $t5, $t5, 1
	j if

exit:
	li $v0, 10
	syscall