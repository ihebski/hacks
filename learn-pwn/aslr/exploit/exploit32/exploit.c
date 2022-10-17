#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char buf[256];

    gets(buf);
    printf(buf);

    return 0;
}
