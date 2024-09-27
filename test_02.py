"""
Find the Common Elements in Two Arrays

New code challenge! This is a great way to practice your coding skills and get feedback from the community. 
We will post a new challenge roughly every 2 days. Good luck!

Description
Write a function called 'commonElements' that takes two arrays as arguments and returns an array of common 
elements between the two input arrays.

Rules
You must post your code in the code challenge channel
The function should return an empty array if there are no common elements.
The input arrays can contain numbers or strings.

Example
commonElements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) => [4, 5]
"""


def common_elements(l1: list[int], l2: list[int]) -> list[int]:
    l1_set = set(l1)
    l2_set = set(l2)
    res = list(l1_set.intersection(l2_set))
    return res


def common_elements_02(l1: list[int], l2: list[int]) -> list[int]:
    local_array = []
    for val in l1:
        if val in l1 and val in l2:
            local_array.append(val)
    return local_array


def main() -> None:
    val = common_elements_02([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    print(val)
    # OUTPUT: [4, 5]
    my_dict = dict()
    my_dict.items()


if __name__ == '__main__':
    main()
