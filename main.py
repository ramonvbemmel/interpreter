from tokenize import run_tokenizer
from interpreter import interper, evaluate_loop_statement

filename= input ("Geef de naaam en/of path van uw source file:" )
mylist=run_tokenizer("voorbeeld.txt")
interper(mylist)
print("Loop statement ", evaluate_loop_statement.counter, "times evaluated")