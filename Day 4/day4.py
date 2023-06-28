def find_higher_int(int_comp: int, int_test: int) -> int:
    if int_comp > int_test:
        return "comp"
    elif int_comp == int_test:
        return "equal"
    elif int_comp < int_test:
        return "test"


with open("data.txt", "r") as data:
    pairs = [x.strip() for x in data.readlines()]

contained_assigments:int = 0

for pair in pairs:
    assignment_compare, assignment_test = pair.split(",")
    assignment_compare_start, assignment_compare_end = assignment_compare.split("-")
    assignment_test_start, assignment_test_end = assignment_test.split("-")

    #? Comparison if either start or end are euqal
    if find_higher_int(assignment_compare_start, assignment_test_start) == "equal":
        contained_assigments = contained_assigments + 1
        print(f'Equal,  Start comp:{assignment_compare_start}, Start test: {assignment_test_start}')
        continue
    elif find_higher_int(assignment_compare_end, assignment_test_end) == "equal":
        contained_assigments = contained_assigments + 1
        print(f'Equal,  End comp:{assignment_compare_end}, End test: {assignment_test_end}')
        continue

    #? Comparison if comp start > test start
    elif find_higher_int(assignment_compare_start, assignment_test_start) == "comp":
        # start first
        if find_higher_int(assignment_compare_end, assignment_test_end) == "comp":
            # start first - end first -> No
            continue
        elif find_higher_int(assignment_compare_end, assignment_test_end) == "test":
            # start first - end second -> Yes
            contained_assigments = contained_assigments + 1
            continue

    #? Comparison if comp start < test start
    elif find_higher_int(assignment_compare_start, assignment_test_start) == "test":
        #start second
        if find_higher_int(assignment_compare_end, assignment_test_end) == "comp":
            #start second - end first -> Yes
            contained_assigments = contained_assigments + 1
            continue
        if find_higher_int(assignment_compare_end, assignment_test_end) == "test":
            #start second - end second -> No
            continue

print(f"Number of fully contained assigments: {contained_assigments}")