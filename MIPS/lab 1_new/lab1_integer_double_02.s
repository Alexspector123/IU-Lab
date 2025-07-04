.data
input: .asciiz "Enter the number: "
output: .asciiz "\nThe value of the first byte of the number is: "
strName: .asciiz "Phan Tran Thanh Huy"
ID: .asciiz "\nITCSIU22056"
strLine: .asciiz "\n"
number: .word 0
.text
.globl main
main: 

la $a0, strName
li $v0, 4
syscall

la $a0, ID
li $v0, 4
syscall

la $a0, strLine
li $v0, 4
syscall

la $a0, input
li $v0, 4
syscall

li $v0, 5
syscall
sw $v0, number

la $t0, number

lb $a0, 0($t0)
li $v0, 1
syscall

li $v0, 10
syscall