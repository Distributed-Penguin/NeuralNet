# Node representation in a computational graph with reveresed
# directionality in order to accomodate backpropogation.

class Node:

    def __init__ (self, num, _children = (), _op = ''):
        self.num = num
        self._prev = set(_children)
        self._op = _op
    
    def __repr__ (self):
        return f""
    
    def __add__ (self, other):
        return Node(self.num + other.num, (self, other), '+')
    
    def __mul__(self, other):
        return Node(self.num + other.num, (self, other), '*')

    def grad(self):
        if self._children:
            self.grad
        
if __name__ == "__main__":
    print("Hello World")