class NumberStorage:
    def __init__(self):
        self.numbers = []
    
    def insert_number(self, number):
        self.numbers.append(number)
    
    def search_number(self, x):
        try:
            return self.numbers.index(x) + 1  # Convert to 1-based index
        except ValueError:
            return -1
