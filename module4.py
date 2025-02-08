N = int(input("Enter how many numbers:"))  
numbers = [int(input("Enter number:")) for _ in range(N)]  
X = int(input("Enter checking possible number:"))  
print(numbers.index(X) + 1 if X in numbers else -1)
