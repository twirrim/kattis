/* A solution to the Take Two Stones problem on open.kattis.com */
#include <stdio.h>

int main(void){
    int stones;
    while(scanf("%d", &stones) == 1){
        if ((stones % 2) == 0){
            printf("Bob\n");
        } else {
            printf("Alice\n");
        };
    }
    return 0;
}
