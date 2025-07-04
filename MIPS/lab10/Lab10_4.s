.data
	Name:	.asciiz "Phan Tran Thanh Huy\nITCSIU22056\n"

	prompt_shape:.asciiz "1. Rectangle Box\n2. Cube\n3. Cylinder\n4. Rectangle Pyramid\nEnter option: "

	prompt_rec:	.asciiz "Enter length, width and height of rectangle box: \n"
	option_rec:	.asciiz "\n1.Volume\n2.Surface area\nEnter option: "
	volume_rec:	.asciiz "Volume of rectangle box: "
	area_rec:	.asciiz "Surface area of rectangle box: "
	
	prompt_cube:	.asciiz "Enter edge of cube: "
	option_cube:	.asciiz "\n1.Volume\n2.Surface area\nEnter option: "
	volume_cube:	.asciiz "Volume of cube: "
	area_cube:		.asciiz "Surface area of cube: "
	
	prompt_cylinder:	.asciiz "Enter radius and height of cylinder: \n"
	option_cylinder:	.asciiz "\n1.Volume\n2.Surface area\nEnter option: "
	volume_cylinder:	.asciiz "Volume of cylinder: "
	area_cylinder:		.asciiz "Surface area of cylinder: "
	pi:			.float 3.141592654
	
	prompt_recPyramid:	.asciiz "Enter length, width and height of rectangle box: \n"
	option_recPyramid:	.asciiz "\n1.Volume\n2.Surface area\nEnter option: "
	volume_recPyramid:	.asciiz "Volume of rectangle box: "
	area_recPyramid:	.asciiz "Surface area of rectangle box: "
	
.text
.globl main
main:
	la $a0, Name
	li $v0, 4
	syscall

	li $s0, 1	#option 1
	li $s1, 2	#option 2
	li $s2, 3
	li $s3, 4
	
	la $a0, prompt_shape
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	
	beq $v0, $s0, Rectangle_box
	beq $v0, $s1, Cube
	beq $v0, $s2, Cylinder
	beq $v0, $s3, Rectangle_Pyramid

Rectangle_box:
	jal calculate_Rectangle
	li $v0, 2
	syscall
	j End
	
Cube:
	jal calculate_Cube
	li $v0, 2
	syscall
	j End
	
Cylinder:
	jal calculate_Cylinder
	li $v0, 2
	syscall
	j End
	
Rectangle_Pyramid:
	jal calculate_Rectangle_Pyramid
	li $v0, 2
	syscall
	j End
	
End:
	li $v0, 10
	syscall
	
calculate_Rectangle_Pyramid:
	la $a0, prompt_recPyramid
	li $v0, 4
	syscall

	li $v0, 6
	syscall 
	mov.s $f1, $f0	#f1 = length
	
	li $v0, 6
	syscall 
	mov.s $f2, $f0	#f2 = width
	
	li $v0, 6
	syscall 
	mov.s $f3, $f0	#f3 = height
	
	la $a0, option_recPyramid
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	
	beq $v0, $s0, volumeRecPyramid
	beq $v0, $s1, areaRecPyramid

	volumeRecPyramid:
	la $a0, volume_recPyramid
	li $v0, 4
	syscall

	mul.s $f4, $f1, $f2		
	mul.s $f4, $f4, $f3		#l.w.h
	
	li.s $f5, 3.0
	div.s $f4, $f4, $f5		#l.w.h/3
	j result
	
	areaRecPyramid:
	la $a0, area_recPyramid
	li $v0, 4
	syscall
	
	mul.s $f5, $f1, $f2		#l.w
	
	li.s $f6, 2.0
	div.s $f6, $f2, $f6		#w/2
	mul.s $f6, $f6, $f6		#(w/2)^2
	mul.s $f7, $f3, $f3		#h^2
	add.s $f6, $f6, $f7		#(w/2)^2 + h^2
	sqrt.s $f6, $f6			
	mul.s $f6, $f1, $f6		#l.sqrt((w/2)^2 + h^2)
	
	li.s $f7, 2.0
	div.s $f7, $f1, $f7		#l/2
	mul.s $f7, $f7, $f7		#(l/2)^2
	mul.s $f8, $f3, $f3		#h^2
	add.s $f7, $f7, $f8		#(l/2)^2 + h^2
	sqrt.s $f7, $f7			
	mul.s $f7, $f2, $f7		#w.sqrt((l/2)^2 + h^2)
	
	add.s $f4, $f5, $f6
	add.s $f4, $f4, $f7		#l.w + l.sqrt((w/2)^2 + h^2) + w.sqrt((l/2)^2 + h^2)
	
	j result
			
calculate_Cylinder:
	la $a0, prompt_cylinder
	li $v0, 4
	syscall

	li $v0, 6
	syscall 	#f1 = radius
	mov.s $f1, $f0
	
	li $v0, 6
	syscall 	#f0 = height
	
	l.s $f2, pi	#f2 = pi
	
	la $a0, option_cylinder
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	
	beq $v0, $s0, volumeCylinder
	beq $v0, $s1, areaCylinder
	
	volumeCylinder:
	la $a0, volume_cylinder
	li $v0, 4
	syscall

	mul.s $f5, $f1, $f1		#r^2
	mul.s $f6, $f0, $f2		#pi.h
	mul.s $f4, $f5, $f6		#pi.r^2.h
	j result
	
	areaCylinder:
	la $a0, area_cylinder
	li $v0, 4
	syscall
	
	mul.s $f5, $f1, $f2		#pi.r
	add.s $f5, $f5, $f5		#2pi.r
	add.s $f6, $f1, $f0		#r+h
	mul.s $f4, $f6, $f5		#2pi.r(r+h)
	j result
	
calculate_Cube:
	la $a0, prompt_cube
	li $v0, 4
	syscall

	li $v0, 6
	syscall 	#f0 = edge
	
	la $a0, option_cube
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	
	beq $v0, $s0, volumeCube
	beq $v0, $s1, areaCube
	
	volumeCube:
	la $a0, volume_cube
	li $v0, 4
	syscall

	mul.s $f4, $f0, $f0		
	mul.s $f4, $f0, $f4		#s^3
	j result
	
	areaCube:
	la $a0, area_cube
	li $v0, 4
	syscall
	
	li.s $f6, 6.0
	mul.s $f5, $f0, $f0		#s^2
	mul.s $f4, $f6, $f5		#6s^2
	j result
	
calculate_Rectangle:
	la $a0, prompt_rec
	li $v0, 4
	syscall

	li $v0, 6
	syscall 
	mov.s $f1, $f0	#f1 = length
	
	li $v0, 6
	syscall 
	mov.s $f2, $f0	#f2 = width
	
	li $v0, 6
	syscall 
	mov.s $f3, $f0	#f3 = height
	
	la $a0, option_rec
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	
	beq $v0, $s0, volumeRec
	beq $v0, $s1, areaRec

	volumeRec:
	la $a0, volume_rec
	li $v0, 4
	syscall

	mul.s $f4, $f1, $f2		
	mul.s $f4, $f4, $f3		#l.w.h
	j result
	
	areaRec:
	la $a0, area_rec
	li $v0, 4
	syscall
	
	mul.s $f5, $f1, $f2		#l.w
	mul.s $f6, $f3, $f2		#l.h
	mul.s $f7, $f1, $f3		#w.h
	add.s $f4, $f5, $f6
	add.s $f4, $f4, $f7		#l.w + l.h + w.h
	
	add.s $f4, $f4, $f4		#2.(l.w + l.h + w.h)
	j result
	
result:
	mov.s $f12, $f4
	jr $ra