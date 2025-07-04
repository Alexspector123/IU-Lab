.data		# the data segment
prompt: .asciiz "Guess a number (1 - 1000): "
win: 	.asciiz	"You win!!\n"
lose: 	.asciiz	"You lose!!\n"
newline:.asciiz	"\n"

		.text		# the code segment
		.globl main
main:
	
	li $t0, 0x1fa # 0x1fa --> t0=506
	
	# print out the prompt
	la $a0, prompt		
	li $v0, 4		
	syscall
	
	# read in an integer
	li $v0, 5			
	syscall
	move $t1, $v0 # move the input number (user) to t1; e.g 506
	
	bne $t0, $t1, LOSE #compare value of t1 and t0
	beq $t0, $t1, WIN
WIN:
	# print out "win"
	la $a0, win		
	li $v0, 4		
	syscall			# return to caller (__start)
	
LOSE:
	# print out "lose"
	la $a0, lose		
	li $v0, 4		
	syscall	
	
	jr $ra				# return to caller (__start)
