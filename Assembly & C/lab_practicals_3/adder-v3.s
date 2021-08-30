MESSAGE:
.asciz "%d parameters. 1st arg: %s, 2nd arg: %s\n"

.text
	.align 4
	.global	main
main:
	mov	ip, sp
	stmfd	sp!, {fp, ip, lr, pc}
	sub	fp, ip, #4
	ldr	r3, [r1, #8]
	ldr	r2, [r1, #4]
	mov	r1, r0
	ldr	r0, MSG1
	bl	printf
	mov	r0, #0
	sub	sp, fp, #12
	ldmfd	sp, {fp, sp, lr}
	bx	lr

MSG1:
	.word MESSAGE
