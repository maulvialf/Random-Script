// gcc -fPIC -shared ptrace.c -o ptrace.so
// gcc -m32 -fPIC -shared ptrace.c -o ptrace.so

long ptrace(int request, int pid, void *addr, void *data) {
    return 0;
}  
