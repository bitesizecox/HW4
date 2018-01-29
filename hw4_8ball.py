#We're making a magic 8-ball game!

# check_question
# question = input("Ask me a question and I will tell you your future: ")
while True:
	question = input("Ask me a question and I will tell you your future: ")
	if question[-1] != "?":
		print("I'm sorry, I can only answer questions.")
	else:
		break
answer_list_A = ["It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes"]
# Person C, Yuanting Lin, adds the last 10 answers. 
answers = ["Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good"]

answer = random.choice(answers)
print(answer)
