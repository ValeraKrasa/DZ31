
class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating
    
    def __eq__(self, other) -> bool: # коли ==
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        elif isinstance(other, int):
            return self.rating == other
        else:
            return 'Не можливо порівняти'

    def __gt__(self, other) -> bool: # коли >
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        elif isinstance(other, int):
            return self.rating > other
        else:
            return 'Не можливо порівняти'

    def __lt__(self, other) -> bool: # коли <
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        elif isinstance(other, int):
            return self.rating < other
        else:
            return 'Не можливо порівняти'

magnus = ChessPlayer('Carlsen', 'Magnus', 3200)
ian = ChessPlayer('Ian', 'Xarasho', 2789)

print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # 'Не можливо порівняти'