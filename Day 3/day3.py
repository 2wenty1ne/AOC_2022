def prioritie_value(letter):
    priority = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter.isupper():
        priority = priority + 26
    return priority + alphabet.index(letter.lower()) + 1

def split_backpack(backpack):
    backpack_size = len(backpack)
    backpack_size_half = int(backpack_size/2)
    first_compartment = backpack[:backpack_size_half]
    second_compartment = backpack[backpack_size_half:]
    return first_compartment, second_compartment


with open("data.txt", "r") as data:
    backpack_list = [x.strip() for x in data.readlines()]


# Round 1
priority_sum: int = 0
item_in_both_backbacks = str()

for backpack in backpack_list:
    first_compartment, second_compartment = split_backpack(backpack)

    for item in first_compartment:
        if item in second_compartment:
            item_in_both_backbacks = item
            break
    item_priority = prioritie_value(item_in_both_backbacks)
    priority_sum = priority_sum + item_priority


# Round 2
group_index:int = 0
single_group = list()
group_badge = str()
priority_badge_sum:int = 0
items = list()

for backpack in backpack_list:
    single_group.append(backpack)
    if (group_index + 1) % 3 == 0 and group_index:
        for item in single_group[0]:
            if item in single_group[1] and item in single_group[2]:
                break
        items.append(item)
        priority_badge_sum = priority_badge_sum + prioritie_value(item)
        single_group = []
    group_index = group_index + 1


print(f'Priority sum of all backpacks: {priority_sum}')
print(f'Priority sum of all group badges: {priority_badge_sum}')