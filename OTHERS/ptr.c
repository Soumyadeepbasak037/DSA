#include <stdio.h>

struct L
{
    char name[50];
};
int main()
{
    struct L la;
    strcpy(la.name, "La");
    printf("Name: %s\n", la.name);
}
