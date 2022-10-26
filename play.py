from hand import Hand
from chips import Chips
from deck import Deck


class Game:

    def __init__(self):
        self.playing = True
        self.player_chips = Chips()

    @staticmethod
    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input('How many chips do you want to bet?: '))
            except ValueError:
                print('Error: a number value is required')
            else:
                if chips.bet > chips.total:
                    print("You don't have enough chips for that bet!")
                else:
                    break

    @staticmethod
    def hit(hand, deck):
        hand.add_card(deck.deal_card())
        hand.adjust_for_ace()

    def hit_or_stand(self, players_hand, dealers_hand, deck):

        while True:
            try:
                choice = str(input('\nDo you want to hit or stand? (h or s): ')).casefold()
            except ValueError:
                print('You must enter h or s')
            else:
                if choice == 'h':
                    self.hit(players_hand, deck)
                    self.show_some(players_hand, dealers_hand)
                elif choice == 's':
                    print('Player has chosen to stand. Now it is the dealer\'s turn.')
                    self.playing = False
                else:
                    continue
                break

    @staticmethod
    def show_some(player_hand, dealer_hand):
        print(f'\nDealer hand: (Hidden card, {dealer_hand.cards[1]})')
        print('Player hand: (', end='')
        print(*player_hand.cards, sep=', ', end=')\n')

    @staticmethod
    def show_all(player_hand, dealer_hand):
        print('\nDealer hand: (', end='')
        print(*dealer_hand.cards, sep=', ', end=')\n')
        print(f'Dealer total: {dealer_hand.value}')
        print('Player hand: (', end='')
        print(*player_hand.cards, sep=', ', end=')\n')
        print(f'Player total: {player_hand.value}')

    @staticmethod
    def player_wins(dealer_hand, chips):
        if dealer_hand.value > 21:
            print('\nDealer bust, player wins!!')
        else:
            print('\nPlayer wins!!')
        chips.win_bet()

    @staticmethod
    def dealer_wins(player_hand, chips):

        if player_hand.value > 21:
            print('\nPlayer bust, dealer wins!!')
        else:
            print('\nDealer wins!!')
        chips.lose_bet()

    @staticmethod
    def push():
        print('\nDealer and player tie!')

    def play(self):
        while True:
            print('This is blackjack. The goal is to reach as close to 21 as you can without going above it.')
            print('The dealer will continue to hit until they reach a total of at least 17.')
            print('Aces can be either 1 or 11\n')

            deck = Deck()
            deck.shuffle()
            players_hand = Hand()
            dealers_hand = Hand()

            for i in range(2):
                players_hand.add_card(deck.deal_card())
                dealers_hand.add_card(deck.deal_card())

            if self.player_chips.total <= 0:
                self.player_chips = Chips()

            self.take_bet(self.player_chips)

            self.show_some(players_hand, dealers_hand)

            while self.playing:
                self.hit_or_stand(players_hand, dealers_hand, deck)

                if players_hand.value > 21:
                    self.dealer_wins(players_hand, self.player_chips)
                    break

            if players_hand.value <= 21:
                while dealers_hand.value < 17:
                    self.hit(dealers_hand, deck)

                self.show_all(players_hand, dealers_hand)

                if dealers_hand.value > 21:
                    self.player_wins(dealers_hand, self.player_chips)
                elif players_hand.value > dealers_hand.value:
                    self.player_wins(dealers_hand, self.player_chips)
                elif dealers_hand.value > players_hand.value:
                    self.dealer_wins(players_hand, self.player_chips)
                else:
                    self.push()

            print(f'\nPlayers chip total: {self.player_chips.total}')

            play_again = input('\nWould you like to play again? (y or n): ')

            if play_again.lower() == 'y':
                self.playing = True
                continue
            else:
                break


game = Game()
game.play()
