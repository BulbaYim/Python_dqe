import random
import string
import re


# homework 2 functions:
# return random generated list of dictionaries
def random_list():
    list_of_dict = [
    {random.choice(string.ascii_letters): random.randint(0, 100) for _ in range(random.randint(2, 10))}
        for _ in range(random.randint(2, 10))
    ]
    return list_of_dict


# return common dictionary, created from list
def common_dict(list_of_dict):
    '''convert list of dictionaries to list 
    [ [key0, value0, number_of_dict], ... [keyN, valueN, number_of_dict] ]
    '''
    list_key_value = [[key, value, num_of_dict] for num_of_dict, dict in enumerate(list_of_dict, start=1)
    for key, value in dict.items()
    ]   

    # sort lists to simplify logic of finding max values among similar keys
    list_key_value.sort(key = lambda x: (x[0], x[1]), reverse = True)
    final_dict = {}

    # adding key-values to common dict
    for i in range(len(list_key_value)):
    
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


# return sorted dictionary
def sort_dict(dict):
    dict_keys = list(dict.keys())
    dict_keys.sort()
    return {key: dict[key] for key in dict_keys}


# homework 3 functions:
# return number of whitespaces
def count_whitespaces(text):
    return len([symbol for symbol in text if symbol.isspace()])


# return normalized text
def normalized_text(text):
    text_rows = text.split('\n') # split text and get array of rows
    normalized_sentences = []
    last_words = []

    for row in text_rows:
        if row in ('', ' ') : 
            continue # go to next element of array, if current is empty
        
        # delete '\t', start/end whitespaces, make lower case
        row = row.replace('\t', '').strip().lower()	
        
        # split row in sentences array, add '.', delete start/end whitespaces
        sentences = [
            sentence + '.' if sentence[-1] != ':' else sentence 
                for sentence in row.split('.') if sentence != ''
        ]
        normalized_sentence = ''
        
        for sentence in sentences:
            sentence = sentence.strip().capitalize()
            
            # change 'iz' on 'is'
            sentence = re.sub("\s{1}iz\s{1}", ' is ',  sentence, re.IGNORECASE)
            
            # find the last word of the sentence and add it to last_words array
            for match in re.finditer("\s{1}[A-Za-z0-9_-]+[.]$", sentence, re.IGNORECASE):
                last_word = sentence[match.start() + 1: match.end() - 1]
                last_words.append(last_word)
            normalized_sentence +=  ' ' + sentence

        normalized_sentences.append(normalized_sentence.strip())
    
    last_sentence = ' '.join(last_words)
    normalized_sentences.append(last_sentence.capitalize() + '.')
    final_text = '\n'.join(sentence for sentence in normalized_sentences)
    return final_text