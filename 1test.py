# a, b, c, d  = 1, 4, 5 , 6
# x = y = z = 2
# cal= (a + b)
# num = (((a + b + c + d) * c) / z)
# print(cal)
# print (num)

#<<<<<<<<<<<<<<<<<<< umpacking element>>>>>>>>>>>>>>>>>>

# a = [1,2,3,4,6]
# x, *y, z  = a
# print("frist :", x)
# print("middle :", y)
# print("last:" , z)

# <<<<<<<<<<<<<<<<<<<<<<<<<<globle variablr using (def) function >>>>>>>>>>>>>>>>
# a ="mahesh"
# def some():
#     a ="saurabh"
#     print(a)
# some()
# print(a)
# num1 = 5
# def addition():
#  global num2
#  num2 = 10

# addition()
# print("addition of num1 and num2 :- ",num1 + num2)

# a = "Global" # global variabl
# def greet():
#  global a
#  a= "Local" #local variable
#  print("Hello", a)
# greet()
# print("Hello ",a)

# name = "India"
# print("Name before changing :-", name)
# def ChangeGlobalVariable():
#  global name
#  name = "Bharat"
# ChangeGlobalVariable()
# print("Name after changing :- ",name)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<sitring or arry    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# lineOfMind = """When" You Expect \"""more\""" than others expectations, it hurts more than others expectations"""
# print(len (lineOfMind))
# print(lineOfMind[1:4])

# word = "radar"
# if word == word[::-1]:
#     print("It is a palindrome!")

# Name = "Karan"
# print(Name[2])


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   py collections   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Name = ["Karan" , "mahesh" , "saurabh", 'chetan'] 
# print(Name[2])

# stdName = list["Chetan", 2, True, 2.5, 1+7j]
# print(type(stdName))

# stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh","bittu" , "seenu" , "riya", "Gayatri"]
# print(stdName[::3])
 #------------------------------------------------------------------------------------------------
# insert item

# {.instert(index,element)}
# stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
# print(len(stdName))
# stdName.insert(3,"bittu")
# stdName.insert(7,"seenu")
# stdName.insert(5,"sarry")
# print(stdName)
# print(len(stdName))

#-----------------------------------------------------------------------------------------------------

#{ .append()}
# stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
# stdName.append("mahesh")
# print(stdName)

# -----------------------------------------------------------------------------------------------------
 
# { .extend()} can add multiple data
# stdName   = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
# stdRollNo = [1,2,3,4,5]
# stdclass  = ["A" , "B"]
# school = stdName + stdRollNo
# school.extend(stdclass)
# print(school)