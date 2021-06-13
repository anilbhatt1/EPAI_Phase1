vals  = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def create_deck_normal(vals, suits):
    deck = []
    for suit in suits:
        for val in vals:
            deck.append(val + '-' + suit)
    return deck

deck1 = sorted([val + '-' + suit for val, suit in zip(vals*4, suits*13)])

def winner(hand_1, hand_2):
    hand1 = [card.upper() for card in hand_1]
    hand2 = [card.upper() for card in hand_2]
    hand1_suite, hand1_rank, hand2_suite, hand2_rank = [], [], [], []
    value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    value_suite = {'C': 1, 'D': 2, 'H': 3, 'S': 4}
    rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    value_hand1, value_hand2 = 0, 0
    winner_1, winner_2 = '** Player 1 won !', '** Player 2 won !'

    duplicate_list = ['Dupl' for card in hand1 if card in hand2]

    if len(hand1) != len(hand2):
        return 'Both hands need equal cards'
    elif len(hand1) < 3 or len(hand2) < 3:
        return 'Each hand needs 3, 4 or 5 cards - Less than 3 cards found'
    elif len(hand1) > 5 or len(hand2) > 5:
        return 'Each hand needs 3, 4 or 5 cards - More than 5 cards found'
    elif 'Dupl' in duplicate_list:
        return 'Duplicate cards found in both hands - Only 1 deck is permitted'

    if len(hand1) == len(hand2) and (len(hand1) == 3 or len(hand1) == 4 or len(hand1) == 5):

        for card in hand1:
            suite, rank = card.split('-')
            hand1_suite.append(suite)
            hand1_rank.append(rank)
            value_hand1 += value_dict[rank] + value_suite[suite]
        for card in hand2:
            suite, rank = card.split('-')
            hand2_suite.append(suite)
            hand2_rank.append(rank)
            value_hand2 += value_dict[rank] + value_suite[suite]

        if value_hand1 > value_hand2:
            higher_value_hand = winner_1
        else:
            higher_value_hand = winner_2

        rank_lst_1 = [rank_order.index(rank) for rank in hand1_rank]
        rank_lst_2 = [rank_order.index(rank) for rank in hand2_rank]

        # Hand-1 -> To find all_same_suite. Useful for Royal Flush, Straight Flush and Flush
        i, hand1_all_same_suite = 1, 1
        prev_suite = ''
        for suite in hand1_suite:
            if i == 1:
                pass
            elif prev_suite == suite:
                pass
            else:
                hand1_all_same_suite = 0
                break
            i += 1
            prev_suite = suite

        # Hand-2 -> To find all_same_suite. Useful for Royal Flush, Straight Flush and Flush
        i, hand2_all_same_suite = 1, 1
        prev_suite = ''
        for suite in hand2_suite:
            if i == 1:
                pass
            elif prev_suite == suite:
                pass
            else:
                hand2_all_same_suite = 0
                break
            i += 1
            prev_suite = suite

        # Hand-1 -> Identifying 4-of-kind, Full-House, 3-of-kind
        cnt = 0
        hand1_4_of_kind, hand1_full_house, hand1_3_of_kind = 0, 0, 0
        hand1_rank_temp = sorted(hand1_rank)
        cnt = hand1_rank_temp.count(hand1_rank_temp[0])
        if cnt == 4 or hand1_rank_temp.count(hand1_rank_temp[1]) == 4:
            hand1_4_of_kind = 1
        elif ((len(hand1_rank_temp) == 5 and cnt == 3 and hand1_rank_temp.count(hand1_rank_temp[3]) == 2) or
              (len(hand1_rank_temp) == 5 and cnt == 2 and hand1_rank_temp.count(hand1_rank_temp[2]) == 3)):
            hand1_full_house = 1
        elif cnt == 3 or hand1_rank_temp.count(hand1_rank_temp[1]) == 3 or hand1_rank_temp.count(
                hand1_rank_temp[2]) == 3:
            hand1_3_of_kind = 1

        # Hand 1 -> Identifying 2-pairs, 1-pair
        hand1_2_pair, hand1_1_pair = 0, 0
        if hand1_4_of_kind or hand1_full_house or hand1_3_of_kind:
            pass
        else:
            prev_rank = ''
            i = 1
            for rank in hand1_rank_temp:
                if i == 1:
                    pass
                elif prev_rank == rank and not hand1_1_pair:
                    hand1_1_pair = 1
                elif prev_rank == rank and hand1_1_pair:
                    hand1_2_pair = 1
                i += 1
                prev_rank = rank

        # Hand-2 -> Identifying 4-of-kind, Full-House, 3-of-kind
        cnt = 0
        hand2_4_of_kind, hand2_full_house, hand2_3_of_kind = 0, 0, 0
        hand2_rank_temp = sorted(hand2_rank)
        cnt = hand2_rank_temp.count(hand2_rank_temp[0])
        if cnt == 4 or hand2_rank_temp.count(hand2_rank_temp[1]) == 4:
            hand2_4_of_kind = 1
        elif ((len(hand2_rank_temp) == 5 and cnt == 3 and hand2_rank_temp.count(hand2_rank_temp[3]) == 2) or
              (len(hand2_rank_temp) == 5 and cnt == 2 and hand2_rank_temp.count(hand2_rank_temp[2]) == 3)):
            hand2_full_house = 1
        elif cnt == 3 or hand2_rank_temp.count(hand2_rank_temp[1]) == 3 or hand2_rank_temp.count(
                hand2_rank_temp[2]) == 3:
            hand2_3_of_kind = 1

        # Hand 2 -> Identifying 2-pairs, 1-pair
        hand2_2_pair, hand2_1_pair = 0, 0
        if hand2_4_of_kind or hand2_full_house or hand2_3_of_kind:
            pass
        else:
            prev_rank = ''
            i = 1
            for rank in hand2_rank_temp:
                if i == 1:
                    pass
                elif prev_rank == rank and not hand2_1_pair:
                    hand2_1_pair = 1
                elif prev_rank == rank and hand2_1_pair:
                    hand2_2_pair = 1
                i += 1
                prev_rank = rank

        # Determining winners
        # 1. Check for Royal Flush - Same Suite & A, K, Q, J, 10
        msg = 'Royal Flush '
        if len(hand1) == 5:
            if hand1_all_same_suite and sorted(rank_lst_1) == list(range(8, 13)):
                return msg + winner_1
            elif hand2_all_same_suite and sorted(rank_lst_2) == list(range(8, 13)):
                return msg + winner_2

        # 2. straight flush - Same Suite & rank in sequence
        hand1_sf, hand2_sf = 0, 0
        winner = ''
        msg = 'Straight Flush '
        if hand1_all_same_suite and sorted(rank_lst_1) == list(range(min(rank_lst_1), max(rank_lst_1) + 1)):
            hand1_sf = 1
            winner = winner_1
        if hand2_all_same_suite and sorted(rank_lst_2) == list(range(min(rank_lst_2), max(rank_lst_2) + 1)):
            hand2_sf = 1
            winner = winner_2

        if hand1_sf and hand2_sf:  # Tie
            return msg + higher_value_hand
        elif hand1_sf or hand2_sf:
            return msg + winner

        # 3. Four of a kind
        msg = '4-of-kind '
        if hand1_4_of_kind and hand2_4_of_kind:
            return msg + higher_value_hand
        elif hand1_4_of_kind:
            return msg + winner_1
        elif hand2_4_of_kind:
            return msg + winner_2

        # 4. Full-House
        msg = 'Full-House '
        if hand1_full_house and hand2_full_house:
            return msg + higher_value_hand
        elif hand1_full_house:
            return msg + winner_1
        elif hand2_full_house:
            return msg + winner_2

        # 5. Flush (Same Suite - Any 5 cards)
        msg = 'Flush '
        if hand1_all_same_suite and hand2_all_same_suite:
            return msg + higher_value_hand
        elif hand1_all_same_suite:
            return msg + winner_1
        elif hand2_all_same_suite:
            return msg + winner_2

        # 6. Straight (5 Cards in sequence, any suite)
        hand1_straight, hand2_straight = 0, 0
        winner = ''
        msg = 'Straight '
        if sorted(rank_lst_1) == list(range(min(rank_lst_1), max(rank_lst_1) + 1)):
            hand1_straight = 1
            winner = winner_1
        if sorted(rank_lst_2) == list(range(min(rank_lst_2), max(rank_lst_2) + 1)):
            hand2_straight = 1
            winner = winner_2

        if hand1_straight and hand2_straight:  # Tie
            return msg + higher_value_hand
        elif hand1_straight or hand2_straight:
            return msg + winner

        # 7. 3-of-a-kind (3 of same rank)
        msg = '3-of-a-kind '
        if hand1_3_of_kind and hand2_3_of_kind:
            return msg + higher_value_hand
        elif hand1_3_of_kind:
            return msg + winner_1
        elif hand2_3_of_kind:
            return msg + winner_2

        # 8. 2 Pairs
        msg = '2-pairs '
        if hand1_2_pair and hand2_2_pair:
            return msg + higher_value_hand
        elif hand1_2_pair:
            return msg + winner_1
        elif hand2_2_pair:
            return msg + winner_2

        # 9. 1 pair
        msg = '1-pair '
        if hand1_1_pair and hand2_1_pair:
            return msg + higher_value_hand
        elif hand1_1_pair:
            return msg + winner_1
        elif hand2_1_pair:
            return msg + winner_2

        # 10. High-Card (None of the above)
        return 'High-card ' + higher_value_hand