import re


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
        output = []

        # Store numbers where you don't have a pair yet and count them
        candidates = {}

        for num in nums:

            # No complementary number yet
            # Looped number appears for the first time
            if ((self.num_to_sum_to - num) not in candidates) \
                    and (num not in candidates):

                candidates[num] = 1

            # No complementary number yet
            # Looped number appears NOT for the first time
            elif ((self.num_to_sum_to - num) not in candidates) \
                    and (num in candidates):

                candidates[num] += 1

            # Complementary number found, but value = 0
            elif ((self.num_to_sum_to - num) in candidates) \
                    and (candidates[(self.num_to_sum_to - num)] == 0):

                # Looped number appears for the first time
                if num not in candidates:
                    candidates[num] = 1
                # Looped number appears NOT for the first time
                elif num in candidates:
                    candidates[num] += 1

            # Complementary number found and value > 0
            elif ((self.num_to_sum_to - num) in candidates) \
                    and (candidates[(self.num_to_sum_to - num)] > 0):

                temp = []
                temp.append(num)
                temp.append((self.num_to_sum_to - num))
                candidates[(self.num_to_sum_to - num)] -= 1
                pair = [min(temp), max(temp)]
                output.append(pair)

        return output

    def find_pairs_old(self, nums: list) -> list:
        """
        Take a list of numbers and find pairs of numbers
        that can sum up to specific >sum_num< value.
        Each number can be put into a pair only once.
        The first number in a pair should be smaller than the second one.
        """
        output = []
        skip_index = []

        for i in range(len(nums) - 1, -1, -1):
            if (i >= 1) & (i not in skip_index):
                num_1 = nums[i]
                for j in range(len(nums) - 2, -1, -1):
                    if j not in skip_index:
                        if num_1 + nums[j] == self.num_to_sum_to:
                            num_2 = nums[j]
                        else:
                            num_2 = None
                        if num_2:
                            pair = [num_1, num_2]
                            skip_index.append(i)
                            skip_index.append(j)
                            output.append(pair)
                            break

        return output

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
