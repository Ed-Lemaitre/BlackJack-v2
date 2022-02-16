# mazo de cartas = deck of cards
# mano = hand

import myclasses as myc
import random

game_instance = myc.game()


def play_game():

    screen_print("instructions")

    deal()

    screen_print("game_screen")
    action = input()
    if action == "Sp":
        split()
    if action == "Do":
        double()
    if action == "Hi":
        hit()
    if action == "St":
        stay()
    if action == "Q":
        return False

    if is_natural(game_instance.player_cards):
        pagar("natural")
        screen_print("is_natural")
        return False

    # Dealer Fase
    # pide hasta que suma maxima o minima llegue a 17 o mas
    dealer_play()

    pagar("dealer")

    print("----------------------------")
    if input("Do you want another game? s/n") == "n":
        return False


def screen_print(to_print):
    if to_print == "instructions":
        print("--- Welcome to Black Jack---")
        input("Press 'Enter' to start the game")
    if to_print == "game_screen":
        print(f"Visible dealers card is: {game_instance.dealer_cards[0]}")
        print(
            f"Your hand is: {game_instance.player_cards[0]} {game_instance.player_cards[1]}"
        )
        print(f"Your Money: {game_instance.current_money}")
        print(
            "Please choose and option: (Sp)lit / (Do)uble / (Hi)t / (St)ay / (Q)uit: "
        )
    if to_print == "is_natural":
        print("Congratulations! You have won!")
    if to_print == "no_split":
        print("Split is not possible. Try other option")
    if to_print == "no_double":
        print("Double is not possible. Try other option")
    if to_print == "split_instructions":
        print("Now you have two games. You can only (Hi)t or (St)ay")
    if to_print == "split_game_screen":
        print(f"Visible dealers card is: {game_instance.dealer_cards[0]}")
        print(
            f"Your first hand is: {game_instance.player_split_A[0]} {game_instance.player_split_A[1]}"
        )
        print(
            f"Your second hand is: {game_instance.player_split_B[0]} {game_instance.player_split_B[1]}"
        )


def deal():
    game_instance.player_cards.append(random_card())
    game_instance.player_cards.append(random_card())
    game_instance.dealer_cards.append(random_card())
    game_instance.dealer_cards.append(random_card())


def deal_one(object_property):
    object_property.append(random_card())


def random_card():
    card_position = random.randrange(0, len(game_instance.deck) - 1)
    return game_instance.deck.pop(card_position)


def split():
    if is_split_possible():
        game_instance.is_split = True
        game_instance.split_A_bet_amount = game_instance.bet_amount
        game_instance.split_B_bet_amount = game_instance.bet_amount
        game_instance.current_money -= game_instance.bet_amount
        game_instance.bet_amount = 0

        game_instance.player_split_A.append(game_instance.player_cards[0])
        game_instance.player_split_B.append(game_instance.player_cards[1])

        play_split()

    else:
        screen_print("no_split")


def double():
    if is_double_possible():
        game_instance.is_double = True
        game_instance.current_money -= game_instance.bet_amount
        game_instance.bet_amount += game_instance.bet_amount

        play_double()

    else:
        screen_print("no_double")


def play_double():
    deal_one(game_instance.player_cards)


def is_double_possible():
    if not game_instance.is_double and is_sum_double(game_instance.player_cards):
        return True
    return False


def is_sum_double(object_property):
    l = []
    sum_max = 0
    sum_min = 0
    for a in object_property:
        l.append(a[:-1])
    for card_values in l:
        if card_values == "A":
            sum_max += 11
            sum_min += 1
        if card_values == "K":
            sum_max += 13
            sum_min += 13
        if card_values == "Q":
            sum_max += 12
            sum_min += 12
        if card_values == "J":
            sum_max += 11
            sum_min += 11
        else:
            sum_max += int(a)
            sum_min += int(a)
    if sum_max in range(9, 12) or sum_min in range(9, 12):
        return True
    else:
        return False


def hit():  # this function is for the player
    deal_one(game_instance.player_cards)
    if is_busted(game_instance.player_cards):
        print("You loose !!")
        game_instance.bet_amount = 0


def stay():
    pass


def is_natural(mano_verificar):
    nat = ["10", "J", "Q", "K"]
    if sum([cadena.count("A") for cadena in mano_verificar]) == 1:
        if sum([cadena.count(a) for cadena in mano_verificar for a in nat]):
            return True
    return False


def is_split_possible():
    if (
        not game_instance.is_split
        and game_instance.player_cards[0][0] == game_instance.player_cards[0][1]
    ):
        return True
    return False


def is_busted(object_property):
    l = []
    sum = 0
    for a in object_property:
        l.append(a[:-1])
    for card_values in l:
        if card_values == "A":
            sum += 1
        if card_values == "K":
            sum += 13
        if card_values == "Q":
            sum += 12
        if card_values == "J":
            sum += 11
        if card_values == "10":
            sum += 10
    if sum > 21:
        return True
    else:
        return False


