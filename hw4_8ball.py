#We're making a magic 8-ball game!

# check_question
# question = input("Ask me a question and I will tell you your future: ")
while True:
	question = input("Ask me a question and I will tell you your future: ")
	if question[-1] != "?":
		print("I'm sorry, I can only answer questions.")
	else:
		break