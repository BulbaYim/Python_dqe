from hw_04.functions_hw_02 import random_list, common_dict, sort_dict
from hw_04.functions_hw_03 import count_whitespaces, normalized_text


def main():
    print('HOMEWORK 2:')

    # call random_list() to get list with random dicts
    list_of_dict = random_list()
    print(f'Generated list:\n{list_of_dict}\n')

    # call common_dict() to get common dictionary, created from list
    final_dict = common_dict(list_of_dict)

    # call sort_dict() to get sorted dictionary
    print(f'Common dictionary:\n{sort_dict(final_dict)}\n')
    print('HOMEWORK 3:')

    with open('input_data/text.txt', 'r', encoding="utf-8") as file:
        text = file.read()

    # call count_whitespaces() to get number of whitespaces
    print(f'The number of whitespaces in non-normalized text is {count_whitespaces(text)}.')

    # call normalized_text() to get normalized text
    print(normalized_text(text))


if __name__ == "__main__":
    main()