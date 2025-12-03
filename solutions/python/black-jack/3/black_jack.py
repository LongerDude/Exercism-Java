def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.
    
    'J', 'Q', 'K' = 10,
    'A' = 1,
    '2' - '10' = numerical value.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.
    :return: str or tuple - resulting tuple contains both cards if they are of equal value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return (card_one, card_two)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the upcoming ace card.

    :param card_one, card_two: str - card dealt.
    :return: int - either 1 or 11 as the value for the upcoming ace card.
    
    When an ace is already in hand (either card is 'A'), the new ace should be valued as 1.
    Otherwise, if the sum of card values plus 11 does not bust (i.e. <= 21), choose 11; if it would bust, choose 1.
    """
    # If the hand already contains an ace, the new ace must be 1.
    if card_one == 'A' or card_two == 'A':
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)
    if total + 11 <= 21:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' blackjack.

    :param card_one, card_two: str - cards dealt.
    :return: bool - whether the hand is a blackjack (two cards worth 21).
    
    Only a combination of an ace and a ten-value card constitutes blackjack.
    """
    return ((card_one == 'A' and value_of_card(card_two) == 10) or
            (card_two == 'A' and value_of_card(card_one) == 10))

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - whether the hand can be split into two pairs
                   (i.e. both cards have the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - whether the hand can be doubled down
                   (i.e. total is either 9, 10, or 11 points).
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
