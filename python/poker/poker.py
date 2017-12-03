from collections import Counter
from operator import itemgetter


def rank_and_suit_analysis(hand):
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    rank_val_dict = dict(zip(ranks, range(2, 15)))
    suit_counts = list(Counter([card[-1] for card in hand]).values())
    ranks_counter = Counter([rank_val_dict[card[:-1]] for card in hand])
    ranks_mc = sorted(ranks_counter.most_common(),
                      key=itemgetter(1, 0), reverse=True)
    rank_counts = [c for r, c in ranks_mc]
    ranks_for_counts = [r for r, c in ranks_mc]
    return suit_counts, rank_counts, ranks_for_counts


def is_sequential(ranklist):
    return sorted(ranklist) == list(range(min(ranklist), max(ranklist)+1))


def score(hand):
    suit_counts, rank_counts, ranks_for_counts = rank_and_suit_analysis(hand)
    if suit_counts == [5] and is_sequential(ranks_for_counts):
        hand_score = 9  # straight flush
    elif rank_counts == [4, 1]:
        hand_score = 8  # four of a kind
    elif rank_counts == [3, 2]:
        hand_score = 7  # full house
    elif suit_counts == [5]:
        hand_score = 6  # flush
    elif is_sequential(ranks_for_counts):
        hand_score = 5  # straight
    elif rank_counts == [3, 1, 1]:
        hand_score = 4  # three of a kind
    elif rank_counts == [2, 2, 1]:
        hand_score = 3  # two pair
    elif rank_counts == [2, 1, 1, 1]:
        hand_score = 2  # pair
    else:
        hand_score = 1  # high card
    return hand_score, ranks_for_counts


def poker(hands):
    scored_hands = sorted([(score(hand), hand) for hand in hands])
    max_score = scored_hands[-1][0]
    return [hand
            for score, hand in scored_hands
            if score == max_score]
