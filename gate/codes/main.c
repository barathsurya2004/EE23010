#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main() {
    double lambda = 8; // Change lambda to your desired mean

    int n = 100000; // Number of simulations
    int validCount = 0; // Count of valid X values (X > 0)
    double sumY = 0.0; // Sum of 1 / (X + 1)

    srand(time(0)); // Seed the random number generator

    for (int i = 0; i < n; i++) {
        int X = 0;
        double p = exp(-lambda);
        double F = p;

        double U = (double)rand() / RAND_MAX;

        while (U > F) {
            p *= lambda / (X + 1);
            F += p;
            X++;
        }

        if (X > 0) {
            double Y = 1.0 / (X + 1);
            sumY += Y;
            validCount++;
        }
    }

    if (validCount > 0) {
        double conditionalExpectation = sumY / validCount;
        printf("Simulated E(1 / (X + 1) | X > 0): %lf\n", conditionalExpectation);
    } else {
        printf("No valid X values (X > 0) were generated.\n");
    }

    double formulaans = (1 - exp(-lambda) - lambda * exp(-lambda)) / (lambda * (1 - exp(-lambda)));
    printf("Formula-based answer: %lf\n", formulaans);

    return 0;
}