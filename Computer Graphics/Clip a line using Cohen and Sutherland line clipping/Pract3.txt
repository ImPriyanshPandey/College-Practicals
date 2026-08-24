#include <stdio.h>

/* Define region codes */
#define INSIDE 0 // 0000
#define LEFT 1   // 0001
#define RIGHT 2  // 0010
#define BOTTOM 4 // 0100
#define TOP 8    // 1000

/* Clipping window boundaries */
double x_min, y_min, x_max, y_max;

/* Function to compute region codes */
int computeCode(double x, double y) {
    int code = INSIDE;

    if (x < x_min)       // to the left of clip window
        code |= LEFT;
    else if (x > x_max)  // to the right of clip window
        code |= RIGHT;
    if (y < y_min)       // below the clip window
        code |= BOTTOM;
    else if (y > y_max)  // above the clip window
        code |= TOP;

    return code;
}

/* Cohen-Sutherland clipping algorithm */
void cohenSutherlandClip(double x1, double y1, double x2, double y2) {
    int code1 = computeCode(x1, y1);
    int code2 = computeCode(x2, y2);
    int accept = 0;

    while (1) {
        if ((code1 == 0) && (code2 == 0)) {
            // Both points inside
            accept = 1;
            break;
        } 
        else if (code1 & code2) {
            // Both points outside -> reject
            break;
        } 
        else {
            // At least one point outside
            int code_out;
            double x, y;

            // Choose one end point
            code_out = code1 ? code1 : code2;

            // Find intersection point
            if (code_out & TOP) {
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1);
                y = y_max;
            } 
            else if (code_out & BOTTOM) {
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1);
                y = y_min;
            } 
            else if (code_out & RIGHT) {
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1);
                x = x_max;
            } 
            else if (code_out & LEFT) {
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1);
                x = x_min;
            }

            // Replace outside point with intersection point
            if (code_out == code1) {
                x1 = x;
                y1 = y;
                code1 = computeCode(x1, y1);
            } 
            else {
                x2 = x;
                y2 = y;
                code2 = computeCode(x2, y2);
            }
        }
    }

    if (accept) {
        printf("Line accepted from (%.2f, %.2f) to (%.2f, %.2f)\n", x1, y1, x2, y2);
    } 
    else {
        printf("Line rejected\n");
    }
}

int main() {
    double x1, y1, x2, y2;

    printf("Enter clipping window (x_min y_min x_max y_max): ");
    scanf("%lf %lf %lf %lf", &x_min, &y_min, &x_max, &y_max);

    printf("Enter line coordinates (x1 y1 x2 y2): ");
    scanf("%lf %lf %lf %lf", &x1, &y1, &x2, &y2);

    cohenSutherlandClip(x1, y1, x2, y2);

    return 0;
}