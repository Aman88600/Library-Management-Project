#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Getting user choice on entering books
    int response = 0;

    do
    {
        printf("Press 1 to enter books\n");
        printf("Press 0 to exit\n");
        printf("Your response : ");
        scanf("%i", &response);

        if (response == 1)
        {
            while ((getchar()) != '\n')
                ;
            char buffer[101];
            printf("Enter your book name: ");
            // Stores the name into auxiliary memory
            scanf(" %100[^\n]", buffer);
            // Creates a dynamic string
            char *name = (char *)malloc(strlen(buffer) + 1);
            // Sets the value
            strcpy(name, buffer);
            printf("Your name is %s\n", name);
            // Frees the memory
            free(name);
            printf("Your book name is %s", name);
        }
    } while (response == 1);
    return 0;
}