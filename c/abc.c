#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *p, const void *q) {
    // From https://en.wikipedia.org/wiki/Qsort
    int x = *(const int *)p;
    int y = *(const int *)q;

    if (x < y)
        return -1;  // Return -1 if you want ascending, 1 if you want descending order.
    else if (x > y)
        return 1;   // Return 1 if you want ascending, -1 if you want descending order.

    return 0;
}

int lookup(char input){
    // This will return 2 on invalid input.  Not ideal, but we don't seem to get that kind of invalid data
    if ('A' == input){
        fprintf(stderr, "It's an A\n");
        return 0;
    } else if ('B' == input){
    fprintf(stderr, "It's a B\n");
        return 1;
    };
    fprintf(stderr, "Have to assume C\n");
    return 2;
}

int main(void){
    char desired_order[3];
    int input[4];

    // Read in the test case
    if (scanf("%d %d %d\n", &input[0], &input[1], &input[2]) != 3){
        fprintf(stderr, "Failed to read initial input\n");
        return 1;
    };
    fprintf(stderr, "%d %d %d\n", input[0], input[1], input[2]);

    // Use qsort from stdlib
    qsort(input, 3, sizeof(*input), compare_ints);
    fprintf(stderr, "%d %d %d\n", input[0], input[1], input[2]);

    if (scanf("%3s\n", desired_order) != 1){
        fprintf(stderr, "Failed to read initial input\n");
        return 1;
    };
    fprintf(stderr, "Desired order: %s\n", desired_order);
    printf("%d %d %d\n", input[lookup(desired_order[0])], input[lookup(desired_order[1])], input[lookup(desired_order[2])]);
    return 0;
}
