import sort
import random


def make_arr():
    random_array = [int(random.random() * 100) for _ in range(30)]
    return random_array


arr = make_arr()

sorted_arr = sort.merge_sort(arr)

print(sorted_arr)
print("==============")

sorted_arr2 = sort.quick_sort(arr)
