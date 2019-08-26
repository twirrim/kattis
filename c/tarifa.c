#include <stdio.h>

int main(void){
    int megabyte_limit;
    int month_count;
    int data_used;

    int remaining = 0;
    if (scanf("%d\n", &megabyte_limit) == 1){
        if (scanf("%d\n", &month_count) == 1){
            for (int i = 0; i < month_count; i++){
                if (scanf("%d\n", &data_used) == 1){
                    remaining = remaining + (megabyte_limit - data_used);
                } else {
                    printf("Failed to read data for month\n");
                    return 1;
                }
            }
        } else {
            printf("Failed to read a month count\n");
            return 1;
        };
    } else {
        printf("Failed to read a megabyte limit in the first line\n");
        return 1;
    }
    printf("%d\n", remaining + megabyte_limit);
    return 0;
}
