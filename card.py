from enum import auto, IntEnum


class CardColor(IntEnum):
    """
    Enum class for the color of the card
    """
    RED = 0
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    CRAZY = auto()


class CardLabel(IntEnum):
    """
    Enum class for the value of the card
    """
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    CRAZY = auto()
    DRAW_FOUR = auto()

class Card:
    def __init__(self, color: CardColor, label: CardLabel) -> None:
        """
        Constructor for the Card class

        Args:
            color (CardColor): The color of the card
            label (CardLabel): The label of the card

        Returns:
            None

        Complexity:
            Best Case Complexity:   O(1)
            Worst Case Complexity:  O(1)
        """
        self.color = color
        self.label = label
    
    def __str__(self):
        return f"Card color: {self.color.name}, Card label: {self.label.name}"
    
    def __gt__(self,other) -> bool:
        if self.color > other.color:
            return True
        elif self.color == other.color:
            return self.label > other.label
        else:
            return False
        
    def __lt__(self, other) -> bool:
        if self.color < other.color:
            return True
        elif self.color == other.color:
            return self.label < other.label
        else:
            return False
        
    def __ge__(self, other) -> bool:
        return self < other or self == other
    
    def __le__(self,other) -> bool:
        if self.color == other.color:
            return self.label <= other.label
        return self.color <= other.color
    
    def __eq__(self,other) -> bool:
        if isinstance(other, Card):
            return self.color == other.color and self.label == other.label
        return False