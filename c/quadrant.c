/* A solution to the Quadrant Selection problem on Kattis */
#include <stdio.h>

int main(void){
    int x, y;
    while(scanf("%d\n%d", &x, &y) == 2)
    if (x < 0){
        if (y > 0){
            printf("2\n");
        } else {
            printf("3\n");
        }
    } else {
        if (y > 0){
            printf("1\n");
        } else {
            printf("4\n");
        }
    };
}
