import sys
import re
import os

def index_text_file(txt_filename, idx_filename,
    delimiter_chars=",.;:!?"):
		txt_fil = open(txt_filename, "r")

		word_occurrences = dict()
		line_num = 0

		for lin in txt_fil:
			print(lin)
			line_num += 1
            # Split the line into words delimited by whitespace.
            #words = lin.split()
			words=re.findall('F...',lin)
            # Remove unwanted delimiter characters adjoining words.
			words2 = [ word.strip(delimiter_chars) for word in words ]
            # Find and save the occurrences of each word in the line.
			for word in words2:
				if word in word_occurrences:
					word_occurrences[word].append(line_num)
				else:
					word_occurrences[word] = [ line_num ]


		if (line_num < 1):
			print("No lines found in text file, no index file created.")
			txt_fil.close()
			sys.exit(0)

        # Display results.
		word_keys=list()
		word_keys = list(word_occurrences.keys())
		print(word_keys)
        #print "{} unique words found.".format(len(word_keys))
		#word_keys = word_occurrences.keys()

        # Sort the words in the word_keys list.
		word_keys.sort()

        # Create the index file.
		idx_fil = open(idx_filename, "w")

		for word in word_keys:
			line_nums = word_occurrences[word]
			idx_fil.write(word + " ")
			for line_num in line_nums:
				idx_fil.write(str(line_num) + " ")
			idx_fil.write("\n")

		txt_fil.close()
		idx_fil.close()


txt_filename="hashcontent.txt"
txt_indexname="indexfile.txt"
index_text_file(txt_filename,txt_indexname)
