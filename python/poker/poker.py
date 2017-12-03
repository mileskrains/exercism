from collections import defaultdict

def rank_and_suit_analysis(hand):
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    rank_val_dict = dict(zip(ranks, range(2, 15)))
    rbs = defaultdict(list)
    sbr = defaultdict(list)
    for card in hand:
        rank, suit = rank_val_dict[card[:-1]], card[-1]
        rbs[suit].append(rank)
        sbr[rank].append(suit)
    suit_counts = list(map(len,rbs.values()))
    rank_counts = sorted(map(len,sbr.values()), reverse=True)
    counts_of_ranks = [(len(v), k) for k, v in sbr.items()]
    ranks_for_counts = [r for c, r in sorted(counts_of_ranks, reverse=True)]
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
