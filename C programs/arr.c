#include <stdio.h>
int main(int argc, char const *argv[])
{
    int arr[3][3];
    int i, j, k;
    for (i = 0, k = 1; i < 3; i++)
    {
        for (j = 0; j < 3; j++, k++)
        {
            arr[i][j] = k;
        }
    }
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("%d ", *(*(arr + i) + j));
        }
        printf("\n");
    }
    return 0;
}
