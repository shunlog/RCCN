grammar=Grammar.g4
input=input.txt
preprocessed_input=preprocessed.txt
pypreprocess=./preprocess.py

PHONY: show_tree antlr_generate

$(preprocessed_input): $(input) $(pypreprocess)
	 $(pypreprocess) < $(input) > $(preprocessed_input)

show_tree:
	antlr4-parse $(grammar) document -gui $(preprocessed_input)

antlr_generate:
	antlr4 -Dlanguage=Python3 -o build $(grammar)
