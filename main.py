import streamlit as st
import string
import random

@st.cache
def load_words():
	with open('words.txt') as file:
		valid_words = set(file.read().split())
	
	words={}
	for word in valid_words:
		words[word]=1

	return words


if __name__ == '__main__':
	st.title("Word Game")
	st.header("Test your vocabulary")
	english_words = load_words()
	count=0
	alphas=list(string.ascii_lowercase)
	upper_alphas=list(string.ascii_uppercase)
	rand=random.randint(0,25)

	label="Enter words starting with alphabet " + alphas[rand] + " or leave blank to quit"
	word="xyz"
	
	while(word!=""):
		word=st.text_input(label,"")

		if word!="" and (word[0]!=alphas[rand] and word[0]!=upper_alphas[rand]):
			st.write("You need to enter word with alphabet", alphas[rand])
		
		elif(english_words.get(word,0)==0):
			st.write("word not found")
		
		else:
			st.write("Keep Going")
			count+=1

	if(count<10):
		st.write("Need to improve")

	if(count>=10 and count<20):
		st.write("That went well, Keep it up")


	if(count>=20 and count<25):
		st.write("Very Good")


	if(count>=25):
		st.write("Brilliant")

    