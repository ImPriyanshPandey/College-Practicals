#include <stdio.h>

#define MAX_POINTS 100

// Clipping window boundaries
float x_min , y_min , x_max , y_max ;

typedef struct {
    float x;
    float y;
} Point;

// Check if point is inside boundary
int inside(Point p, int edge) {
    switch(edge) {
        case 0: return p.x >= x_min; // Left
        case 1: return p.x <= x_max; // Right
        case 2: return p.y >= y_min; // Bottom
        case 3: return p.y <= y_max; // Top
    }
    return 0;
}

// Find intersection point of polygon edge with clipping boundary
Point intersection(Point p1, Point p2, int edge) {
    Point i;
    float m = (p2.y - p1.y) / (p2.x - p1.x);

    switch(edge) {
        case 0: //left
            i.x = x_min;
            i.y = p1.y + m * (x_min - p1.x);
            break;
        case 1: //right
            i.x = x_max;
            i.y = p1.y + m * (x_max - p1.x);
            break;
        case 2: //bottom
            i.y = y_min;    
            if (p2.x != p1.x)
                i.x = p1.x + (y_min - p1.y) / m;
            else
                i.x = p1.x;
            break;
        case 3: //top
            i.y = y_max;
            if (p2.x != p1.x)
                i.x = p1.x + (y_max - p1.y) / m;
            else
                i.x = p1.x;
            break;
    }
    return i;
}

// Clip polygon against one edge
int clip(Point inPoly[], int n, int edge, Point outPoly[]) {
    int outCount = 0;
    Point s = inPoly[n - 1]; //Start with the last vertex

    for (int i =0; i<n; i++) {
        Point p = inPoly[i];
        if (inside(p, edge)) {
            if (inside(s, edge))
                // Case 1: s and p inside
                outPoly[outCount++] = p;
            else {
                // Case 4: s outside, p inside
                outPoly[outCount++] = intersection(s, p, edge);
                outPoly[outCount++] = p;
            }
        }
        else{
            if (inside(s, edge)) {
                // Case 3: s inside, p outside
                outPoly[outCount++] = intersection(s, p, edge);
            }
            // Case 4: both outside -> nothing added
        }
        s = p;
    }
    return outCount;
}

int main() {
    int n;
    Point inPoly[MAX_POINTS], outPoly[MAX_POINTS];

    printf("Enter clipping window (x_min y_min x_max y_max): ");
    scanf("%f %f %f %f", &x_min, &y_min, &x_max, &y_max);

    printf("Enter number of vertices of polygon: ");
    scanf("%d", &n);

    printf("Enter the vertices (x y) :\n");
    for (int i = 0; i < n; i++) {
        scanf("%f %f", &inPoly[i].x, &inPoly[i].y);
    }

    int outCount = n;

    //Clip polygon against each edge of the clipping window
    for (int edge = 0; edge < 4; edge++) {
        outCount = clip(inPoly, outCount, edge, outPoly);

        // Prepare input for next iteration
        for (int i = 0; i < outCount; i++) {
            inPoly[i] = outPoly[i];
        }
    }

    printf("\nClipped polygon vertices:\n");
    for (int i = 0; i < outCount; i++) {
        printf("(%.2f, %.2f)\n", outPoly[i].x, outPoly[i].y);
    }
    return 0;
}