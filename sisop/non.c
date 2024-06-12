#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM 1000

long long fib(int n, long long *memo) {
    if (n <= 1)
        return n;

    // If we have already computed fib(n), return the stored result
    if (memo[n] != -1)
        return memo[n];

    // Otherwise, compute it and store the result in the memo array
    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n];
}

int main() {
    clock_t start, end;
    double cpu_time_used;

    // Allocate memory for the memo array and initialize all elements to -1
    long long *memo = malloc((NUM + 1) * sizeof(long long));
    for (int i = 0; i <= NUM; i++) {
        memo[i] = -1;
    }

    start = clock();

    for (int i = 0; i < NUM; i++) {
        printf("%lld\n", fib(i, memo));
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Time spent: %f\n", cpu_time_used);

    free(memo);
    return 0;
}
