MESSAGE:
	.asciz "%d + %d = %d\n"

.text
	.align 4
	.global	main
main:
	mov ip, sp                     @ caller SP in IP
	stmfd sp!,{fp, ip, lr, pc}     @ callere Regs store at
 				       @ callee stack
	sub fp, ip, #4                 @ new callee FP
	ldr r0, MSG1                   @ ascii argument to printf 
        mov r1, #2
	mov r2, #3
	add r3, r1, r2
	bl printf                
	mov r0, #0                     @ return value from main
	sub sp, fp, #12                @ aligning callee SP
	ldmfd sp, {fp, sp, lr}         @ restoring caller Regs
	bx lr

MSG1:
	.word MESSAGE	
