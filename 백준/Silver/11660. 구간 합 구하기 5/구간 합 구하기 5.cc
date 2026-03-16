#include <stdio.h>

int main() {
    int N, M;
    int arr[1025][1025] = {0};
    int sum_arr[1025][1025] = {0};

    scanf("%d %d", &N, &M);

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            scanf("%d", &arr[i][j]);
        }
    }
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            sum_arr[i][j] = arr[i][j] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1];
        }
    }

    // printf("< sum_arr >\n");
    //
    // for (int i=1; i<=N; i++) {
    //     for (int j=1; j<=N; j++) {
    //         printf("%d ", sum_arr[i][j]);
    //     }
    //     printf("\n");
    // }
    for (int i=1; i<=M; i++) {
        int x[2], y[2];
        int result;
        scanf("%d %d %d %d", &y[0], &x[0], &y[1], &x[1]);

        if (x[0] == x[1] && y[0] == y[1]) {
            result = arr[y[0]][x[0]];
        }
        else {
            result = sum_arr[y[1]][x[1]] - sum_arr[y[0]-1][x[1]] - sum_arr[y[1]][x[0] - 1] + sum_arr[y[0]-1][x[0] - 1];
        }
        printf("%d\n", result);
    }

}

/*
 * 2: (1, 2) -> (4, 3)
 * 3: (1, 3) -> (4, 2)
 * 4: (2, 3) -> (3, 2)
 * next_loc = N+1 - pre_loc
 */