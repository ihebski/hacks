#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//gcc -m64 -o chapter_4 chapter_4.c -no-pie -fno-stack-protector

void check_username() {
    char name[32];

    puts("Name?");
    fgets(name, 200, stdin);

    if(strcmp(name, "admin\n") == 0) {
        puts("Nope. Invalid username.");
    }
    else {
        puts("OK");
    }
}

int main(int argc, char **argv) {
    check_username();
    return 0;
}
