##### Harris McCullers - 2019 #####

sexismSemantics/Photos:
	A folder containing several subfolders with photo examples of word clouds

sexismSemantics/Models:
	A folder containing all of the saved model binaries for later use

sexismSemantics/Text:
	A folder containing all of the text samples used to train the models

sexismSemantics/books:
	A folder specifically containing books for training models

sexismSemantics/etc:
	A folder containing other useful files

sexismSemantics/w2v.py:
	The python program used to create the models
	Usage:
		> python3 w2v.py [sample.txt] [output.bin]

sexismSemantics/insights.py:
	The python program used to create the word clouds
	Usage:
	First, set the lists at the top of the file s.t.
		WORDS - contains all highlighted words
		MALE_WORDS - all of the words in WORDS that are male
		FEMALE_WORDS - all of the words in WORDS that are female
	Then, use the command line
		>python3 insights.py
		>Enter filename of model: [path_to_model.bin]
