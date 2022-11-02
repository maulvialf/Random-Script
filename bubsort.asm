extern scanf
extern printf
extern fflush
 
section .data
    output db "%d ",0
    pinal db "%d",10,0
     
    input db "%d", 0
    baca_int db "%d", 0
    awal dq 0.0
      
section .bss
    number resb 1000
    hasil resb 1000
    n resb 1000
    m resb 1000
    i resb 1000
    count resb 1000
 
section .text
      
    global main
 
ngesort:
    push ebp
    mov ebp, esp
    mov esi, 0
    mov edx, 0
loop1: 
     
    mov ecx, edx
    loop2:
        ; komper
        mov eax, dword[4*edx+number] ; sebelum
        cmp eax, dword[4*ecx+number+4] ; setelah
        jl engga
         
        ; nuker
        xchg eax, dword[4*ecx+number+4]
        mov dword[4*edx+number], eax
         
        engga:
        inc ecx
        cmp ecx, dword[n]
        jl loop2
                 
     
    inc edx
    cmp edx, dword[n]
    jl loop1
    jmp ngeprint
     
     
baca:
    mov eax, esi
    mov edi, 4
    mul edi
    add eax, number
    push eax
    push input
    call scanf 
    add esp, 8
    inc esi
    cmp esi, dword[n]
    jl baca
    push dword[n]
    push number
    call ngesort
     
     
     
main:
    push n
    push input
    call scanf
    add esp, 8
    mov ecx, [n]
    mov edx, m
    dec ecx
    mov [edx], ecx
    inc ecx
    mov esi, 0
    jmp baca
 
ngeprint:
    mov esi, 0
     
    haha:
        push dword[4*esi+number+4]
        push output
        call printf
        add esp, 8
        inc esi
        cmp esi, dword[m]
        jl haha
     
    push dword[4*esi+number+4]
    push pinal
    call printf
    add esp, 8
    push 0
    call fflush
    mov eax, 1
    mov ebx, 0
    int 0x80
