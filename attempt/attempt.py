#Ask the User a question like "Who is PM of India?"

#Track in how many attempts the user answers.

#Give hints based on how many guesses the user makes.

question="who is Pm of india?"
attempt=0

while True(ans):
     attempt=attempt+1
     if ans=="Modi":
         print("correct ans")
         break
     else:
         print("incorrect ans")

         if count(attempt)==1:
             hint1="he is 70 years old"
             print(hint1)
         elif count(attempt)==2:
             hint2="he is from BJP"
             print(hint2)
         elif count(attempt)==3:
             hint3="he has white beard"
             print(hint3)
         else:
             print("you are loser")
