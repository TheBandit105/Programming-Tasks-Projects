MESSAGE:
	.asciz "I am programming an ARM in assembly code!\n"

.text
	.align 4
	.global	main
main:
	mov ip, sp                     @ caller SP in IP
	stmfd sp!,{fp, ip, lr, pc}     @ callere Regs store at
 				       @ callee stack
	sub fp, ip, #4                 @ new callee FP
	ldr r0, MSG1                   @ ascii argument to printf 
	bl printf                
	mov r0, #0                     @ return value from main
	sub sp, fp, #12                @ aligning callee SP
	ldmfd sp, {fp, sp, lr}         @ restoring caller Regs
	bx lr

MSG1:
	.word MESSAGE
	
