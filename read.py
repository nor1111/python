word_list = []
filename_word = 'word.txt'
with open(filename_word,'r') as file_object_word:
	for word in file_object_word.readlines():
		word_list.append(word.strip())

chinese_list = []
filename_chinese = 'chinese.txt'
with open(filename_chinese,'r') as file_object_chinese:
	for chinese in file_object_chinese.readlines():
		chinese_list.append(chinese.strip())

	
	
	
	

