import random

capitals={"Andhra Pradesh": "Hyderabad","Arunachal Pradesh" : "Itanagar","Assam" : "Dispur","Bihar": "Patna","Goa" : "Panaji","Gujarat" : "Gandhinagar","Haryana" : "Chandigarh","Himachal Pradesh" : "Shimla","Jammu & Kashmir" : "Srinagar","Karnataka" : "Bangaluru","Kerala" : "Thiruvananthapuram","Madhya Pradesh" : "Bhopal","Maharashtra" : "Mumbai","Manipur" : "Imphal","Meghalaya" : "Shillong","Mizoram": "Aizawl","Nagaland" : "Kohima","Orissa" : "Bhubaneswar","Punjab" : "Chandigarh","Rajasthan" : "Jaipur","Sikkim" : "Gangtok","Tamil Nadu" : "Chennai","Tripura" : "Agartala","Uttar Pradesh" : "Lucknow","West Bengal" : "Kolkata","Chhattisgarh" : "Raipur","Uttarakhand" : "Dehradun","Jharkhand" : "Ranchi","Telangana" : "Hyderabad","Delhi" : "New Delhi" ,"Andaman & Nicobar Islands" : "Port Blair","Chandigarh" : "Chandigarh","Dadra & Nagar Haveli" : "Silvasa","Daman & Diu" : "Daman","Lakshadweep" : "Kavaratti","Puducherry" : "Puducherry"}

#Generate 35 quiz files:

for quizNum in range(36):
	quizFile=open('capitalsquiz%s.txt' %(quizNum+1), 'w')
	answerKeyFile=open('capitalsquiz_answer%s.txt' %(quizNum+1), 'w')

	#Write out the header for the quiz
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' '*20)+ ' State Capital Quiz (Form %s)' %(quizNum+1))
	quizFile.write('\n\n')

	#Shuffle the order of the states
	states=list(capitals.keys())
	random.shuffle(states)
	

	#Loop through all 50 states, making a question for each.
	for questionNum in range(36):
		correctAnswer=capitals[states[questionNum]]
		wrongAnswers=list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers=random.sample(wrongAnswers,3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		# Write the question and the answer options to the quiz file.
		quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
			quizFile.write('\n')
			# Write the answer key to a file.

		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

	quizFile.close()
	answerKeyFile.close()

