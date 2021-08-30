MESSAGE:
.asciz "%d + %d = %d\n"

FAREWELL:
.asciz "Usage: %s n m (with n and m integers) \n"


.text
	.align	4
	.global	main
main:
	mov	ip, sp
	stmfd	sp!, {fp, ip, lr, pc}
	sub	fp, ip, #4
	cmp	r0, #3
	beq	CONT
	ldr	r1, [r1]
	ldr	r0, MSG2
	b	OUT
CONT:
	stmfd	sp!, {r1}
	ldr	r0, [r1, #8]
	bl	atoi
	mov	r2, r0
	ldmfd	sp!, {r1}
	stmfd	sp!, {r2}
	ldr	r0, [r1, #4]
	bl	atoi
	mov	r1, r0
	ldmfd	sp!, {r2}
	add	r3, r1, r2
	ldr	r0, MSG1
OUT:
	bl	printf
	mov	r0, #0
	sub	sp, fp, #12
	ldmfd	sp, {fp, sp, lr}
	bx	lr

MSG1:
	.word MESSAGE
MSG2:
	.word FAREWELL 
