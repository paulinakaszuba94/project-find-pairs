import re
from collections import defaultdict


class FindPairsToGainSpecificSum:
    """
    Class created to process .txt file with values
    to find pairs that can sum up to a given number.
    """

    def __init__(self, num_to_sum_to: int):
        """
        Specify number of sum that is the target.
        """
        self.num_to_sum_to = num_to_sum_to

    def load_input(self, file_path: str) -> str:
        """
        Load input string from a .txt file.
        """
        try:
            with open(file_path) as f:
                nums_raw = f.read()
                if len(nums_raw) == 0:
                    print("Attention! This file is empty!")

                elif any(character.isalpha() for character in nums_raw):
                    print("Attention! There are letters in the input file!")
                else:
                    return nums_raw

        except IOError:
            print("Incorrect path/ the file not found")

    def preprocess_input(self, nums_raw: str) -> list:
        """
        Take input string and split numbers to a list.
        Then convert values to the integer type.
        Finally, sort numbers and reverse them within the list.
        """
        nums = re.split(r"[-;,.\s]\s*", nums_raw)

        nums = [int(n) for n in nums]
        return nums

    def find_pairs(self, nums: list) -> list:
        """
        Take a list of numbers and find pairs of numbers
        that can sum up to specific >num_to_sum_to< value.
        Each number can be put into a pair only once.
        The first number in a pair should be smaller than the second one.
        """
        # Create an empty list to collect pairs
        pairs = []

        # Store numbers where you don't have a pair yet and count them
        potential_nums_to_match = defaultdict(int)

        for num in nums:

            # Complementary number
            num_to_find = self.num_to_sum_to - num

            # Check how many times complementary number appeared by now
            quantity_of_num_to_find = potential_nums_to_match[num_to_find]
            # Check how many times looped number appeared by now
            quantity_of_num = potential_nums_to_match[num]

            # Complementary number found
            # A pair can be created
            if quantity_of_num_to_find > 0:
                potential_nums_to_match[num_to_find] -= 1
                pairs.append(sorted([num, num_to_find]))

            # Complementary number not found
            # A pair cannot be created yet
            else:
                potential_nums_to_match[num] = quantity_of_num + 1

        return pairs

    def save_result(self, result_to_be_saved: list, file_name: str) -> None:
        """
        Save result as a .txt file.
        """
        with open(file_name, 'w') as f:
            f.write(str(result_to_be_saved))


if __name__ == '__main__':
    sum_12 = FindPairsToGainSpecificSum(12)
    numbers_raw = sum_12.load_input('numbers.txt')
    numbers = sum_12.preprocess_input(numbers_raw)
    result = sum_12.find_pairs(numbers)
    sum_12.save_result(result, 'result.txt')
