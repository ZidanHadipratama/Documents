#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM 45

long long fib(int n) {
    if (n <= 1)
        return n;
    else
        return(fib(n-1) + fib(n-2));
}

int main() {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    for (int i = 0; i < NUM; i++) {
        printf("%lld\n", fib(i));
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Time spent: %f\n", cpu_time_used);

    return 0;
}
