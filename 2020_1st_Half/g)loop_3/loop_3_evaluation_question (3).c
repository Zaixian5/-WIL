#include <stdio.h>

int main()
{
    int n;
    int i, j;

    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=n*2-1;j>i*2-1;j--){
            printf(" ");
        }
        for(j=1;j<=i*2-1;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
