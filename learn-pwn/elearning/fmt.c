#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<string.h>

int target;

void deadcode()

{

char *information = "The execution flow was redirected!";
printf(information);
_exit(1);

}
void vuln()
{
char buffer[512];
fgets(buffer, sizeof(buffer), stdin);
printf(buffer);
exit(1);
}
int main(int argc, char **argv)
{
vuln();
}
