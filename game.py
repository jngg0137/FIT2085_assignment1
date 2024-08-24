from data_structures.referential_array import ArrayR
from player import Player
from card import CardColor, CardLabel, Card
from random_gen import RandomGen
from constants import Constants
from data_structures.stack_adt import ArrayStack
from data_structures.array_sorted_list import ArraySortedList
from constants import Constants

class Game:
    """
    Game class to play the game
    """
    def __init__(self) -> None:
        """
        Constructor for the Game class

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:   O(1)
            Worst Case Complexity:  O(1)
        """
        self.players = ArraySortedList(Constants.MAX_PLAYERS)
        self.draw_pile = ArrayStack(Constants.DECK_SIZE)
        self.discard_pile = ArrayR(Constants.DECK_SIZE)
        self.current_player = Player
        self.current_color = None
        self.current_label = None

    def generate_cards(self) -> ArrayR[Card]:
        """
        Method to generate the cards for the game

        Args:
            None

        Returns:
            ArrayR[Card]: The array of Card objects generated

        Complexity:
            Best Case Complexity: O(N) - Where N is the number of cards in the deck
            Worst Case Complexity: O(N) - Where N is the number of cards in the deck
        """
        list_of_cards: ArrayR[Card] = ArrayR(Constants.DECK_SIZE)
        idx: int = 0

        for color in CardColor:
            if color != CardColor.CRAZY:
                # Generate 4 sets of cards from 0 to 9 for each color
                for i in range(10):
                    list_of_cards[idx] = Card(color, CardLabel(i))
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel(i))
                    idx += 1

                # Generate 2 of each special card for each color
                for i in range(2):
                    list_of_cards[idx] = Card(color, CardLabel.SKIP)
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel.REVERSE)
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel.DRAW_TWO)
                    idx += 1
            else:
                # Generate the crazy and crazy draw 4 cards
                for i in range(4):
                    list_of_cards[idx] = Card(CardColor.CRAZY, CardLabel.CRAZY)
                    idx += 1
                    list_of_cards[idx] = Card(CardColor.CRAZY, CardLabel.DRAW_FOUR)
                    idx += 1

                # Randomly shuffle the cards
                RandomGen.random_shuffle(list_of_cards)

                return list_of_cards

    def initialise_game(self, new_players: ArrayR[Player]) -> None:
        """
        Method to initialise the game

        Args:
            players (ArrayR[Player]): The array of players

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        card_index = 0
        cards_generated = self.generate_cards()
        self.players = new_players
        # print(cards_generated.__str__())

        #deal cards to players until each player has 7 cards
        # print("Dealing cards to players..")
        for _ in range(0,Constants.NUM_CARDS_AT_INIT):
            # print("Dealing card",_)
            for player in self.players:
                card_dealt = cards_generated[card_index]
                player.add_card(card_dealt)
                card_index += 1
                # print("Player",i,"was dealt",card_dealt)

        #add remaining cards to the draw pile
        #print("Cards added to draw pile")
        for i in range(card_index,Constants.DECK_SIZE):
            card_dealt = cards_generated[i]
            # print(card_dealt.__str__())
            self.draw_pile.push(card_dealt)

        #draw card from draw pile and put in discard pile
        continue_draw_cards = True
        # print("Card put in discard:")
        while continue_draw_cards:
            counter = 0
            card_drawn = self.draw_pile.pop()
            self.discard_pile[counter] = card_drawn
            counter += 1
            # print(card_drawn.__str__())
            if (card_drawn.color != CardColor.CRAZY) and card_drawn.label not in (CardLabel.SKIP, CardLabel.REVERSE, CardLabel.DRAW_TWO, CardLabel.CRAZY, CardLabel.DRAW_FOUR):
                continue_draw_cards = False

        self.current_color = card_drawn.color
        self.current_label = card_drawn.label            
        # print("Current ",card_drawn.__str__())

    def play_reverse(self) -> None:
        """
        Method to play a reverse card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        # new_order = ArraySortedList(self.players.__len__())
        # current_order = self.players
        # for i in range(self.players.__len__() - 1,0,-1):
        #     player = current_order.__getitem__(i)
        #     new_order.add(player)
        # self.players = new_order
        # new_order = ArraySortedList(self.players.__len__())
        # for i in range(0,self.players.__len__()):
        #     print(self.players.__len__() - i)
        #     player = self.players.__getitem__(self.players.__len__() - i)
        #     new_order.__setitem__(i,player)
        # self.players = new_order

    def play_skip(self) -> None:
        """
        Method to play a skip card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        try:
            current_index = self.players.index(self.current_player)
            new_index = current_index + 1
        except ValueError:
            new_index = 1
        new_current_player = self.players[new_index]
        self.current_player = new_current_player

    def draw_card(self, player: Player, playing: bool) -> Card | None:
        """
        Method to draw a card from the deck

        Args:
            player (Player): The player who is drawing the card
            playing (bool): A boolean indicating if the player is able to play the card

        Returns:
            Card - When drawing a playable card, other return None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """

        card_drawn = self.draw_pile.pop()
        # print(card_drawn.__str__())
        if playing:
            if ((card_drawn.color == CardColor.CRAZY)):
                return card_drawn
            elif (card_drawn.color == self.current_color):
                self.current_label = card_drawn.label
                return card_drawn
            elif ((card_drawn.label == self.current_label)):
                self.current_color = card_drawn.color
                return card_drawn
            else:
                 player.add_card(card_drawn)
        else:
            player.add_card(card_drawn)

    def next_player(self) -> Player:
        """
        Method to get the next player

        Args:
            None

        Returns:
            Player: The next player

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        # if (self.players.__contains__(self.current_player)):
        #     index_next_player = self.players.index(self.current_player)
        #     return self.players.__getitem__(index_next_player)
        # else:
        #     return self.players.__getitem__(0) 
        try:
            index = self.players.index(self.current_player)
            return self.players[index]
        except ValueError:
            return self.players[0]
    
    def crazy_play(self, card: Card) -> None:
        """
        Method to play a crazy card

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        if (card.label == CardLabel.DRAW_FOUR):
            for _ in range(4):
                self.next_player().draw_card(False)
        else:
            self.current_color = CardColor(RandomGen.randint(0,3))

    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError


def test_case():
    players: ArrayR[Player] = ArrayR(4)
    players[0] = Player("Alice", 0)
    players[1] = Player("Bob", 1)
    players[2] = Player("Charlie", 2)
    players[3] = Player("David", 3)
    g: Game = Game()
    g.initialise_game(players)
    winner: Player = g.play_game()
    print(f"Winner is {winner.name}")


if __name__ == '__main__':
    test_case()
