from tokenize import run_tokenizer
from interpreter import interper

filename= input ("Geef de naaam en/of path van uw source file:" )
mylist=run_tokenizer(filename)
interper(mylist)