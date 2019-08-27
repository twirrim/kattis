#include <stdio.h>

int main(void){
    int k, n;
    int _ignore;
    if (scanf("%d\n", &_ignore) != 1){
        return -1;
    }
    while(scanf("%d %d\n", &k, &n) == 2){
        int s1 = (n * (n + 1))/2;
        int s3 = s1 * 2;
        int s2 = s3 - n;
        printf("%d %d %d %d\n", k, s1, s2, s3);
    };
    return 0;
};
