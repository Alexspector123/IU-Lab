.data
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
input: .asciiz "Input a, b, c, d: "
strLine: .asciiz "\n"
output1: .asciiz "The result of F is: "
output2: .asciiz "The result of G is: "
aNum: .word 0
bNum: .word 0
cNum: .word 0
dNum: .word 0

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
sw $v0,aNum

li $v0, 5
syscall
sw $v0, bNum

li $v0, 5
syscall
sw $v0, cNum

li $v0, 5
syscall
sw $v0, dNum

lw $t0, aNum
lw $t1, bNum
lw $t2, cNum
lw $t3, dNum

mul $t4, $t0, $t0
add $t0, $t0, $t1
sub $t2, $t2, $t3

mul $t5, $t0, $t2

mtc1 $t4, $f0
mtc1 $t5, $f2

cvt.d.w $f0, $f0
cvt.d.w $f2, $f2

la $a0, output1
li $v0, 4
syscall

div.d $f12, $f2, $f0
li $v0, 3
syscall

la $a0, strLine
li $v0, 4
syscall

lw $t0, aNum
lw $t1, bNum
lw $t2, cNum
lw $t3, dNum

sub $t4, $t2, $t0
addi $t0, $t0, 1
addi $t1, $t1, 2
addi $t2, $t2, -3

mul $t5, $t0, $t1
mul $t5, $t5, $t2
div $t5, $t4

mtc1 $t4, $f0
mtc1 $t5, $f2

cvt.d.w $f0, $f0
cvt.d.w $f2, $f2

la $a0, output2
li $v0, 4
syscall

div.d $f12, $f2, $f0
li $v0, 3
syscall

li $v0, 10
syscall
