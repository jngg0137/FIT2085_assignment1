from card import Card
from constants import Constants
from data_structures.array_sorted_list import ArraySortedList

class Player:
    """
    Player class to store the player details
    """
    def __init__(self, name: str, position: int) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None

        Complexity:
            Best Case Complexity:   O(1)
            Worst Case Complexity:  O(1)
        """
        self.name = name
        self.position = position
        self.hand = ArraySortedList(Constants.NUM_CARDS_AT_INIT) #need to change to something that can be sorted

        #toString method
        def __str__(self):
            return f"Player name: {name}, Position: {position})"

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity:   
            Worst Case Complexity:  
        """
        self.hand.add(card)

    def play_card(self, index: int) -> Card:
        """
        Method to play a card from the player's hand

        Args:
            index (int): The index of the card to be played

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity:   
            Worst Case Complexity:  
        """
        return self.hand.delete_at_index(index)

    def __len__(self) -> int:
        """
        Method to get the number of cards in the player's hand

        Args:
            None

        Returns:
            int: The number of cards in the player's hand

        Complexity:
            Best Case Complexity:   O(1)
            Worst Case Complexity:  O(1)
        """
        return self.hand.length

    def __getitem__(self, index: int) -> Card:
        """
        Method to get the card at the given index from the player's hand

        Args:
            index (int): The index of the card to be fetched

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity:   O(1)
            Worst Case Complexity:  O(1)
        """
        return self.hand[index]

    # def __gt__(self,other) -> bool:
    #     if self.position > other.position:
    #         return True
    #     else:
    #         return False
        
    # def __lt__(self, other) -> bool:
    #     if self.position < other.position:
    #         return True
    #     else:
    #         return False
        
    # def __ge__(self, other) -> bool:
    #     return self < other or self == other
    
    # def __le__(self,other) -> bool:
    #     # if self.color == other.color:
    #     #     return self.label <= other.label
    #     return self.position <= other.position