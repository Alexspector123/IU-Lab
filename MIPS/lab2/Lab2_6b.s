.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
input: .asciiz "Enter the binary number: "
output: .asciiz "The decimal number is: "
binary: .space 20
decimal: .word 0
limit: .word -2

.text
.globl main

main:
la $a0, strName	
li $v0, 4		
syscall

la $a0, strID		
li $v0, 4		
syscall

la $a0, input		
li $v0, 4		
syscall

la $a0, binary
li $a1, 20
li $v0, 8
syscall

la $t0, binary
lw $s1, limit
lb $t1, 0($t0)

loop2:
addi $t0, $t0, 1
addi $s1, $s1, 1
sw $s1, limit
lb $t1, 0($t0)
bne $t1, 0, loop2

la $a0, output		
li $v0, 4		
syscall

la $t0, binary
lw $s1, limit
li $s2, 2
li $t4, 0

loop:
lb $t1, 0($t0)
lw $s0, decimal
beq $t1, 49, case1
beq $t1, 48, case0

case1:
li $t2, 0
li $t3, 1
beq $s1, $t4, else
loop1:
mul $t3, $t3, $s2
addi $t2, $t2, 1
bne $t2, $s1, loop1
add $s0, $s0, $t3
sw $s0, decimal
sub $s1, $s1, 1
addi $t0, $t0, 1
j loop

else:
addi $s0, $s0, 1
sw $s0, decimal
j exit

case0:
beq $s1, $t4, exit
sub $s1, $s1, 1
addi $t0, $t0, 1
j loop

exit:
lw $a0, decimal
li $v0, 1
syscall

li $v0, 10
syscall

