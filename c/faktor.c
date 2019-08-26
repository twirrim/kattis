/* A solution to the Faktor problem on Kattis */
#include <stdio.h>
int main(void){
    float articles, impact;
    while(scanf("%f %f", &articles, &impact) == 2){
        // Because we're rounding down, we can just decrement the target, multiply the first by it and add the 1 back in again
        impact--;
        float result = (articles * impact) + 1;
        printf("%d", (int)result);
    }
}
