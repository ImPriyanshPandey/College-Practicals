#include<stdio.h>

#define MAX_VERTICES 20

typedef struct {
    int x, y;
}Point ;

/* Function to swap two integers */
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* Scanline polygon fill algorithm */
void scanlineFill(Point polygon[], int n){
    int i, j, k, temp;
    int y, ymax, ymin;
    y, ymax = polygon[0].y, y, ymin = polygon[0].y;
    int xIntersect[MAX_VERTICES];

    /* Find ymin and ymax of polygon */
    for (i=1; i<n; i++) {
        if (polygon[i].y > ymax) ymax = polygon[i].y;
        if (polygon[i].y < ymin) ymin = polygon[i].y;
    }

    /* Scanline from bottom to top */
    for (y = ymin; y <= ymax; y++) {
        int count = 0; 
        
        /* Find intersections of scanline with polygon edges */
        for (i = 0; i < n; i++){
            j = (i + 1) % n; 
            if((polygon[i].y <= y && polygon[j].y > y)
               || (polygon[j].y <= y && polygon[i].y > y)) {
                /* Calculate intersection X */
                xIntersect[count++] = polygon[i].x + 
                    (y - polygon[i].y) * (polygon[j].x - polygon[i].x) / 
                    (polygon[j].y - polygon[i].y);
            }
        }

        /* Sort the intersections */
        for (i = 0; i < count - 1; i++) {
            for (j = i +1; j < count; j++) {
                if (xIntersect[i] > xIntersect[j]) {
                    swap(&xIntersect[i], &xIntersect[j]);
                }
            }
        }

        /* Fill between pairs of intersections */
        for (i = 0; i < count; i += 2) {
            if (i + 1 < count) {
                printf(" Scanline Y=%d: Fill from X=%d to X=%d\n", 
                    y, xIntersect[i], xIntersect[i + 1]);
            }
        }
    }

}
int main() {
    int n, i;
    Point polygon[MAX_VERTICES];

    printf("Enter number of vertices of polygon : ");
    scanf("%d", &n);

    printf("Enter polygon vertices (x y) : \n");
    for (i = 0; i < n; i++) {
        scanf("%d %d", &polygon[i].x, &polygon[i].y);
    }

    printf("\nScanline filling steps :\n");
    scanlineFill(polygon, n);

    return 0;
}   