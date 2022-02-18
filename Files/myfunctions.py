# myfunctions.py

import myclasses as myc
import random

game_instance = myc.game()


def play_game():

    game_instance.soft_reset()

    screen_print("instructions")

    screen_print("make_bet")

    while True:
        bet = input()
        if check_bet(bet):
            break

    deal()

    while True:
        screen_print("game_screen")
        action = input()
        if action == "Sp" and split():
            break
        if action == "Do" and double():
            break
        if action == "Hi" or action == "St":
            game_instance.is_normal_hit_stay = action
            break
        if action == "Q":
            break

    if is_natural(game_instance.player_cards):
        game_instance.is_natural = True

    while (
        game_instance.is_normal
        and game_instance.player_cards != ""
        and not game_instance.is_normal_finished
    ):
        play_normal()

    while (
        game_instance.is_double
        and game_instance.player_cards != ""
        and not game_instance.is_double_finished
    ):
        play_double()

    while (
        game_instance.is_split
        and (game_instance.player_split_A != "" or game_instance.player_split_B != "")
        and not game_instance.is_split_finished
    ):
        play_split()

    dealer_play()

    pay()

    screen_print("resume")

    print("----------------------------")
    if input("Do you want another game? s/n: ") == "n":
        return False
    else:
        return True


def screen_print(to_print):
    if to_print == "instructions":
        print("--- Welcome to Black Jack---")
    elif to_print == "game_screen":
        print(f"Visible dealers card is: {game_instance.dealer_cards[0]}")
        print("Your hand is: ", end="")
        for a in game_instance.player_cards:
            print(f"{a} ", end="")
        print("")
        print(f"Your Money: {game_instance.current_money}")
        print(
            "Please choose and option: (Sp)lit / (Do)uble / (Hi)t / (St)ay / (Q)uit: "
        )
    elif to_print == "is_natural":
        print("Congratulations! You have won!")
    elif to_print == "no_split":
        print("Split is not possible. Try other option")
    elif to_print == "no_double":
        print("Double is not possible. Try other option")
    elif to_print == "split_instructions":
        print("Now you have two games.")
    elif to_print == "split_game_screen":
        print(f"Visible dealers card is: {game_instance.dealer_cards[0]}")
        print("Your first hand is ", end="")
        for a in game_instance.player_split_A:
            print(f"{a} ", end="")
        print("")
        print("Your second hand is ", end="")
        for a in game_instance.player_split_B:
            print(f"{a} ", end="")
        print("")
    elif to_print == "make_bet":
        print(f"You have {game_instance.current_money} available")
        print("Make your bet: ", end="")
    elif to_print == "show_game":
        print(f"Visible dealers card is: {game_instance.dealer_cards[0]}")
        print("Your hand is: ", end="")
        for a in game_instance.player_cards:
            print(f"{a} ", end="")
        print("")
    elif to_print == "resume":
        print("-------------------------------")
        print("You have finished this round")
        print(f"You have ${game_instance.current_money}")
        print(" ---- DEALER CARDS ----")
        for a in game_instance.dealer_cards:
            print(f"{a} ", end="")
        print("")
        print(" ---- YOUR CARDS ----")
        if game_instance.is_normal or game_instance.is_double:
            for a in game_instance.player_cards:
                print(f"{a} ", end="")
        elif game_instance.is_split:
            for a in game_instance.player_split_A:
                print(f"{a} ", end="")
            print("")
            for a in game_instance.player_split_B:
                print(f"{a} ", end="")
        print("")


