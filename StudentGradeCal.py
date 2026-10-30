name=input("Enter name of the student:- ")
print("Enter marks in 5 subject: ")
Maths=int(input("Math: "))
Science=int(input("Science: "))
English=int(input("English: "))
Computer=int(input("Computer: "))
Social=int(input("Social: "))
total=Maths+Science+English+Computer+Social
pre=(total/500)*100
print("Total Marks:",total,"/500")
print("Percentage:",pre,"%")
if 90<pre<100:
    print("Grade:A ")
elif 80<pre<89:
    print("Grade:B")
elif 70<pre<79:
    print("Grade:C")
elif 60<pre<69:
    print("Grade:D ")
else:
    print("Grade:F")


