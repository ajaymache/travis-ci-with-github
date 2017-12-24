class arithmetic:
    
    def __init__(self):
        pass
        
    def add(self, x: int, y: int) -> int:
        self.x = x
        self.y = y
        return x + y
    
    
temp = arithmetic()

print(temp.add(2, 4))