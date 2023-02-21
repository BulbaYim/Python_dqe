from hw_04.hw_04 import *


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

    text = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''
    
    # call count_whitespaces() to get number of whitespaces
    print(f'The number of whitespaces in non-normalized text is {count_whitespaces(text)}.')
    
    # call normalized_text() to get normalized text
    print(normalized_text(text))


if __name__ == "__main__":
    main()