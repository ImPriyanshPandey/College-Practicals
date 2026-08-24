#include <stdio.h>
#include <math.h>

#define SIZE 4 // For Homogenous 4x4 transformation matrices

// Fuction to multiply 4x4 matrix with a point (vector)
void multiplyMatrixVector(float mat[SIZE][SIZE], float point[4], float result[4]) {
    for (int i = 0; i < SIZE; i++) {
        result[i] = 0;
        for (int j = 0; j < SIZE; j++) {
            result[i] += mat[i][j] * point[j];
        }
    }
}

// Function to print coordinates
void printPoint(char *label, float point[4]) {
    printf("%s (X: %.2f, Y: %.2f, Z: %.2f)\n", label, point[0], point[1], point[2]);
}

int main() {
    float point[4], transformed[4], scaled[4], rotated[4];
    float tx, ty, tz, sx, sy, sz, angle;

    // Input original Point
    printf("Enter coordinates of the 3D point (X Y Z): ");
    scanf("%f %f %f", &point[0], &point[1], &point[2]);
    point[3] = 1; // Homogeneous coordinate

    // Translation values
    printf("Enter translation values (tx ty tz): ");
    scanf("%f %f %f", &tx, &ty, &tz);

    // Scaling Factors
    printf("Enter scaling factors (sx sy sz): ");
    scanf("%f %f %f", &sx, &sy, &sz);

    // Rotation angle araound Z-axis
    printf("Enter rotation angle around Z-axis (in degrees): ");
    scanf("%f", &angle);
    float rad = angle * (M_PI / 180.0); 

    // Translation Matrix
    float translationMatrix[SIZE][SIZE] = {
        {1, 0, 0, tx},
        {0, 1, 0, ty},
        {0, 0, 1, tz},
        {0, 0, 0, 1}
    };

    // Scaling Matrix
    float scalingMatrix[SIZE][SIZE] = {
        {sx, 0, 0, 0},
        {0, sy, 0, 0},
        {0, 0, sz, 0},
        {0, 0, 0, 1}
    };

    // Rotation Matrix around Z-axis
    float rotationMatrix[SIZE][SIZE] = {
        {cos(rad), -sin(rad), 0, 0},
        {sin(rad),  cos(rad), 0, 0},
        {0,         0,        1, 0},
        {0,         0,        0, 1}
    };

    // Step 1: Translation 
    multiplyMatrixVector(translationMatrix, point, transformed);
    printPoint("\nAfter Translation", transformed);

    // Step 2: Scaling
    multiplyMatrixVector(scalingMatrix, transformed, scaled);
    printPoint("After Scaling", scaled);

    // Step 3: Rotation
    multiplyMatrixVector(rotationMatrix, transformed, rotated);
    printPoint("After Rotation", rotated);

    //===============================================
    //      Projection Matrices
    //===============================================

    // Parallel Projection Matrix (Z ignored)
    float parallelProj[SIZE][SIZE] = {
        {1, 0, 0, 0},
        {0, 1, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 1}
    };

    // Perspective Projection Matrix
    float d;
    printf("\n\nEnter distance for perspective projection (d): ");
    scanf("%f", &d);

    float perspectiveProj[SIZE][SIZE] = {
        {1, 0, 0, 0},
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {0, 0, 1/d, 0}
    };

    // Apply Parallel Projection
    float parallel[4];
    multiplyMatrixVector(parallelProj, rotated, parallel);
    printPoint("\nParallel Projection", parallel);

    // Apply Perspective Projection
    float perspective[4];
    multiplyMatrixVector(perspectiveProj, rotated, perspective);

    // Normalize (divide by w)
    if (perspective[3] != 0) {
        perspective[0] /= perspective[3];
        perspective[1] /= perspective[3];
        perspective[2] /= perspective[3];
        perspective[3] = 1;
    }
    printPoint("Perspective Projection", perspective);

    return 0;
}