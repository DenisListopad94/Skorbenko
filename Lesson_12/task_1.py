class ChessPiece:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def attack(self, x, y):
        pass


class Queen(ChessPiece):
    def attack(self, x, y):
        if abs(self.x - x) == abs(self.y - y) or self.x == x or self.y == y:
            return True
        return False


class Pawn(ChessPiece):
    def attack(self, x, y):
        if self.color == "белые" and x == self.x + 1 and (y == self.y + 1 or y == self.y - 1):
            return True

        elif self.color == "черные" and x == self.x - 1 and (y == self.y + 1 or y == self.y - 1):
            return True
        return False


class Horse(ChessPiece):
    def attack(self, x, y):
        if abs(self.x - x) == 2 and abs(self.y - y) == 1 or abs(self.x - x) == 1 and abs(self.y - y) == 2:
            return True
        return False


queen = Queen(4, 4, "белые")
print(queen.attack(6, 6))  # True

pawn = Pawn(2, 2, "черные")
print(pawn.attack(3, 3))  # False

horse = Horse(1, 1, "белые")
print(horse.attack(3, 2))  # True
