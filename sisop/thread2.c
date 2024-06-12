#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define NUM 45

typedef struct {
    int n;
    long long result;
} FibArgs;

void *fib(void *args) {
    FibArgs *fibArgs = (FibArgs *)args;
    int n = fibArgs->n;
    if (n <= 1)
        fibArgs->result = n;
    else {
        long long prev1 = 0, prev2 = 1;
        for (int i = 2; i <= n; i++) {
            fibArgs->result = prev1 + prev2;
            prev1 = prev2;
            prev2 = fibArgs->result;
        }
    }
    return NULL;
}

int main() {
    pthread_t threads[NUM];
    FibArgs args[NUM];

    clock_t start, end;
    double cpu_time_used;

    start = clock();

    for (int i = 0; i < NUM; i++) {
        args[i].n = i;
        pthread_create(&threads[i], NULL, fib, &args[i]);
    }

    for (int i = 0; i < NUM; i++) {
        pthread_join(threads[i], NULL);
        printf("%lld\n", args[i].result);
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Time spent: %f\n", cpu_time_used);

    return 0;
}