def check_bet(bet):
    if bet.isdigit():
        apuesta = int(bet)
        if apuesta in range(2, 501) and apuesta <= game_instance.current_money:
            game_instance.bet_amount = apuesta
            game_instance.current_money -= apuesta
            return True
    print("------------------------------------")
    print("------Thats not a valid amount------")
    print("------------------------------------")
    print(
        f"You have ${game_instance.current_money}. Bet range must be from $2 to $500:"
    )
    print("Please, make your bet: ", end="")
    return False


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
        game_instance.is_double = False
        game_instance.is_normal = False
        game_instance.split_A_bet_amount = game_instance.bet_amount
        game_instance.split_B_bet_amount = game_instance.bet_amount
        game_instance.current_money -= game_instance.bet_amount
        game_instance.bet_amount = 0
        game_instance.player_split_A.append(game_instance.player_cards[0])
        game_instance.player_split_B.append(game_instance.player_cards[1])
        return True
    else:
        screen_print("no_split")
    return False


def double():
    if is_double_possible():
        game_instance.is_split = False
        game_instance.is_double = True
        game_instance.is_normal = False
        game_instance.current_money -= game_instance.bet_amount
        game_instance.bet_amount += game_instance.bet_amount
        return True
    else:
        screen_print("no_double")
        return False


def play_double():
    deal_one(game_instance.player_cards)
    if is_busted(game_instance.player_cards):
        game_instance.is_busted_double = True
    game_instance.is_double_finished = True
    screen_print("show_game")


def is_double_possible():
    if not game_instance.is_double and is_sum_double(game_instance.player_cards):
        return True
    return False


def is_sum_double(object_property):
    sum_to_check = sum_min_best(object_property)
    return sum_to_check[0] in range(9, 12) or sum_to_check[1] in range(9, 12)


def play_normal():
    while True:
        if game_instance.is_normal_hit_stay == "St":
            game_instance.is_normal_finished = True
            break
        elif (
            not game_instance.is_normal_finished
            and game_instance.is_normal_hit_stay == "Hi"
        ):
            deal_one(game_instance.player_cards)
        if not game_instance.is_normal_finished and is_busted(
            game_instance.player_cards
        ):
            game_instance.is_busted = True
            game_instance.is_normal_finished = True
        if not game_instance.is_normal_finished and not game_instance.is_busted:
            screen_print("show_game")
            print("Select option (St)ay or (Hi)t: ")
            game_instance.is_normal_hit_stay = input()
        else:
            break


def is_natural(mano_verificar):
    nat = ["10", "J", "Q", "K"]
    if sum([cadena.count("A") for cadena in mano_verificar]) == 1:
        if sum([cadena.count(a) for cadena in mano_verificar for a in nat]):
            return True
    return False


def is_split_possible():
    if (
        not game_instance.is_split
        and game_instance.player_cards[0][0] == game_instance.player_cards[1][0]
    ):
        return True
    return False


def is_busted(object_property):
    sum_to_check = sum_min_best(object_property)
    return sum_to_check[0] > 21


def play_split():
    while not (game_instance.is_split_A_finished and game_instance.is_split_B_finished):
        screen_print("split_instructions")
        while not game_instance.is_split_A_finished:
            screen_print("split_game_screen")
            print("Choose an option for your first hand: (Hi)t / (St)ay: ")
            action = input()
            if action == "St":
                game_instance.is_split_A_finished = True
                break
            elif action != "Hi" and action != "St":
                print("Choose a valid option!")
            elif action == "Hi":
                deal_one(game_instance.player_split_A)
                if is_busted(game_instance.player_split_A):
                    print("You loose your first splited Hand")
                    game_instance.is_split_A_finished = True
                    game_instance.is_busted_A = True
                    game_instance.split_A_bet_amount = 0
                    break

        while not game_instance.is_split_B_finished:
            screen_print("split_game_screen")
            print("Choose an option for your second hand: (Hi)t / (St)ay: ")
            action = input()
            if action == "St":
                game_instance.is_split_B_finished = True
                break
            if action != "Hi" and action != "St":
                print("Choose a valid option!")
            if action == "Hi":
                deal_one(game_instance.player_split_B)
                if is_busted(game_instance.player_split_B):
                    print("You loose your second splited Hand")
                    game_instance.is_split_B_finished = True
                    game_instance.is_busted_B = True
                    game_instance.split_B_bet_amount = 0
                    break
        if game_instance.is_split_A_finished and game_instance.is_split_B_finished:
            game_instance.is_split_finished = True


