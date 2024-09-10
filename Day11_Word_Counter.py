def text_count(text):
    word=text.split()  # text.split function to split each word based on spaces
    return len(word)   #return length of list of words

sentence=input("Enter the sentence: ")
word_count=text_count(sentence)    #called the function
print(f"The number of words in a given sentence is:  {word_count}")