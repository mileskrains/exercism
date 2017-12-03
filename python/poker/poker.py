from collections import defaultdict

def rank_and_suit_dicts(hand):
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    rank_val_dict = dict(zip(ranks, range(13)))
    rbs = defaultdict(list)
    sbr = defaultdict(list)
    for card in hand:
        rank, suit = rank_val_dict[card[:-1]], card[-1]
        rbs[suit].append(rank)
        sbr[rank].append(suit)
    return rbs, sbr


def is_sequential(ranklist):
    return max(ranklist) - min(ranklist) == len(ranklist) - 1


def score(hand):
    rbs, sbr = rank_and_suit_dicts(hand)
    suit_counts = sorted(map(len,rbs.values()))
    rank_counts = sorted(map(len,sbr.values()))
    kicker = 0
    # straight flush?
    if suit_counts == [5] and is_sequential(list(sbr.keys())):
        hand_score = 9
        rank = max(sbr.keys())
    # four of a kind?
    elif rank_counts == [1, 4]:
        hand_score = 8
        rank = [k for k, v in sbr.items() if len(v) == 4][0]
        kicker = [k for k, v in sbr.items() if len(v) == 1][0]
    # full house?
    elif rank_counts == [2, 3]:
        hand_score = 7
        triplet_score = [k for k, v in sbr.items() if len(v) == 3][0]
        pair_score = [k for k, v in sbr.items() if len(v) == 2][0]
        rank = 13 * triplet_score + pair_score
    # flush?
    elif suit_counts == [5]:
        hand_score = 6
        rank = max(sbr.keys())
    # straight?
    elif is_sequential(sbr.keys()):
        hand_score = 5
        rank = max(sbr.keys())
    # three of a kind?
    elif rank_counts == [1, 1, 3]:
        hand_score = 4
        rank = [k for k, v in sbr.items() if len(v) == 3][0]
        kicker = max([k for k, v in sbr.items() if len(v) == 1])
    # two pair?
    elif rank_counts == [1, 2, 2]:
        hand_score = 3
        pair_scores = [k for k, v in sbr.items() if len(v) == 2]
        rank = max(pair_scores)
        low_pair_score = min(pair_scores)
        single_card_score = [k for k, v in sbr.items() if len(v) == 1][0]
        kicker = 13 * low_pair_score + single_card_score
    # pair?
    elif rank_counts == [1, 1, 1, 2]:
        hand_score = 2
        rank = [k for k, v in sbr.items() if len(v) == 2][0]
        k3, k2, k1 = sorted([k for k, v in sbr.items() if len(v) == 1])
        kicker = (13**2 * k1) + (13 * k2) + k3
    # high card
    else:
        hand_score = 1
        k4, k3, k2, k1, high = sorted(sbr.keys())
        rank = high
        kicker = (13**3 * k1) + (13**2 * k2) + (13 * k3) + k4
    return hand_score, rank, kicker


def poker(hands):
    scored_hands = sorted([(score(hand), hand) for hand in hands])
    return [hand
            for score, hand in scored_hands
            if score == scored_hands[-1][0]]
