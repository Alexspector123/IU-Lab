.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ID: ITCSIU22056\n" 

.text
.globl main

main:

la $a0, strName
li $v0, 4
syscall	

la $a0, strID
li $v0, 4
syscall	

li $v0, 10
syscall	