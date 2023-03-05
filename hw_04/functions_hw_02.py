import random
import string


def random_list():
    ''' return random generated list of dictionaries '''
    list_of_dict = [
        {random.choice(string.ascii_letters): random.randint(0, 100)
            for _ in range(random.randint(2, 10))}
        for _ in range(random.randint(2, 10))
    ]
    return list_of_dict


# return common dictionary, created from list
def common_dict(list_of_dict):
    '''convert list of dictionaries to list 
    [ [key0, value0, number_of_dict], ... [keyN, valueN, number_of_dict] ]
    '''
    list_key_value = [
        [key, value, num_of_dict] for num_of_dict, dictionary in enumerate(list_of_dict, start=1)
            for key, value in dictionary.items()
    ]

    # sort lists to simplify logic of finding max values among similar keys
    list_key_value.sort(key=lambda x: (x[0], x[1]), reverse=True)
    final_dict = {}

    # adding key-values to common dict
    for i, _ in enumerate(list_key_value):

        # check for the last element
        if i == len(list_key_value) - 1:
            if list_key_value[i][0] != list_key_value[i-1][0]:
                final_dict[list_key_value[i][0]] = list_key_value[i][1]

        # if previous key != current key and next key != current key, then there are no similar keys
        elif list_key_value[i][0] != list_key_value[i+1][0] and \
                list_key_value[i][0] != list_key_value[i-1][0]:
            final_dict[list_key_value[i][0]] = list_key_value[i][1]

        # if previous key != current key and next key == current key, then current element has similar keys
        elif list_key_value[i][0] == list_key_value[i+1][0] and \
            list_key_value[i][0] != list_key_value[i-1][0]:
            serial_number = f'{list_key_value[i][0]}_{list_key_value[i][2]}'
            final_dict[serial_number] = list_key_value[i][1]

    return final_dict


def sort_dict(dictionary):
    ''' return sorted dictionary '''
    dict_keys = list(dictionary.keys())
    dict_keys.sort()
    return {key: dictionary[key] for key in dict_keys}