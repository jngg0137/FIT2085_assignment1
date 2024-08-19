from card import Card
from constants import Constants
from data_structures.array_sorted_list import *

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
        self.hand = ArraySortedList(7)

        #toString method
        def __str__(self):
            return f"Player name: {self.color.name}, Position: {self.label.name})"

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
        return self.hand.__getitem__(index)
    
    # def index(self, item: T) -> int:
    #      """ Find the position of a given item in the list. """
    #      for i in range(len(self.__len__())):
    #          if item == self.hand[i]:
    #              return i
    #      raise ValueError("Card not in hand")
    
    # # @abstractmethod
    # def insert(self, index: int, item: T) -> None:
    #     """ Insert an item at a given position. """
    #     pass
        
    # # @abstractmethod
    # def __setitem__(self, index: int, item: T) -> None:
    #     """ Magic method. Insert the item at a given position. """
    #     self.hand[index] = item

    # # @abstractmethod
    # def delete_at_index(self, index: int) -> T:
    #     """ 
    #     Delete item at a given position. 

    #     Args:
    #         index (int): The index of the card to be deleted

    #     Returns:
    #         Card: The card at the given index from the player's hand

    #     Complexity:
    #         Best Case Complexity:   O(1) - if index is in last position so loop doesn't start
    #         Worst Case Complexity:  O(len(self.hand.length)) - if index is in the first position so loop runs fully
    #     """
    #     item = self.hand[index]
    #     self.hand.length -= 1
    #     for i in range (index,self.__len__()):
    #         self.hand[i] = self.hand[i+1]
        