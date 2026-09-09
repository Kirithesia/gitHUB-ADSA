#include <stdio.h>
#include <conio.h>

void main()
{
    int n, i, j, temp;
    int a[50];
    int total = 0;
    float avg;

    clrscr();

    printf("Enter number of files: ");
    scanf("%d", &n);

    printf("Enter the lengths of files:\n");
    for(i = 0; i < n; i++)
    {
        printf("File %d: ", i + 1);
        scanf("%d", &a[i]);
    }

    /* Sort files in ascending order */
    for(i = 0; i < n - 1; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            if(a[i] > a[j])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

    /* Calculate total retrieval time */
    total = 0;
    for(i = 0; i < n; i++)
    {
        for(j = 0; j <= i; j++)
        {
            total = total + a[j];
        }
    }

    avg = (float)total / n;

    printf("\nOptimal order of files:\n");
    for(i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }

    printf("\n\nTotal Retrieval Time = %d", total);
    printf("\nAverage Retrieval Time = %.2f", avg);

    getch();
}
