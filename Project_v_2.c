#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Getting user choice on entering books
    int response = 0;

    // Loop will run till the response is not 0
    do
    {
        printf("Press 1 to enter books\n");
        printf("Press 0 to exit\n");
        printf("Your response : ");
        scanf("%i", &response);

        if (response == 1)
        {
            // Cleating the input buffer
            while ((getchar()) != '\n')
                ;

            // Getting the inputs
            char Book[50] = "empty";
            int quantity = 0;
            printf("Enter Book name : ");
            fgets(Book, 50, stdin);
            printf("Enter book quantity : ");
            scanf("%i", &quantity);

            // Saving inputs in text file
            FILE *fptr;

            fptr = fopen("Project_v_2.txt", "a");
            long size = 0;
            // Checking if the file is made of not
            if (fptr)
            {
                // File is open
                fseek(fptr, 0, SEEK_END);
                size = ftell(fptr);
                if (size == 0)
                {
                    // File is closed in read mode
                    fclose(fptr);
                    // File is opned in write mode
                    fptr = fopen("Project_v_2.txt", "w");
                    fprintf(fptr, "Book name is %s", Book);
                    fprintf(fptr, "Book quantity is %i", quantity);
                    // File is closed in write mode
                    fclose(fptr);
                }
                else
                {
                    // File is closed in read mode
                    fclose(fptr);
                    // File is opned in append mode
                    fptr = fopen("Project_v_2.txt", "a");
                    fprintf(fptr, "\nBook name is %s", Book);
                    fprintf(fptr, "Book quantity is %i", quantity);
                    // File is closed in append mode
                    fclose(fptr);
                }
            }

            // Writing in the file
            // fprintf(fptr, "Book name is %s", Book);
            // fprintf(fptr, "Book quantity is %i", quantity);
            // Closing the file
            // fclose(fptr);
        }
    } while (response == 1);
    return 0;
}