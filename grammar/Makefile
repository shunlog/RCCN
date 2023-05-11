grammar=Grammar.g4
input=input.txt
preprocessed_input=preprocessed.txt
pypreprocess=./preprocess.py

PHONY: show_tree antlr_generate

show_tree:
	antlr4-parse $(grammar) document -gui $(input)

antlr_generate:
	antlr4 -Dlanguage=Python3 -o build $(grammar)
