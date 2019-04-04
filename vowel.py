import os,sys
def vowel(filename):
	try:
		list = []        										#Declaring the list of words.
		x= open(filename,"rU")
		y= x.read()     										#reading the text file.
		lines = y.split()   										#here were splitng the words in paragarphs.
		for words in lines:
			if ('a' in words or 'e' in words or 'i' in words or 'o' in words or 'u' in words): 	#compairing words with vowels.
				list.append(words)								#appending the words with vowels.
		print list
		x.close()
	except:
		print "file you entered doesn't exists in the same Directory/folder"
def main():
	vowel(sys.argv[1])
if __name__=='__main__':
	main()
	 