def play_split():
    while True:
        screen_print("split_instructions")
        screen_print("split_game_screen")
        while True:
            print("Choose an option for your first hand: (Hi)t / (St)ay: ")
            action = input()
            if action == "St":
                break
            if action != "Hi" and action != "St":
                print("Choose a valid option!")
            if action == "Hi":
                deal_one(game_instance.player_split_A)
                if is_busted(game_instance.player_split_A):
                    print("You loose your first splited Hand")
                    game_instance.split_A_bet_amount = 0
                    break

        while True:
            print("Choose an option for your second hand: (Hi)t / (St)ay: ")
            action = input()
            if action == "St":
                break
            if action != "Hi" and action != "St":
                print("Choose a valid option!")
            if action == "Hi":
                deal_one(game_instance.player_split_B)
                if is_busted(game_instance.player_split_B):
                    print("You loose your second splited Hand")
                    game_instance.split_B_bet_amount = 0
                    break


def dealer_play():
    while True:
        if (
            is_sum_dealer(game_instance.dealer_cards)[0] < 17
            or is_sum_dealer(game_instance.dealer_cards)[1] < 17
        ):
            resultado = hit_dealer()
            if resultado == False:
                break


def hit_dealer():
    deal_one(game_instance.dealer_cards)
    if is_busted(game_instance.dealer_cards):
        return False


def is_sum_dealer(object_property):
    l = []
    sum_max = 0
    sum_min = 0
    for a in object_property:
        l.append(a[:-1])
    for card_values in l:
        if card_values == "A":
            sum_max += 11
            sum_min += 1
        if card_values == "K":
            sum_max += 13
            sum_min += 13
        if card_values == "Q":
            sum_max += 12
            sum_min += 12
        if card_values == "J":
            sum_max += 11
            sum_min += 11
        else:
            sum_max += int(a)
            sum_min += int(a)
    return (sum_min, sum_max)


def pagar(what):
    if what == "natural":
        if is_natural(game_instance.dealer_cards):
            game_instance.current_money += game_instance.bet_amount
            game_instance.bet_amount = 0
        else:
            game_instance.current_money += game_instance.bet_amount * 2.5
            game_instance.bet_amount = 0
    elif what == "dealer":
        if game_instance.is_split == True:
            pay_split()
        elif game_instance.is_double == True:
            pay_normal()
        else:
            pay_normal()


def pay_normal():
    if is_busted(game_instance.dealer_cards):
        game_instance.current_money += game_instance.bet_amount * 2
        game_instance.bet_amount = 0
    else:
        if sum_pay(game_instance.dealer_cards) > sum_pay(game_instance.player_cards):
            game_instance.bet_amount = 0
        elif sum_pay(game_instance.dealer_cards) < sum_pay(game_instance.player_cards):
            game_instance.current_money += game_instance.bet_amount * 2
            game_instance.bet_amount = 0
        else:
            game_instance.current_money += game_instance.bet_amount
            game_instance.bet_amount = 0


def pay_split():
    if is_busted(game_instance.dealer_cards):
        game_instance.current_money += (
            game_instance.split_A_bet_amount * 2 + game_instance.split_B_bet_amount * 2
        )
        game_instance.split_B_bet_amount = 0
        game_instance.split_A_bet_amount = 0

    else:
        if sum_pay(game_instance.dealer_cards) > sum_pay(game_instance.player_split_A):
            game_instance.split_A_bet_amount = 0
        elif sum_pay(game_instance.dealer_cards) < sum_pay(
            game_instance.player_split_A
        ):
            game_instance.current_money += game_instance.split_A_bet_amount * 2
            game_instance.bet_amount = 0
        else:
            game_instance.current_money += game_instance.split_A_bet_amount
            game_instance.bet_amount = 0
        if sum_pay(game_instance.dealer_cards) > sum_pay(game_instance.player_split_B):
            game_instance.split_B_bet_amount = 0
        elif sum_pay(game_instance.dealer_cards) < sum_pay(
            game_instance.player_split_B
        ):
            game_instance.current_money += game_instance.split_B_bet_amount * 2
            game_instance.bet_amount = 0
        else:
            game_instance.current_money += game_instance.split_B_bet_amount
            game_instance.bet_amount = 0


def sum_pay(object_property):
    l = []
    sum_max = 0
    sum_min = 0
    for a in object_property:
        l.append(a[:-1])
    for card_values in l:
        if card_values == "A":
            sum_max += 11
            sum_min += 1
        if card_values == "K":
            sum_max += 13
            sum_min += 13
        if card_values == "Q":
            sum_max += 12
            sum_min += 12
        if card_values == "J":
            sum_max += 11
            sum_min += 11
        else:
            sum_max += int(a)
            sum_min += int(a)
    if sum_max < 22:
        return sum_max
    else:
        return sum_min
