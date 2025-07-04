.data		# the data segment
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
prompt: .asciiz "Input: "
output: .asciiz "Output: "
buffer: .space 100
newline: .asciiz "\n"

.text		# the code segment
.globl main
main:
	la $a0, strName	
	li $v0, 4		
	syscall

	la $a0, strID		
	li $v0, 4		
	syscall

	# print out the prompt
	la $a0, prompt		
	li $v0, 4		
	syscall
	
	# read a string
	li $v0,8
	la $a0, buffer
	li $a1, 100
	syscall
    
    # print out the result
	la $a0, output
	li $v0, 4		
	syscall
	
	la $t0, buffer
	li $s0, 32

        lb $t1, 0($t0)
        sub $t1, $t1, 32
        sb $t1, 0($t0)
loop:
    lb $t1, 0($t0)
    beq $t1, 32, CASE
    beq $t1, 0, exit
    addi $t0, $t0, 1
    j loop
CASE:
addi $t0, $t0, 1
lb $t1, 0($t0)
blt $t1, 'a', loop
bgt $t1, 'z', loop
sub $t1, $t1, 32
sb $t1, 0($t0)
addi $t0, $t0, 1
j loop
exit:
	la $a0, buffer
	li $v0, 4
	syscall
	
	jr $ra				# return to caller (__start)
