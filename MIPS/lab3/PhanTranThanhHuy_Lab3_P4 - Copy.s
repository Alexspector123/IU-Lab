.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
strLine: .asciiz "\n"
strPoint: .asciiz ": "
arr: .asciiz "abdeefggff"
size: .word 0
brr: .space 30
char: .space 1

.text
.globl main

main:
la $a0, strName
li $v0, 4
syscall

la $a0, strID
li $v0, 4
syscall

la $t0, arr
lw $s0, size

LOOP:
lb $t1, 0($t0)
addi $s0, $s0, 1
addi $t0, $t0, 1
bne $t1, 0, LOOP

addi $s0, $s0, -1
sw $s0, size

la $t0, arr
lw $s0, size

LOOP1:
la $t1, brr
lb $t2, 0($t0)
li $s1, 'a'
sub $t3, $t2, $s1
mul $t3, $t3, 4
lw $t4, 0($t1)
add $t1, $t1, $t3
lw $t4, 0($t1)
addi $t4, $t4, 1
sw $t4, 0($t1)
addi $t0, $t0, 1
addi $s0, $s0, -1
bne $s0, $0, LOOP1

la $a0, arr
li $v0, 4
syscall

la $a0, strLine
li $v0, 4
syscall

lw $s0, size
lw $s2, size
addi $s2, $s2, 1

LOOP3:
addi $s2, $s2, -1
beq $s0, $0, exit
la $t1, brr
li $s1, 26

LOOP2:
lw $t2, 100($t1)
beq $t2, $s2, CASE
addi $t1, $t1, -4
addi $s1, $s1, -1
beq $s1, $0, LOOP3
j LOOP2

CASE:
addi $t5, $s1, -1
li $t3, 'a'
add $t4, $t5, $t3
sb $t4, char
la $a0, char
li $v0, 4
syscall
la $a0, strPoint
li $v0, 4
syscall
move $a0, $t2
li $v0, 1
syscall
la $a0, strLine
li $v0, 4
syscall
addi $t1, $t1, -4
addi $s1, $s1, -1
sub $s0, $s0, $t2
beq $s1, $0, LOOP3
j LOOP2

exit:
li $v0, 10
syscall