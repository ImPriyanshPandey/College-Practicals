#include <stdio.h>
#include <math.h>

void hermite(double p0[2], double p1[2], double r0[2], double r1[2], int steps) {
    printf("Cubic Hermite Curve Points:\n");
    for (int i = 0; i <= steps; i++) {
        double t = (double)i / steps;
        double t2 = t * t;
        double t3 = t2 * t;

        double h1 = 2 * t3 - 3 * t2 + 1;
        double h2 = -2 * t3 + 3 * t2;
        double h3 = t3 - 2 * t2 + t;
        double h4 = t3 - t2;

        double x =h1*p0[0] + h2*p1[0] + h3*r0[0] + h4*r1[0];
        double y =h1*p0[1] + h2*p1[1] + h3*r0[1] + h4*r1[1];

        printf("t=%.2f -> (%.3f, %.3f)\n", t, x, y);
    }
    printf("\n");
}

void bezier(double b0[2], double b1[2], double b2[2], double b3[2], int steps) {
    printf("Cubic Bezier Curve Points:\n");
    for (int i = 0; i <= steps; i++) {
        double t = (double)i / steps;
        double u = 1 - t;

        double b0c = u * u * u;
        double b1c = 3 * u * u * t;
        double b2c = 3 * u * t * t;
        double b3c = t * t * t;

        double x = b0c * b0[0] + b1c * b1[0] + b2c * b2[0] + b3c * b3[0];
        double y = b0c * b0[1] + b1c * b1[1] + b2c * b2[1] + b3c * b3[1];

        printf("t=%.2f -> (%.3f, %.3f)\n", t, x, y);
    }
    printf("\n");
}

int main() {
    double p0[2] = {0.0, 0.0};
    double p1[2] = {1.0, 1.0};
    double r0[2] = {1.0, 0.0};      // tangent at p0
    double r1[2] = {1.0, 0.0};      // tangent at p1

    double b0[2] = {0.0, 0.0};
    double b1[2] = {0.3, 1.2};
    double b2[2] = {0.7, -0.2};
    double b3[2] = {1.0, 1.0};

    int steps = 10;

    hermite(p0, p1, r0, r1, steps);
    bezier(b0, b1, b2, b3, steps);

    return 0;
}