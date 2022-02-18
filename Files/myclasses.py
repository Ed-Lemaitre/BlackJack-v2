# myclasses.py


class game:
    def __init__(self) -> None:
        self.deck = [
            "A♦",
            "2♦",
            "3♦",
            "4♦",
            "5♦",
            "6♦",
            "7♦",
            "8♦",
            "9♦",
            "10♦",
            "J♦",
            "Q♦",
            "K♦",
            "A♣",
            "2♣",
            "3♣",
            "4♣",
            "5♣",
            "6♣",
            "7♣",
            "8♣",
            "9♣",
            "10♣",
            "J♣",
            "Q♣",
            "K♣",
            "A♥",
            "2♥",
            "3♥",
            "4♥",
            "5♥",
            "6♥",
            "7♥",
            "8♥",
            "9♥",
            "10♥",
            "J♥",
            "Q♥",
            "K♥",
            "A♠",
            "2♠",
            "3♠",
            "4♠",
            "5♠",
            "6♠",
            "7♠",
            "8♠",
            "9♠",
            "10♠",
            "J♠",
            "Q♠",
            "K♠",
        ]
        self.starting_money = 2000
        self.current_money = self.starting_money

    player_cards = []
    dealer_cards = []
    bet_amount = 0
    split_A_bet_amount = 0
    split_B_bet_amount = 0
    is_natural = False
    is_split = False
    is_double = False
    is_normal = True
    is_normal_finished = False
    is_double_finished = False
    is_split_finished = False
    is_split_A_finished = False
    is_split_B_finished = False
    is_busted = False
    is_busted_double = False
    is_busted_dealer = False
    is_busted_A = False
    is_busted_B = False
    is_normal_hit_stay = ""
    player_split_A = []
    player_split_B = []

    def soft_reset(self):
        self.deck = [
            "A♦",
            "2♦",
            "3♦",
            "4♦",
            "5♦",
            "6♦",
            "7♦",
            "8♦",
            "9♦",
            "10♦",
            "J♦",
            "Q♦",
            "K♦",
            "A♣",
            "2♣",
            "3♣",
            "4♣",
            "5♣",
            "6♣",
            "7♣",
            "8♣",
            "9♣",
            "10♣",
            "J♣",
            "Q♣",
            "K♣",
            "A♥",
            "2♥",
            "3♥",
            "4♥",
            "5♥",
            "6♥",
            "7♥",
            "8♥",
            "9♥",
            "10♥",
            "J♥",
            "Q♥",
            "K♥",
            "A♠",
            "2♠",
            "3♠",
            "4♠",
            "5♠",
            "6♠",
            "7♠",
            "8♠",
            "9♠",
            "10♠",
            "J♠",
            "Q♠",
            "K♠",
        ]
        self.player_cards = []
        self.dealer_cards = []
        self.bet_amount = 0
        self.split_A_bet_amount = 0
        self.is_natural = False
        self.is_split = False
        self.is_double = False
        self.is_normal = True
        self.is_normal_finished = False
        self.is_double_finished = False
        self.is_split_finished = False
        self.is_split_A_finished = False
        self.is_split_B_finished = False
        self.is_busted = False
        self.is_busted_double = False
        self.is_busted_dealer = False
        self.is_busted_A = False
        self.is_busted_B = False
        self.is_normal_hit_stay = ""
        self.player_split_A = []
        self.player_split_B = []
