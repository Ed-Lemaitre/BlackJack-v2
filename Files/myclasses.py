class game:
    def __init__(self) -> None:
        self.complete_deck = [
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
        self.deck = self.complete_deck
        self.current_money = self.starting_money

    player_cards = []
    dealer_cards = []
    bet_amount = 0
    insurance_amount = 0
    split_A_bet_amount = 0
    split_B_bet_amount = 0
    is_natural = False
    is_split = False
    is_double = False
    player_split_A = []
    player_split_B = []
