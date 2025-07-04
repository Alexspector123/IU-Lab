.data		# the data segment
strName: .asciiz "Phan Tran Thanh Huy\n"
strID: .asciiz "ITCSIU22056\n"
prompt: .asciiz "Guess a number (1 - 1000): "
win: 	.asciiz	"You win!!\n"
lose: 	.asciiz	"You lose!!\n"
small: .asciiz "Your number is smaller than the secret number!!\n"
big: .asciiz "Your number is bigger than the secret number!!\n"
exit: .asciiz "Thanks for playing!"
newline:.asciiz	"\n"

		.text		# the code segment
		.globl main
main:
	la $a0, strName	
	li $v0, 4		
	syscall

	la $a0, strID		
	li $v0, 4		
	syscall

	li $t0, 0x1fa # 0x1fa --> t0=506
LOOP:
	# print out the prompt
	la $a0, prompt		
	li $v0, 4		
	syscall
	
	# read in an integer
	li $v0, 5			
	syscall
	move $t1, $v0 # move the input number (user) to t1; e.g 506

	beq $0, $t1, EXIT 	

	bne $t0, $t1, LOSE #compare value of t1 and t0
	beq $t0, $t1, WIN
WIN:
	# print out "win"
	la $a0, win		
	li $v0, 4		
	syscall
	jr $ra				# return to caller (__start)
	
LOSE:
	# print out "lose"
	la $a0, lose		
	li $v0, 4		
	syscall
	blt $t1, $t0, SMALL
	bgt $t1, $t0, BIG
SMALL:
	la $a0, small
	li $v0, 4
	syscall
	j LOOP				
BIG:
	la $a0, big
	li $v0, 4
	syscall
	j LOOP
EXIT:
	la $a0, exit
	li $v0, 4
	syscall
	li $v0, 10
	syscall
