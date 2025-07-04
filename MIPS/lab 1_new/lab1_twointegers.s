.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ID: ITCSIU22056\n" 
input1: .asciiz "Enter the number 1: "
input2: .asciiz "\nEnter the number 2: "
result: .asciiz "The result is: "
strLine: .asciiz "\n"

.text
.globl main

main: 
la $a0, strName
li $v0, 4
syscall	

la $a0, strID
li $v0, 4
syscall	

la $a0, input1
li $v0, 4
syscall

li $v0, 5
syscall

move $t0, $v0

la $a0, input2
li $v0, 4
syscall

li $v0, 5
syscall

move $t1, $v0

add $t2, $t0, $t1

la $a0, result
li $v0, 4
syscall

move $a0, $t2
li $v0, 1
syscall

la $a0, strLine
li $v0, 4
syscall
jr $ra