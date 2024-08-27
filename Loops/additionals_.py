# break, continue, & else clauses on loops


# breaking out of a loop early
for item in [1, 2, 3, 4, 5]:
    if item == 3:
        print(item, " ...break!")
        break
    print(item, " ...next iteration")


# including an else-clause at the end of the loop
for item in [2, 4, 6]:
    if item == 3:
        print(item, " ...break!")
        break
    print(item, " ...next iteration")
else:
    print("if you are reading this, then the loop completed without a 'break'")


# demonstrating a `continue` statement in a loop
x = 1
while x < 4:
    print("x = ", x, ">> enter loop-body <<")
    if x == 2:
        print("x = ", x, " continue...back to the top of the loop!")
        x += 1
        continue
    x += 1
    print("--reached end of loop-body--")
