import numpy as np

class KNNRegressor:
    def __init__(self, k):
        """Initialize with k value and empty dataset"""
        self.k = k
        self.points = np.array([])

    def insert_point(self, x, y):
        """Insert a new (x, y) data point"""
        if self.points.size == 0:
            self.points = np.array([[x, y]])
        else:
            self.points = np.vstack((self.points, [x, y]))

    def predict(self, X):
        """Perform k-NN Regression and return the predicted Y value"""
        if self.k > len(self.points):
            return "Error: k cannot be greater than the number of data points (N)."

        # Extract x values
        x_values = self.points[:, 0]
        y_values = self.points[:, 1]
        distances = np.abs(x_values - X)

        nearest_indices = np.argsort(distances)[:self.k]

        return np.mean(y_values[nearest_indices])


def main():
    N = int(input("Enter the number of data points (N): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    k = int(input("Enter the number of nearest neighbors (k): "))
    if k <= 0:
        print("Error: k must be a positive integer.")
        return

    knn = KNNRegressor(k)

    print(f"Enter {N} data points (x y) one by one:")
    for _ in range(N):
        x, y = map(float, input().split())
        knn.insert_point(x, y)

    X = float(input("Enter the X value to predict Y: "))

    result = knn.predict(X)
    print("Predicted Y:", result)


if __name__ == "__main__":
    main()
