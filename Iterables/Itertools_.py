# Mostly used Iterterators (range, enumerate, and zip)

# range
print(range(10))  # will generate 0.. 1.. 2.. ... 8.. 9
print(list(range(10)))
print(range(0, 10, 3))  # will generate 0.. 3.. 6.. 9
print(list(range(0, 10, 3)))

# enumerate
print(
    enumerate(["apple", "banana", "cat", "dog"])
)  # will generate (0, 'apple').. (1, 'banana').. (2, 'cat').. (3, 'dog')
print(list(enumerate(["apple", "banana", "cat", "dog"])))

# zip
names = ["Angie", "Brian", "Cassie", "David"]
exam_1_scores = [90, 82, 79, 87]
exam_2_scores = [95, 84, 72, 91]
# will generate ('Angie', 90, 95).. ('Brian', 82, 84).. ('Cassie', 79, 72).. ('David', 87, 91)
print(zip(names, exam_1_scores, exam_2_scores))
print(list(zip(names, exam_1_scores, exam_2_scores)))

# Other usefull iterators

# itertools.chain (Chains together multiple iterables, end-to-end, forming a single iterable)
from itertools import chain

gen_1 = range(0, 5, 2)  # 0.. 2.. 4
gen_2 = (i**2 for i in range(3, 6))  # 9.. 16.. 25
iter_3 = ["moo", "cow"]
iter_4 = "him"
# will generate: 0.. 2.. 4.. 9.. 16.. 25.. 'moo'.. 'cow'.. 'h'.. 'i'.. 'm'
print(chain(gen_1, gen_2, iter_3, iter_4))


# itertools.combinations (Generate all length-n tuples storing “combinations” of items from an iterable)
from itertools import combinations

# will generate: (0, 1, 2).. (0, 1, 3).. (0, 2, 3).. (1, 2, 3)
print(
    combinations([0, 1, 2, 3], 3)
)  # generate all length-3 combinations from [0, 1, 2, 3]
