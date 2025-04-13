# Question 5: Loop Control Statements (break, continue, pass)
# 5. Given a list of numbers from 1 to 9, use the following loop control statements:
#    - Use 'break' to stop the loop when the number is 5 and print "Breaking at: 5".
#    - Use 'continue' to skip even numbers and print only the odd numbers.
#    - Use 'pass' to do nothing when the number is 3 and print all other numbers except 3.


for i in range(1,9):
    if(i == 5):
        print("breaking at : "+str(i)); 
        break;
    if(i%2==0):
        continue;
    if (i==3):
        pass; #differnec between pass and continue 
    else:
        print(i,end=",");

    

