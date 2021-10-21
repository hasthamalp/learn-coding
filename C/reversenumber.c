#include <stdio.h>
int main()
{
    int n, reverse = 0, rem;
    printf("Enter a number: ");
    scanf("%d", &n); //taking values from user
    while (n != 0)
    {
        rem = n % 10;
        reverse = reverse * 10 + rem;
        n /= 10;
    }
    printf("Reversed Number: %d", reverse); //printing the results
    return 0;
}