.data
n: .word 0
input: .asciiz "Enter the number: "
output: .asciiz "The result is: "
strLine: .asciiz "\n"

.text
.globl main

main:
LOOP1:
la $a0, input
li $v0, 4
syscall

li $v0, 7
syscall

mov.d $f2, $f0
cvt.w.d $f2, $f2
mfc1 $t0, $f2
blt $t0, $0, LOOP1

mov.d $f2, $f0
sqrt.d $f2, $f2

la $a0, output
li $v0, 4
syscall

mov.d $f12, $f2
li $v0, 3
syscall

li $v0, 10
syscall
