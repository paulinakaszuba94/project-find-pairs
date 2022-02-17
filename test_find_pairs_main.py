import find_pairs_main as main


def test_load_empty_input(capsys):
    """
    Check the function behaviour
    when a file put as the argument is empty.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_12.load_input('test_cases/empty.txt')
    out, err = capsys.readouterr()
    assert out == "Attention! This file is empty!\n"


def test_load_input_with_letters(capsys):
    """
    Check the function behaviour
    when a file put as the argument contains letters.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_12.load_input('test_cases/letters.txt')
    out, err = capsys.readouterr()
    assert out == "Attention! There are letters in the input file!\n"


def test_load_unavailable_input(capsys):
    """
    Check the function behaviour
    when a file put as the argument doesn't exist.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_12.load_input('no_file.txt')
    out, err = capsys.readouterr()
    assert out == "Incorrect path/ the file not found\n"


def test_preprocess_input_diff_sep(capsys):
    """
    Check the function behaviour
    when a file put as the argument contains different separators.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_string = test_12.load_input('test_cases/numbers_diff_sep.txt')
    preprocessed_test_list = test_12.preprocess_input(test_string)
    out = test_12.find_pairs(preprocessed_test_list)
    assert sorted(out) == sorted([[0, 12], [0, 12], [1, 11], [4, 8], [4, 8]])


def test_find_pairs_no_pair():
    """
    Check the function behaviour when in the input is no valid pair.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_string = "1, 1, 1, 1, 1"
    preprocessed_test_list = test_12.preprocess_input(test_string)
    out = test_12.find_pairs(preprocessed_test_list)
    assert out == []


def test_find_pairs_one_input_number():
    """
    Check the function behaviour when in the input is only one number.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_string = "12"
    preprocessed_test_list = test_12.preprocess_input(test_string)
    out = test_12.find_pairs(preprocessed_test_list)
    assert out == []


def test_find_pairs_one_input_num():
    """
    Check the function behaviour when in the input is only one number.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_string = "12"
    preprocessed_test_list = test_12.preprocess_input(test_string)
    out = test_12.find_pairs(preprocessed_test_list)
    assert out == []


def test_find_pairs_normal_scenario():
    """
    Check the function behaviour when we have normal scenario.
    """
    test_12 = main.FindPairsToGainSpecificSum(12)
    test_string = "0, 0, 1, 2, 3, 4, 5, 2, 1, 2, 10, 11, 12, 1, 1, 1"
    preprocessed_test_list = test_12.preprocess_input(test_string)
    out = test_12.find_pairs(preprocessed_test_list)
    assert sorted(out) == sorted([[0, 12], [1, 11], [2, 10]])
