#include <stdio.h>

int main() {
    char buffer[32];
    puts("Simple ROP.\n");
    gets(buffer);

    return 0;
}
