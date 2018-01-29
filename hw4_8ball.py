#We're making a magic 8-ball game!

# check_question
question = input("Ask me a question and I will tell you your future: ")
while True:
	if question[-1] != "?":
		print("I'm sorry, I can only answer questions.")
		question = input("Ask me a question and I will tell you your future: ")
	else:
		break