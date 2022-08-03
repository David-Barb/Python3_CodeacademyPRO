#Magic 8-ball exercise from "Control Flow section":
import random

answer_one = "Yes - definitely."
answer_two = "It is decidedly so."
answer_three = "Without a doubt."
answer_four = "Reply hazy, try again."
answer_five = "Ask again later."
answer_six = "Better not tell you now."
answer_seven = "My sources say no."
answer_eight = "Outlook not so good."
answer_nine = "Very doubtful."

name = "David"
question = "Are you dumb?"
random_number = random.randint(1,9)
#print(random_number)

if name == "": print("Question: "+question)
elif question == "": print("No questions inserted.")
else:  print(name+" asks: "+question)

if random_number == 1: answer = answer_one
elif random_number == 2: answer = answer_two
elif random_number == 3: answer = answer_three
elif random_number == 4: answer = answer_four
elif random_number == 5: answer = answer_five
elif random_number == 6: answer = answer_six
elif random_number == 7: answer = answer_seven
elif random_number == 8: answer = answer_eight
elif random_number == 9: answer = answer_nine
else: answer = "Error"

if question != "": print("Magic 8-ball's answer: "+answer)