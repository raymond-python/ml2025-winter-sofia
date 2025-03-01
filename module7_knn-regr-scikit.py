import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegression:
    def __init__(self, k):
        """Initialize k-NN regressor with k neighbors."""
        self.k = k
        self.x_train = np.array([])  # Will store x values
        self.y_train = np.array([])  # Will store y values

    def insert_point(self, x, y):
        """Insert a new (x, y) data point."""
        if self.x_train.size == 0:
            self.x_train = np.array([x])
            self.y_train = np.array([y])
        else:
            self.x_train = np.append(self.x_train, x)
            self.y_train = np.append(self.y_train, y)

    def compute_variance(self):
        """Compute variance of y values."""
        return np.var(self.y_train)

    def predict(self, X):
        """Perform k-NN Regression and return the predicted Y value using Scikit-learn."""
        if self.k > len(self.x_train):
            return "Error: k cannot be greater than the number of data points (N)."

        # Reshape data for scikit-learn
        x_train_reshaped = self.x_train.reshape(-1, 1)
        X = np.array([[X]])

        # Train k-NN Regressor
        knn = KNeighborsRegressor(n_neighbors=self.k, metric='euclidean')
        knn.fit(x_train_reshaped, self.y_train)

        # Predict the value
        return knn.predict(X)[0]


# Main function to run the program
def main():
    # Read input N
    N = int(input("Enter the number of data points (N): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    # Read input k
    k = int(input("Enter the number of nearest neighbors (k): "))
    if k <= 0:
        print("Error: k must be a positive integer.")
        return

    # Create k-NN Regressor
    knn = KNNRegression(k)

    # Read N (x, y) points
    print(f"Enter {N} data points (x y) one by one:")
    for _ in range(N):
        x, y = map(float, input().split())
        knn.insert_point(x, y)

    # Compute variance of labels
    variance = knn.compute_variance()
    print(f"Variance of training labels: {variance:.4f}")

    # Read input X
    X = float(input("Enter the X value to predict Y: "))

    # Get prediction
    result = knn.predict(X)
    print("Predicted Y:", result)


# Run the program
if __name__ == "__main__":
    main()
