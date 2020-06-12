from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk import RegexpParser
tokenizer = RegexpTokenizer(r'\w+')
userInput = "The first rule of fight club is: we don't talk about fight club."
filtered_text=tokenizer.tokenize(userInput)
tokens_tag = pos_tag(filtered_text)
print("Filtered text:", filtered_text)
print("Tagged text:", tokens_tag)