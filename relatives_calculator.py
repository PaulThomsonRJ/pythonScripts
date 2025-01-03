user_distance = int(input("Please enter the distance between you and your most common direct ancestor: "))
relative_distance = int(input("Please enter the distance between your relative and their most common direct ancestor: "))
message = "You are "

smaller_gap = min(user_distance, relative_distance)
larger_gap = max(user_distance, relative_distance)
difference = larger_gap - smaller_gap


if smaller_gap == 0:
    if larger_gap == 0:
        message += "you and you"
    else:
        greats_and_grands = "great " * max(0, (difference - 2)) + "grand" * max(0, (difference - 1))
        message += greats_and_grands + "mother/father and son/daughter"

if smaller_gap == 1:
    if larger_gap == 1:
        message += "siblings"
    else:
        message += "great " * (difference-1) + "aunt/uncle and niece/nephew"

if smaller_gap >= 2:
    cousin_gap = smaller_gap - 1
    cousin_gap_str = str(cousin_gap)
    cousin_gap_str += "st" if cousin_gap == 1 else "nd" if cousin_gap == 2 else "th"
    removal = str(difference) + " time(s) removed" if difference > 0 else ""
    message += cousin_gap_str + " cousins " + removal

if smaller_gap < 0:
    message = "That doesn't make sense to me"

print(message)