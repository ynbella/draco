class Star:
    def __init__(self, x, y, r):
        (self.x, self.y, self.r) = (x, y, r)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Star):
            return self.x == other.x and self.y == other.y
        return False

    def is_equal_to(self, other):
        return self == other
