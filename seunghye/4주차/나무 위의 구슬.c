#pragma warning (disable : 4996)
#include <stdio.h>
#include <stdlib.h>

typedef struct tree {
    int num;
    struct tree* up;
    struct tree* vp;
} tree;

int main() {
    int n, u, v; //u 왼, v 오
    long long k;  //int -> 틀렸습니다
    tree* treenode = NULL;
    int nodenum = 1;

    scanf("%d", &n);
    treenode = (tree*)malloc(sizeof(tree) * (n + 1));
    for (int i = 1; i <= n; i++) {
        scanf("%d %d", &u, &v);
        if (u == -1) treenode[i].up = NULL;
        else treenode[i].up = &treenode[u];
        if (v == -1) treenode[i].vp = NULL;
        else treenode[i].vp = &treenode[v];
        treenode[i].num = i;
    }

    scanf("%lld", &k);
    while (1) {
        if (treenode[nodenum].up == NULL && treenode[nodenum].vp == NULL)
            break;
        else if (treenode[nodenum].up == NULL)
            nodenum = treenode[nodenum].vp->num;
        else if (treenode[nodenum].vp == NULL)
            nodenum = treenode[nodenum].up->num;
        else if (k % 2 == 1) {  //홀수 : 2*x+1 에서 x+1의 홀/짝
            nodenum = treenode[nodenum].up->num;
            k = k / 2 + 1;
        }
        else {  //짝수 : 2*x 에서 x의 홀/짝
            nodenum = treenode[nodenum].vp->num;
            k = k / 2;
        }
    }
    printf("%d", nodenum);
 
    return 0;
}
