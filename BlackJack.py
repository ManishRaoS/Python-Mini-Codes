def get_hand_value(*args):
    total = sum(args)
    if total <= 21:
        if total == 21 and len(args) == 2:
            return "Winner Winner Chicken Dinner!"
        return "The value of your hand is {}".format(total)
    if total > 21:
        if 11 in args:
            total = sum(1 if x == 11 else x for x in args)
            if total <= 21:
                return "The value of your hand is {}".format(total)
        return "Busted!"

# hand_1 = get_hand_value(4,4,4,4)
# hand_2 = get_hand_value(11,10)
# hand_3 = get_hand_value(11,5,6,4,11,4)
# hand_4 = get_hand_value(11,5,6,10)
# hand_5 = get_hand_value(10,5,7)
# hand_6 = get_hand_value(5,6,5,10)
# hand_7 = get_hand_value(10,11)
# hand_8 = get_hand_value(11,11,11,11,10,10)
# hand_9 = get_hand_value(5,6,5,5)