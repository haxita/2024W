class Vector:
    def __init__(self, components: list[float]):
        if not all(isinstance(x, (int, float)) for x in components):
            raise TypeError("All components must be numbers (int or float).")
        self.components = tuple(components)
    
    def __repr__(self):
        return f"Vector({self.components})"
    
    def __str__(self):
        return f"<{', '.join(str(x) for x in self.components)}>"
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.components == other.components
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            return NotImplemented
        summed_components = [a + b for a, b in zip(self.components, other.components)]
        return Vector(summed_components)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            return NotImplemented
        subtracted_components = [a - b for a, b in zip(self.components, other.components)]
        return Vector(subtracted_components)
    
    def __neg__(self):
        negated_components = [-x for x in self.components]
        return Vector(negated_components)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        multiplied_components = [x * scalar for x in self.components]
        return Vector(multiplied_components)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __len__(self):
        return len(self.components)
    
    def __getitem__(self, index):
        return self.components[index]
    
    def __iter__(self):
        return iter(self.components)