with open("data.txt", "r") as data:
    calories_list_with_newline = data.read().split("\n\n")

calories_list = []

for i in calories_list_with_newline:
    calories_per_elf_string = i.split("\n")
    calories_per_elf = [int(x) for x in calories_per_elf_string]
    calories_sum_per_elf = sum(calories_per_elf)
    calories_list.append(calories_sum_per_elf)

highest_calorie_sum = max(calories_list)
#print(f'Highest sum of Calories: {highest_calorie_sum}')

calories_list.sort(reverse=True)
top3_calories_sum = calories_list[0] + calories_list[1] + calories_list[2]
print(f'Highest sum of top three Calories: {top3_calories_sum}')