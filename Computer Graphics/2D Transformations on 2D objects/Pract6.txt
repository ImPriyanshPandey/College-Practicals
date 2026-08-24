#include <stdio.h>
#include <math.h>

#define MAX_VERTICES 20

/* Correct Matrix Multiplication for 3×3 and 3×N matrices */
void multiplyMatrix(float A[3][3], float B[3][MAX_VERTICES],
                    float Result[3][MAX_VERTICES],
                    int rowsA, int colsA, int colsB)
{
    int i, j, k;
    for (i = 0; i < rowsA; i++) {
        for (j = 0; j < colsB; j++) {
            Result[i][j] = 0;
            for (k = 0; k < colsA; k++) {
                Result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int n, i, choice;
    float polygon[3][MAX_VERTICES];  
    float transMat[3][3], result[3][MAX_VERTICES];
    float angle, tx, ty, sx, sy;

    printf("Enter number of vertices of polygon: ");
    scanf("%d", &n);

    printf("Enter vertices (x y):\n");
    for (i = 0; i < n; i++) {
        scanf("%f %f", &polygon[0][i], &polygon[1][i]);
        polygon[2][i] = 1;    // Homogeneous coordinate
    }

    do {
        printf("\n--- 2D Transformation Menu ---\n");
        printf("1. Translation\n");
        printf("2. Scaling\n");
        printf("3. Rotation\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {

        case 1:  // Translation
            printf("Enter translation factors (tx ty): ");
            scanf("%f %f", &tx, &ty);

            transMat[0][0] = 1; transMat[0][1] = 0; transMat[0][2] = tx;
            transMat[1][0] = 0; transMat[1][1] = 1; transMat[1][2] = ty;
            transMat[2][0] = 0; transMat[2][1] = 0; transMat[2][2] = 1;

            multiplyMatrix(transMat, polygon, result, 3, 3, n);
            break;

        case 2:  // Scaling
            printf("Enter scaling factors (sx sy): ");
            scanf("%f %f", &sx, &sy);

            transMat[0][0] = sx; transMat[0][1] = 0;  transMat[0][2] = 0;
            transMat[1][0] = 0;  transMat[1][1] = sy; transMat[1][2] = 0;
            transMat[2][0] = 0;  transMat[2][1] = 0;  transMat[2][2] = 1;

            multiplyMatrix(transMat, polygon, result, 3, 3, n);
            break;

        case 3:  // Rotation
            printf("Enter rotation angle (in degrees): ");
            scanf("%f", &angle);

            angle = angle * M_PI / 180.0;  // Convert degrees to radians

            transMat[0][0] = cos(angle);  transMat[0][1] = -sin(angle); transMat[0][2] = 0;
            transMat[1][0] = sin(angle);  transMat[1][1] = cos(angle);  transMat[1][2] = 0;
            transMat[2][0] = 0;           transMat[2][1] = 0;           transMat[2][2] = 1;

            multiplyMatrix(transMat, polygon, result, 3, 3, n);
            break;

        case 4:
            printf("Exiting...\n");
            return 0;

        default:
            printf("Invalid choice! Try again.\n");
            continue;
        }

        // Apply transformed results
        printf("\nTransformed Coordinates:\n");
        for (i = 0; i < n; i++) {
            printf("(%.2f, %.2f)\n", result[0][i], result[1][i]);
            polygon[0][i] = result[0][i];
            polygon[1][i] = result[1][i];
            polygon[2][i] = 1; // Keep homogeneous coordinate fixed
        }

    } while (choice != 4);

    return 0;
}
