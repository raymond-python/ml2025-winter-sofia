import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of (x, y) points: "))
    
    #Initialize NumPy arrays for ground truth (X) and predictions (Y)
    X = np.zeros(N, dtype=int) 
    Y = np.zeros(N, dtype=int) 

    
    print("\nEnter the values for X (ground truth) and Y (predicted):")
    for i in range(N):
        x, y = map(int, input(f"Point {i+1}: ").split())
        if x not in [0, 1] or y not in [0, 1]:
            print("Invalid input! X and Y must be 0 or 1.")
            return
        
        X[i] = x
        Y[i] = y

    #Compute Precision & Recall using Scikit-learn
    precision = precision_score(X, Y, zero_division=0)
    recall = recall_score(X, Y, zero_division=0)

    print("\nResults:")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
