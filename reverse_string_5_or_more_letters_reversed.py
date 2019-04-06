def spin_words(sentence):
    # Your code goes here

    new_sen = sentence.split(" ")

    for i,ele in enumerate(new_sen):

    	if len(ele)>=5:
    		new_sen[i]=ele[::-1]

    new_sen_reversed = " ".join(new_sen)

    print(new_sen_reversed)
    return None


spin_words("Hey fellow warriors")