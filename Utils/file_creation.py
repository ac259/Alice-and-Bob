def file_creation():
	Kb_num_of_chars = 1024
	Mb_num_of_chars = 1024*1024

	# Generate two files- of size 1MB and 1KB -filled with 0's
	with open("test_size_1mb",'wb') as f:
		f.write('0'*Mb_num_of_chars)
	with open("test_size_1kb",'wb') as f:
		f.write('0'*Kb_num_of_chars)

file_creation()