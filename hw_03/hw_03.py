import re


text = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

whitespaces_number = len([symbol for symbol in text if symbol.isspace()])
print(f'The number of whitespaces in non-normalized text is {whitespaces_number}.')

text_rows = text.split('\n') # split text and get array of rows
normalized_sentences = []
last_words = []

for row in text_rows:
	if row in ('', ' ') : continue # go to next element of array, if current is empty
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
			last_words.append(sentence[match.start() + 1: match.end() - 1])
		normalized_sentence +=  ' ' + sentence
	normalized_sentences.append(normalized_sentence.strip())
 
last_sentence = ' '.join(word for word in last_words)
normalized_sentences.append(last_sentence.capitalize() + '.')
finall_text = '\n'.join(sentence for sentence in normalized_sentences)
print(finall_text)