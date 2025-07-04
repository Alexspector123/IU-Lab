.data
name: .asciiz "Name: Phan Tran Thanh Huy\n"
ID: .asciiz "ID: ITCSIU22056"
strLine: .asciiz "\n"
.text
.globl main
main:
la $a0, name
li $v0, 4
syscall

la $a0, ID
li $v0, 4
syscall

la $a0, strLine
li $v0, 4
syscall

li $v0,10
syscall