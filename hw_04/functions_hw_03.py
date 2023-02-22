import re


def count_whitespaces(text):
    ''' return number of whitespaces '''
    return len([symbol for symbol in text if symbol.isspace()])


def normalized_text(text):
    ''' return normalized text '''
    text_rows = text.split('\n')  # split text and get array of rows
    normalized_sentences = []
    last_words = []

    for row in text_rows:
        if row in ('', ' '):
            continue  # go to next element of array, if current is empty

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
            sentence = re.sub(r"\s{1}iz\s{1}", ' is ',  sentence, re.IGNORECASE)

            # find the last word of the sentence and add it to last_words array
            for match in re.finditer(r"\s{1}[A-Za-z0-9_-]+[.]$", sentence, re.IGNORECASE):
                last_word = sentence[match.start() + 1: match.end() - 1]
                last_words.append(last_word)
            normalized_sentence += ' ' + sentence

        normalized_sentences.append(normalized_sentence.strip())

    last_sentence = ' '.join(last_words)
    normalized_sentences.append(last_sentence.capitalize() + '.')
    final_text = '\n'.join(normalized_sentences)
    return final_text