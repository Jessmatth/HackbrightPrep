#Welcome and introduction
print("Welcome to two truths and a lie.  You will be asked to evaluate three statements about Jess Matthews.  Your task is to identify the statement that is not true.")  
print()
print("You will get 10 questions.  If you answer 7 or more correctly, you win!")
print()

#Question Set
question_set_1_a = "A. Jess was in a metal band with her older brother. They released their first recording on a cassette tape  called, Deal with the Madness."
question_set_1_b = "B. Jess grew up in a town with a population of 200.  It had a single stop sign and cows out numbered people in the county."
question_set_1_c = "C. Jess has a pet gecko named, Herbert."

question_set_2_a = "A. Jess has owned and worn Jynco jeans."           
question_set_2_b = "B. Jess played in a band with her cousin called, Strawberry Garbage."
question_set_2_c = "C. Jess graduated from college in 4.5 years with a BA and an MA."

question_set_3_a = "A. Jess created a website for hamster enthusiasts called, running down that road."
question_set_3_b = "B. Jess studied abroad in the UK where she got to record the voiceover for a Russian Cosmonaut on ITV news."
question_set_3_c = "C. One of Jess' favorite places is Torrey Pines a natural preserve north of San Diego that is home to the rarest pine trees in north america."

question_set_4_a = "A. Jess began learning to code on sololearn and W3." 
question_set_4_b = "B. Jess' first formal coding class was a 500 level  python for data science course at UC Berkeley." 
question_set_4_c = "C. Jess started COBOL programming as a way to connect with her father."

question_set_5_a = "A. After college Jess' first job was as a best practices resaercher supporting CIOs and CTOs."
question_set_5_b = "B. Other than working for her family, Jess' first job was a snowboard instructor." 
question_set_5_c = "C. Jess' second job was in consulting at Booze Allen."

question_set_6_a = "A. Jess lived in Washington DC."
question_set_6_b = "B. Jess owns a Tesla." 
question_set_6_c = "C. Jess has unlimed access to ice cream."

question_set_7_a = "A. Jess considers herself to be type A."
question_set_7_b = "B. Jess is in an improv troupe." 
question_set_7_c = "C. Jess prefers Sheetz to Wawa."

question_set_8_a = "A. Jess became interested in technology while watching rockets take off from Cape Canavral with her Grandma."
question_set_8_b = "B. Jess helped Jillian Michaels create the 30 Day Shred workout series." 
question_set_8_c = "C. Jess presented to 120 sales leaders in Sydney."

question_set_9_a = "A. Jess has surfed on 6 continents."
question_set_9_b = "B. Jess was an NCAA athlete." 
question_set_9_c = "C. Jess has three patents."

question_set_10_a = "A. Jess was married by the major of San Francisco."
question_set_10_b = "B. Jess worked on Wall Street during college." 
question_set_10_c = "C. Jess has no pets."

question_1 = [question_set_1_a, question_set_1_b, question_set_1_c]
question_2 = [question_set_2_a, question_set_2_b, question_set_2_c]
question_3 = [question_set_3_a, question_set_3_b, question_set_3_c]
question_4 = [question_set_4_a, question_set_4_b, question_set_4_c]
question_5 = [question_set_5_a, question_set_5_b, question_set_5_c]
question_6 = [question_set_6_a, question_set_6_b, question_set_6_c]
question_7 = [question_set_7_a, question_set_7_b, question_set_7_c]
question_8 = [question_set_8_a, question_set_8_b, question_set_8_c]
question_9 = [question_set_9_a, question_set_9_b, question_set_9_c]
question_10 = [question_set_10_a, question_set_10_b, question_set_10_c]

question = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]

i = 0
h = 0
def ask_question(question): 
    global i
    global h
    while i <= len(question):
        if h < 3:
            print(question[i][h])
            print()
            h = h + 1 
        else: 
            i = i + 1    
            h = 0  
            break


answer_key = {
   1: "C",
2:"B",
3:"A",
4:"C",
5:"C",
6:"B",
7:"A",
8:"B",
9:"C",
10:"C" 
}


index = 1
num_correct = 0

while index < 11: 
    print("Which of the following is not true: ")
    ask_question(question)
    answer = input("Please enter A. B. or C. >")
    answer = answer.upper()
    key = answer_key[index]
    if answer == key: 
        print("You are correct!")
        print()
        print("That is not true.")
        num_correct = num_correct + 1
        index = index + 1
        print(f"You now have {num_correct} correct answer(s).")
        print()
    else: 
        print(f"The correct answer was {answer_key[index]}.")
        print()
        index = index + 1     
        print(f"You have {num_correct} correct answers.")
        print("Let's try again.")

if num_correct >= 7: 
    print("Congratulations!  You Win!")
else: 
    print("You needed 7 to win.  Thank you for playing.")