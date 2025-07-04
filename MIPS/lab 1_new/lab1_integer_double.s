.data
input: .asciiz "Enter the number: "
output: .asciiz "\nThe number is: "
.text
.globl main
main: 
# enter the number
la $a0, input
li $v0, 4
syscall

# Get the user's number
li $v0, 5
syscall

# Store the number in $t0
move $t0, $v0

# Display
la $a0, output
li $v0, 4
syscall

move $a0, $t0
li $v0, 1
syscall
jr $ra