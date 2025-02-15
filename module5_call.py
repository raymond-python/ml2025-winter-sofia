from module5_mod import NumberStorage

def main():
    storage = NumberStorage()
    
    N = int(input("Enter the number of elements: "))
    
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        storage.insert_number(num)
    
    X = int(input("Enter the number to search: "))
    
    print(storage.search_number(X))

if __name__ == "__main__":
    main()
