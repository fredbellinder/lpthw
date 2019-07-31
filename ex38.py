import random
import string
import os
# ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print("Wait, there are not ten things on that list. Let's fix that.")

# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song",
#               "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now")

# print(f"Here we go: {stuff}")

# print("Let's do some things with stuff.")

# print(stuff[1])
# print(stuff[-1])  # Last element in list
# print(stuff.pop())
# print(" and ".join(stuff))
# print("#".join(stuff[3:5]))


cards_deck = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
]


def setPlayerCount():
    count = 0
    while count < 2:
        try:
            count_input = int(input("Player count: "))
        except Exception:
            print("Players need to be a number, an integer (2 or more)")
            continue
        if isinstance(count_input, int):
            if count_input <= 4 and count_input >= 2:
                count = count_input
            elif count_input < 2:
                print("The player count cannot be less than 2")
            else:
                print(
                    """Your desired player count was out of allowed range, min = 2 and max = 4.""")

    return range(1, count + 1)


players = setPlayerCount()
# print("players ", *players)
player_dict = {}
pairs_collected_total = 0


def getCards(card_count_input):
    card_count = 0
    hand = []
    while card_count < card_count_input and len(cards_deck) != 0:
        card_count += 1
        random_int = int(random.random() * len(cards_deck))
        card = cards_deck.pop(random_int)
        hand.append(card)
    return hand


def checkHand(player):
    global pairs_collected_total
    four_of_a_kind = player['four_of_a_kind']
    for card in set(player['cards']):
        if player['cards'].count(card) >= 4:
            four_of_a_kind.add(card)
            for x in range(player['cards'].count(card)):
                player['cards'].remove(card)
            print("You got a pair!")
            pairs_collected_total += 1
    return four_of_a_kind


def setWhat(set_of_cards):
    what = 'default'
    while not what in set_of_cards:
        what = input("> ").upper()
        if not what in set_of_cards:
            print("You can only ask for cards that you already have on hand...")
            print(f"Try one of these: {set_of_cards}")
    return what


def setWho(excluded):
    who = None
    tries = 0
    while not who in excluded:
        if tries == 3:
            print("No one found with that name, selected a random player...")
            random_int_excluded = int(random.random() * len(excluded))
            who = excluded[random_int_excluded]
        else:
            print(f"Tries until random player is chosen: {3 - tries}")
            who = input("> ").title()
        tries += 1
    return who.title()


def setName(idx):
    letters = list(string.ascii_letters)
    player = ""
    approved = False
    while len(player) < 1:
        player_input = input(f"Player {idx} name: ").title()
        for each in list(player_input):
            if not each in letters:
                print("A player name can only be letters, no symbols or numbers")
                break
            approved = True
        if player_input in player_dict.keys() and approved:
            print("That name has already been taken, be original")
        else:
            player = player_input

    return player.title()


for idx, player in enumerate(players):

    player = setName(player)

    player_dict[player] = {
        "cards": getCards(7),
        "four_of_a_kind": set()
    }
    player_dict[player]['four_of_a_kind'] = checkHand(player_dict[player])
    unused = os.system('clear')

while len(cards_deck) != 0 or pairs_collected_total != 13:
    players = player_dict.keys()
    nonEmptyHands = list(filter(lambda x: len(
        player_dict[x]['cards']) > 0, players))
    for player in players:
        if len(nonEmptyHands) or len(cards_deck) != 0:
            input(f"Next player: {player}, press enter to clear screen")
            unused = os.system('clear')
            input(f"{player}'s turn, press enter to go!")
        else:
            break
        excluded = list(filter(lambda x: x != player,
                               list(player_dict.keys())))
        while len(player_dict[player]['cards']) != 0 or len(cards_deck) != 0:
            print(f"{player} choose who to ask: {excluded}") if len(
                excluded) > 1 else None
            who = setWho(excluded) if len(excluded) > 1 else excluded[0]

            set_of_cards = set(player_dict[player]['cards']) if len(
                set(player_dict[player]['cards'])) != 0 else getCards(1)
            print("Your cards: ", sorted(player_dict[player]['cards']))
            print(
                f"{player}, choose what to ask {who} for, one of these: {set_of_cards}")
            what = setWhat(set_of_cards)
            asked_hand = player_dict[who]['cards']
            current_player_hand = player_dict[player]['cards']
            if what in asked_hand:
                loop_count = asked_hand.count(what)
                for each in range(0, loop_count):
                    # while what in asked_hand:
                    print("matching card")
                    asked_hand.remove(what)
                    current_player_hand.append(what)
                    player_dict[player]['four_of_a_kind'] = checkHand(
                        player_dict[player])
            elif len(cards_deck) != 0:
                print("go fish")
                random_int = int(random.random() * len(cards_deck))
                card = cards_deck.pop(random_int)
                player_dict[player]['cards'].append(card)
                player_dict[player]['four_of_a_kind'] = checkHand(
                    player_dict[player])
                break
            else:
                print("No cards left in the puddle!")
                break

print(f"Results: ")
for player in player_dict.keys():
    set_of_pairs = player_dict[player]['four_of_a_kind']
    print(f"{player}: {set_of_pairs if len(set_of_pairs) else 0}",
          len(set_of_pairs))
