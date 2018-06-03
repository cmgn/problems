#include <stdio.h>

int r, c;
int g[1001][1001];
int f[1001][1001];


void fill(int i, int j, int colour, int root)
{
    if (i < 0 || j < 0 || i >= r || j >= c) {
        return;
    } else if (f[i][j] || g[i][j] != root) {
        return;
    }

    f[i][j] = colour;

    fill(i+1, j, colour, root);
    fill(i-1, j, colour, root);
    fill(i, j+1, colour, root);
    fill(i, j-1, colour, root);   
}


int main()
{
    scanf("%d %d", &r, &c);
    char buffer[1001];
    for (int i = 0; i < r; i++) {
        scanf("%s", buffer);
        for (char *p = buffer; *p; p++) {
            g[i][p-buffer] = *p - '0';
        }
    }
    int colour = 1;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            fill(i, j, colour++, g[i][j]);
        }
    }
    int q, r1, c1, r2, c2, can_move;
    scanf("%d", &q);
    while (q--) {
        scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
        r1--; c1--; r2--; c2--;
        can_move = f[r1][c1] == f[r2][c2];
        if (can_move && g[r1][c1]) {
            printf("decimal\n");
        } else if (can_move) {
            printf("binary\n");
        } else {
            printf("neither\n");
        }
    }
    return 0;
}