def dealer_play():
    while True:
        sum_dealer = min(sum_min_best(game_instance.dealer_cards))
        if sum_dealer < 17:
            deal_one(game_instance.dealer_cards)
            if is_busted(game_instance.dealer_cards):
                game_instance.is_busted_dealer = True
                break
        else:
            break


def pay():
    if game_instance.is_natural:
        if is_natural(game_instance.dealer_cards):
            game_instance.current_money += game_instance.bet_amount
            game_instance.bet_amount = 0
        else:
            game_instance.current_money += game_instance.bet_amount * 2.5
            game_instance.bet_amount = 0
    elif game_instance.is_normal:
        pay_normal()
    elif game_instance.is_double:
        pay_double()
    elif game_instance.is_split:
        pay_split()


def pay_normal():
    if game_instance.is_busted:
        game_instance.bet_amount = 0
    elif game_instance.is_busted_dealer:
        game_instance.current_money += game_instance.bet_amount * 2
        game_instance.bet_amount = 0
    else:
        sum_dealer = max(sum_min_best(game_instance.dealer_cards))
        sum_player = max(sum_min_best(game_instance.player_cards))
        if sum_dealer > sum_player:
            game_instance.bet_amount = 0
        elif sum_dealer < sum_player:
            game_instance.current_money += game_instance.bet_amount * 2
            game_instance.bet_amount = 0
        else:
            game_instance.current_money += game_instance.bet_amount
            game_instance.bet_amount = 0


def pay_double():
    pay_normal()


def pay_split():
    # Juego A
    if game_instance.is_busted_A:
        game_instance.split_A_bet_amount = 0
    elif game_instance.is_busted_dealer:
        game_instance.current_money += game_instance.split_A_bet_amount * 2
        game_instance.split_A_bet_amount = 0
    else:
        sum_dealer = max(sum_min_best(game_instance.dealer_cards))
        sum_player = max(sum_min_best(game_instance.player_split_A))
        if sum_dealer > sum_player:
            game_instance.split_A_bet_amount = 0
        elif sum_dealer < sum_player:
            game_instance.current_money += game_instance.split_A_bet_amount * 2
            game_instance.split_A_bet_amount = 0
        else:
            game_instance.current_money += game_instance.split_A_bet_amount
            game_instance.split_A_bet_amount = 0

    # Juego B
    if game_instance.is_busted_B:
        game_instance.split_B_bet_amount = 0
    elif game_instance.is_busted_dealer:
        game_instance.current_money += game_instance.split_B_bet_amount * 2
        game_instance.split_B_bet_amount = 0
    else:
        sum_dealer = max(sum_min_best(game_instance.dealer_cards))
        sum_player = max(sum_min_best(game_instance.player_split_B))
        if sum_dealer > sum_player:
            game_instance.split_B_bet_amount = 0
        elif sum_dealer < sum_player:
            game_instance.current_money += game_instance.split_B_bet_amount * 2
            game_instance.split_B_bet_amount = 0
        else:
            game_instance.current_money += game_instance.split_B_bet_amount
            game_instance.split_B_bet_amount = 0


def sum_min_best(object_property):
    lista = [x[:-1] for x in object_property]

    count_A = lista.count("A")
    count_JQK = sum([lista.count(fig) for fig in ["J", "Q", "K"]])
    sum_digits = sum([int(x) for x in lista if x.isdigit()])

    sum_min = sum_digits + count_JQK * 10 + count_A * 1
    sum_max = sum_min + (10 if count_A > 0 else 0)
    sum_best = sum_min if sum_max > 21 else sum_max

    return (sum_min, sum_best)
