#include <stdio.h>
#include <stdlib.h>

typedef struct { int x, y; } Point;

/* Bresenham algorithm that returns an array of points.
 * The function allocates an array of Points and sets *count to number of points.
 * Caller must free the returned pointer.
 */
Point* bresenham_line(int x0, int y0, int x1, int y1, int *count) {
    int steep = abs(y1 - y0) > abs(x1 - x0);

    // If the line is steep, we transpose the coordinates (swap x and y)
    if (steep) {
        int tmp;
        tmp = x0; x0 = y0; y0 = tmp;
        tmp = x1; x1 = y1; y1 = tmp;
    }

    // Ensure left-to-right iteration (x0 <= x1)
    if (x0 > x1) {
        int tmp;
        tmp = x0; x0 = x1; x1 = tmp;
        tmp = y0; y0 = y1; y1 = tmp;
    }

    int dx = x1 - x0;
    int dy = abs(y1 - y0);
    int error = dx / 2;
    int ystep = (y0 < y1) ? 1 : -1;
    int y = y0;

    // Upper bound for number of points is dx+1
    Point *points = (Point*) malloc((dx + 1) * sizeof(Point));
    if (!points) {
        fprintf(stderr, "Memory allocation failed\n");
        *count = 0;
        return NULL;
    }

    int idx = 0;
    for (int x = x0; x <= x1; x++) {
        if (steep) {
            points[idx].x = y;  // transpose back
            points[idx].y = x;
        } else {
            points[idx].x = x;
            points[idx].y = y;
        }
        idx++;

        error -= dy;
        if (error < 0) {
            y += ystep;
            error += dx;
        }
    }

    *count = idx;
    return points;
}

/* ASCII preview printer:
 * Creates a small grid covering the bounding box of the points and prints
 * '#' for line pixels and '.' for empty pixels.
 * If the grid is too large (> 80x40), it refuses to print to avoid huge output.
 */
void ascii_preview(Point *pts, int n) {
    if (n <= 0) return;

    int minx = pts[0].x, maxx = pts[0].x;
    int miny = pts[0].y, maxy = pts[0].y;
    for (int i = 1; i < n; i++) {
        if (pts[i].x < minx) minx = pts[i].x;
        if (pts[i].x > maxx) maxx = pts[i].x;
        if (pts[i].y < miny) miny = pts[i].y;
        if (pts[i].y > maxy) maxy = pts[i].y;
    }

    int width = maxx - minx + 1;
    int height = maxy - miny + 1;

    // Avoid huge previews
    const int MAX_W = 80, MAX_H = 40;
    if (width > MAX_W || height > MAX_H) {
        printf("\nASCII preview skipped (grid %d x %d is too large)\n", width, height);
        return;
    }

    // Allocate grid and fill with dots
    char **grid = (char**) malloc(height * sizeof(char*));
    for (int r = 0; r < height; r++) {
        grid[r] = (char*) malloc((width + 1) * sizeof(char));
        for (int c = 0; c < width; c++) grid[r][c] = '.';
        grid[r][width] = '\0';
    }

    // Mark points (note: we flip y for printing so higher y prints on top)
    for (int i = 0; i < n; i++) {
        int gx = pts[i].x - minx;
        int gy = pts[i].y - miny;
        // In ASCII row index, 0 is top -> invert y
        int row = height - 1 - gy;
        int col = gx;
        if (row >= 0 && row < height && col >= 0 && col < width)
            grid[row][col] = '#';
    }

    printf("\nASCII preview (X from %d to %d, Y from %d to %d):\n\n", minx, maxx, miny, maxy);
    for (int r = 0; r < height; r++) {
        printf("%s\n", grid[r]);
        free(grid[r]);
    }
    free(grid);
}

int main(void) {
    int x0, y0, x1, y1;
    printf("Enter x0 y0 x1 y1 (integer coordinates), separated by spaces:\n");
    if (scanf("%d %d %d %d", &x0, &y0, &x1, &y1) != 4) {
        fprintf(stderr, "Invalid input. Expected four integers.\n");
        return 1;
    }

    int count = 0;
    Point *pts = bresenham_line(x0, y0, x1, y1, &count);
    if (!pts || count == 0) {
        printf("No points generated.\n");
        free(pts);
        return 1;
    }

    printf("\nGenerated %d points (x, y):\n", count);
    for (int i = 0; i < count; i++) {
        printf("(%d, %d)\n", pts[i].x, pts[i].y);
    }

    // Show ASCII preview if grid small enough
    ascii_preview(pts, count);

    free(pts);
    return 0;
}
