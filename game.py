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
                # print("Player",player.name,"was dealt",card_dealt)

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

    def refill_draw_pile(self) -> None:
        """
        Method to shuffle discard pile and place in draw pile

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        stored_card = self.discard_pile[-1]
        print(stored_card.__str__())
        last_index = self.discard_pile.index(stored_card)

        #shuffle discard pile and store all of it (except stored_card) in another array to shuffle
        temp_array_index = 0
        temp_array = ArrayR(len(self.discard_pile))
        for i in range(last_index - 1, 0,-1):
            temp_array[temp_array_index] = self.discard_pile[i]
            temp_array_index += 1
        RandomGen.random_shuffle(temp_array)

        #add cards from shuffled array back to draw pile such that last index is on top, stored_card goes to discard pile
        for card in temp_array:
            self.draw_pile.push(card)
        self.discard_pile = ArrayR(Constants.DECK_SIZE)
        self.discard_pile[0] = stored_card
        prompt_user = input("Discard pile reshuffled")

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
        self.players = self.players[::-1]
        # for player in self.players:
        #     print(player.name)

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
        # except IndexError:
        #     new_index = 0
            return None
        # if (new_index == len(self.players)):
        #     new_index -= 1
        if (new_index == len(self.players)):
            new_index = 0
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
        if (len(self.draw_pile) == 0):
            self.refill_draw_pile()
        card_drawn = self.draw_pile.pop()
        print("Card drawn from pile:",card_drawn.__str__())
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
                 return None
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
        try:
            index = self.players.index(self.current_player)
            return self.players[index + 1]
        except ValueError:
            return self.players[0]
        except IndexError:
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
                self.draw_card(self.next_player(),False)
            self.play_skip()
        self.current_color = CardColor(RandomGen.randint(0,3))

    def check_hand(self, hand: ArraySortedList[Card]) -> Card | str:
        """
        Method to check if player hand contains a card that can be played

        Args:
            hand (ArraySortedList[Card]): The player's hand

        Returns:
            Card - When playable card in hand is found, other return None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        for card_index in range(0,hand.length):
            if (hand[card_index].color == self.current_color) or (hand[card_index].label == self.current_label) or (hand[card_index].color == CardColor.CRAZY):
                return hand[card_index]
        ret = "No playable card"
        return ret
    
    def play_card(self,card:Card) -> None:
        """
        Method to play a card. If it's a card that isn't numbered, carry out their effects

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        if (card.label == CardLabel.REVERSE):
            self.play_reverse()
        elif (card.label == CardLabel.SKIP):
            self.play_skip()
        elif (card.color == CardColor.CRAZY):
            self.crazy_play(card)
        elif (card.label == CardLabel.DRAW_TWO):
            for _ in range(2):
                self.draw_card(self.next_player(),False)
            self.play_skip()

        if (card.color != CardColor.CRAZY):
            self.current_color = card.color
        self.current_label = card.label

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
        rounds = 1
        print("\n-------------- Game start! --------------")
        while True:
            print("\n----------------- Round",rounds,"-----------------")
            print("Current color:",self.current_color)
            print("Current label:",self.current_label)
            player = self.next_player()
            self.current_player = player

            #display player info
            for player_display in self.players:
                print(player_display.name,"(" , player_display.hand.length , ")")
                display = ""
                for card_index in range(0,player_display.hand.length):
                    display += player_display.hand[card_index].__str__()
                print(" ".join(["Cards:",display]))

            #check player hand to see if there are playable cards
            playableCard = self.check_hand(player.hand)
            if (playableCard == "No playable card"):
                print(player.name,"had no card to play in deck and drew from draw pile")
                drawn_card = self.draw_card(player,True)
                if isinstance(drawn_card,Card):
                    print("!!THE DRAWN CARD MATCHES AND IS PLAYED!!")
                    self.play_card(drawn_card)
            else:
                print(player.name,"played a card: ", playableCard.__str__())
                player.hand.delete_at_index(player.hand.index(playableCard))
                self.play_card(playableCard)
            
            #check if player hand is empty
            if (player.hand.length == 0):
                print(player.name,"has discarded all their cards")
                return player
            rounds += 1

def test_case():
    # RandomGen.set_seed(1802)
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
