.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ID: ITCSIU22056\n"
input: .asciiz "Input the number: "
output: .asciiz "The number: "
strSpace: .asciiz "\n"

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

li $v0, 5
syscall
move $t0, $v0
la $a0, output
li $v0, 4
syscall

move $a0, $t0
li $v0, 1
syscall

li $v0, 10
syscall	