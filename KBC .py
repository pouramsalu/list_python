# question_list =["How many continents are there?",]
# ["What is the capital of India?",]
# ["NG mei kaun se course padhaya jaata hai?",]


# # options_list = [
# # s=[
# #pehle question ke liye options
# options_list = [["Four", "Nine", "Seven", "Eight"],
# # #second question ke liye options
# ["Chandigarh", "Bhopal", "Chennai", "Delhi"]
# # #third question ke liye options
# ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]


# solution_list=[3,4,1]
# i=0
# j=0
# while i<len(question_list)and j<len(options_list):
#     print(question_list[i])
#     k=0
#     while k<(len(options_list)+2):
#         print(k+i,options_list[j][k])
#         k=k+1
#     sol=int(input("enter the number"))
#     if sol==solution_list[i]:
#         print("congratulation! correct answer")
#     else:
#         print("better luck next time")
#     print()
#     i=i+1
#     j=j+1


# solution=[4]
# i=0
# j=0
# while i<len(q) and j<len(s):
#     print(q[i])
#     k=0
#     while k<(len(s)):
#         print(s[k])
#         k=k+1
#     sol=int(input("enter the number"))
#     if sol==solution[i]:
#         print("congratulation! correct answer")
#     else:
#         print("better luck next time")
#     print()
#     i=i+1
#     j=j+1


# # 3rd answer
# solution=[2,4,3,7]
# i=0
# j=0
# while i<len(q) and j<len(s):
#     print(q[i])
#     k=0
#     while k<(len(s)):
#         print(s[k])
#         k=k+1
#     sol=int(input("enter the number"))
#     if sol==solution[i]:
#         print("congratulation! correct answer")
#     else:
#         print("better luck next time")
#     print()
#     i=i+1
#     j=j+1



# question= [
# "How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"
# ]
# option = [
# ["Four", "Nine", "Seven", "Eight"], 
# ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
# ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# solution= [3, 4, 1]
# i=0
# while i<len(question):
#     print("Q",i+1,question[i])
#     j=0
#     while j<(len(option)+1):
#         print(j+1,option[i][j])
#         j+=1
#     k=0
#     sol=int(input("enter any number:"))
#     if sol==solution[i]:
#         print("true the correct ans is",sol)
#     else:
#         print("False")
    # print()
    # i+=1
    # k+=1

question_list=["How many continents are there ?","What is the capital of India ?",
"NG mei kaun se course padhaya jaata hai ? "]
options_list=[["Four","Nine","Seven","Eight"],
["Chandigarh","Bhopal","Chennai","Delhi"],
["Software Engineering","Counseling","Tourism","Agriculture"]]
life_line=[["Seven","Eight"],["Bhopal","Delhi"],["SoftwareEngineering","Counseling"]]
solution_list2=[1,2,1]
i=0
count=0
solution_list=[3,4,1]
while i<len(question_list):
	print("Q.",i+1,question_list[i])
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1
	user=int(input("enter any number: "))
	if user==solution_list[i]:
		print("congrates your answer is correct")
	elif user==5050:
		if count==0:
			k=0
			while k<len(life_line[i]):
				print(k+1,life_line[i][k])
				k=k+1
			count=count+1
			user2=int(input("enter any number. "))
			if user2==solution_list2[i]:
				print("you answer is right")
			else:
				print("wrong answer:")
		else:
			print("you already used the 5050 chance")
			num=int(input("enter any number: "))
			if num==solution_list[i]:
				print("right answer")
			else:
				print("wrong answer")
				break
	else:
		print("Your answer is wrong")
		break
	i=i+1