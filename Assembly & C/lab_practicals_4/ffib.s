	.arch armv5t
	.fpu softvfp
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 2
	.eabi_attribute 18, 4
	.file	"ffib.c"
	.text
	.align	2
	.global	fib
	.type	fib, %function
fib:
	@ args = 0, pretend = 0, frame = 128
	@ frame_needed = 0, uses_anonymous_args = 0
	cmp	r0, #1
	stmfd	sp!, {r4, r5, r6, r7, r8, r9, sl, fp, lr}
	sub	sp, sp, #132
	movle	r1, #0
	str	r0, [sp, #44]
	strle	r1, [sp, #48]
	ble	.L3
	ldr	r2, [sp, #44]
	ldr	r3, [sp, #44]
	sub	r2, r2, #1
	str	r2, [sp, #120]
	ldr	r2, [sp, #44]
	sub	r3, r3, #3
	mov	r1, #0
	str	r3, [sp, #124]
	str	r1, [sp, #48]
.L28:
	ldr	r3, [sp, #120]
	cmp	r3, #1
	suble	r2, r2, #2
	movle	r1, #0
	strle	r2, [sp, #32]
	strle	r1, [sp, #52]
	ble	.L5
	ldr	r1, [sp, #124]
	sub	r3, r2, #4
	bic	r1, r1, #1
	sub	r2, r2, #2
	str	r3, [sp, #116]
	str	r2, [sp, #32]
	str	r2, [sp, #112]
	rsb	r3, r1, r3
	mov	r2, #0
	str	r1, [sp, #8]
	str	r2, [sp, #52]
	str	r3, [sp, #4]
.L27:
	ldr	r1, [sp, #112]
	cmp	r1, #1
	movle	r3, #0
	mov	r2, r1
	strle	r3, [sp, #56]
	ble	.L7
	ldr	r1, [sp, #112]
	ldr	r3, [sp, #112]
	sub	r1, r1, #1
	sub	r3, r3, #3
	str	r1, [sp, #104]
	str	r3, [sp, #108]
	mov	r1, #0
	str	r1, [sp, #56]
.L26:
	ldr	r3, [sp, #104]
	cmp	r3, #1
	suble	r2, r2, #2
	movle	r1, #0
	strle	r2, [sp, #36]
	strle	r1, [sp, #60]
	ble	.L9
	ldr	r1, [sp, #108]
	sub	r3, r2, #4
	bic	r1, r1, #1
	sub	r2, r2, #2
	str	r3, [sp, #100]
	str	r2, [sp, #36]
	str	r2, [sp, #96]
	rsb	r3, r1, r3
	mov	r2, #0
	str	r1, [sp, #16]
	str	r2, [sp, #60]
	str	r3, [sp, #12]
.L25:
	ldr	r1, [sp, #96]
	cmp	r1, #1
	movle	r3, #0
	mov	r2, r1
	strle	r3, [sp, #64]
	ble	.L11
	ldr	r1, [sp, #96]
	ldr	r3, [sp, #96]
	sub	r1, r1, #1
	sub	r3, r3, #3
	str	r1, [sp, #88]
	str	r3, [sp, #92]
	mov	r1, #0
	str	r1, [sp, #64]
.L24:
	ldr	r3, [sp, #88]
	cmp	r3, #1
	suble	r2, r2, #2
	movle	r1, #0
	strle	r2, [sp, #40]
	strle	r1, [sp, #68]
	ble	.L13
	ldr	r1, [sp, #92]
	sub	r3, r2, #4
	bic	r1, r1, #1
	sub	r2, r2, #2
	str	r3, [sp, #84]
	str	r2, [sp, #40]
	str	r2, [sp, #80]
	rsb	r3, r1, r3
	mov	r2, #0
	str	r1, [sp, #24]
	str	r2, [sp, #68]
	str	r3, [sp, #20]
.L23:
	ldr	r1, [sp, #80]
	cmp	r1, #1
	movle	r3, #0
	mov	r2, r1
	strle	r3, [sp, #72]
	ble	.L15
	ldr	r1, [sp, #80]
	ldr	r3, [sp, #80]
	sub	r1, r1, #1
	str	r1, [sp, #76]
	sub	fp, r3, #3
	ldr	r3, [sp, #76]
	mov	r1, #0
	str	r1, [sp, #72]
.L22:
	cmp	r3, #1
	suble	r9, r2, #2
	movle	r8, #0
	ble	.L17
	bic	r1, fp, #1
	sub	r7, r2, #4
	sub	r9, r2, #2
	mov	r6, r9
	mov	r8, #0
	rsb	sl, r1, r7
	str	r1, [sp, #28]
.L21:
	cmp	r6, #1
	mov	r4, r6
	movle	r5, #0
	ble	.L19
	mov	r5, #0
.L20:
	sub	r0, r4, #1
	bl	fib
	sub	r4, r4, #2
	cmp	r4, #1
	add	r5, r5, r0
	bgt	.L20
	and	r4, r7, #1
.L19:
	sub	r6, r6, #2
	cmp	r6, sl
	add	r3, r5, r4
	add	r8, r8, r3
	sub	r7, r7, #2
	bne	.L21
	ldr	r2, [sp, #28]
	rsb	r3, r2, fp
.L17:
	ldr	r1, [sp, #72]
	add	r3, r8, r3
	add	r1, r1, r3
	cmp	r9, #1
	ldr	r3, [sp, #76]
	mov	r2, r9
	sub	r3, r3, #2
	str	r1, [sp, #72]
	str	r3, [sp, #76]
	sub	fp, fp, #2
	bgt	.L22
	ldr	r1, [sp, #84]
	and	r2, r1, #1
.L15:
	ldr	r3, [sp, #80]
	ldr	r1, [sp, #20]
	sub	r3, r3, #2
	cmp	r3, r1
	ldr	r1, [sp, #72]
	str	r3, [sp, #80]
	add	r3, r1, r2
	ldr	r2, [sp, #68]
	add	r2, r2, r3
	ldr	r3, [sp, #84]
	str	r2, [sp, #68]
	sub	r3, r3, #2
	str	r3, [sp, #84]
	bne	.L23
	ldr	r1, [sp, #92]
	ldr	r2, [sp, #24]
	rsb	r3, r2, r1
.L13:
	ldr	r1, [sp, #68]
	ldr	r2, [sp, #40]
	add	r3, r1, r3
	ldr	r1, [sp, #64]
	cmp	r2, #1
	add	r1, r1, r3
	ldr	r3, [sp, #88]
	str	r1, [sp, #64]
	ldr	r1, [sp, #92]
	sub	r3, r3, #2
	sub	r1, r1, #2
	str	r3, [sp, #88]
	str	r1, [sp, #92]
	bgt	.L24
	ldr	r3, [sp, #100]
	and	r2, r3, #1
.L11:
	ldr	r1, [sp, #96]
	ldr	r3, [sp, #12]
	sub	r1, r1, #2
	cmp	r1, r3
	str	r1, [sp, #96]
	ldr	r1, [sp, #64]
	add	r3, r1, r2
	ldr	r2, [sp, #60]
	add	r2, r2, r3
	ldr	r3, [sp, #100]
	str	r2, [sp, #60]
	sub	r3, r3, #2
	str	r3, [sp, #100]
	bne	.L25
	ldr	r1, [sp, #108]
	ldr	r2, [sp, #16]
	rsb	r3, r2, r1
.L9:
	ldr	r1, [sp, #60]
	ldr	r2, [sp, #36]
	add	r3, r3, r1
	ldr	r1, [sp, #56]
	cmp	r2, #1
	add	r1, r1, r3
	ldr	r3, [sp, #104]
	str	r1, [sp, #56]
	ldr	r1, [sp, #108]
	sub	r3, r3, #2
	sub	r1, r1, #2
	str	r3, [sp, #104]
	str	r1, [sp, #108]
	bgt	.L26
	ldr	r3, [sp, #116]
	and	r2, r3, #1
.L7:
	ldr	r1, [sp, #112]
	ldr	r3, [sp, #4]
	sub	r1, r1, #2
	cmp	r1, r3
	str	r1, [sp, #112]
	ldr	r1, [sp, #56]
	add	r3, r2, r1
	ldr	r2, [sp, #52]
	add	r2, r2, r3
	ldr	r3, [sp, #116]
	str	r2, [sp, #52]
	sub	r3, r3, #2
	str	r3, [sp, #116]
	bne	.L27
	ldr	r1, [sp, #124]
	ldr	r2, [sp, #8]
	rsb	r3, r2, r1
.L5:
	ldr	r1, [sp, #52]
	ldr	r2, [sp, #32]
	add	r3, r3, r1
	ldr	r1, [sp, #48]
	cmp	r2, #1
	add	r1, r1, r3
	ldr	r3, [sp, #120]
	str	r1, [sp, #48]
	ldr	r1, [sp, #124]
	sub	r3, r3, #2
	sub	r1, r1, #2
	str	r3, [sp, #120]
	str	r1, [sp, #124]
	bgt	.L28
	ldr	r2, [sp, #44]
	and	r2, r2, #1
	str	r2, [sp, #44]
.L3:
	ldr	r3, [sp, #48]
	ldr	r1, [sp, #44]
	add	r0, r3, r1
	add	sp, sp, #132
	ldmfd	sp!, {r4, r5, r6, r7, r8, r9, sl, fp, pc}
	.size	fib, .-fib
	.ident	"GCC: (Ubuntu 4.3.3-5ubuntu4) 4.3.3"
	.section	.note.GNU-stack,"",%progbits
