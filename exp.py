# # a, b, c, d  = 1, 4, 5 , 6
# # x = y = z = 2
# # cal= (a + b)
# # num = (((a + b + c + d) * c) / z)
# # print(cal)
# # print (num)

# #<<<<<<<<<<<<<<<<<<< umpacking element>>>>>>>>>>>>>>>>>>

# # a = [1,2,3,4,6]
# # x, *y, z  = a
# # print("frist :", x)
# # print("middle :", y)
# # print("last:" , z)

# # <<<<<<<<<<<<<<<<<<<<<<<<<<globle variablr using (def) function >>>>>>>>>>>>>>>>
# # a ="mahesh"
# # def some():
# #     a ="saurabh"
# #     print(a)
# # some()
# # print(a)
# # num1 = 5
# # def addition():
# #  global num2
# #  num2 = 10

# # addition()
# # print("addition of num1 and num2 :- ",num1 + num2)

# # a = "Global" # global variabl
# # def greet():
# #  global a
# #  a= "Local" #local variable
# #  print("Hello", a)
# # greet()
# # print("Hello ",a)

# # name = "India"
# # print("Name before changing :-", name)
# # def ChangeGlobalVariable():
# #  global name
# #  name = "Bharat"
# # ChangeGlobalVariable()
# # print("Name after changing :- ",name)

# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<sitring or arry    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # lineOfMind = """When" You Expect \"""more\""" than others expectations, it hurts more than others expectations"""
# # print(len (lineOfMind))
# # print(lineOfMind[1:4])

# # word = "radar"
# # if word == word[::-1]:
# #     print("It is a palindrome!")

# # Name = "Karan"
# # print(Name[2])


# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   py collections   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Name = ["Karan" , "mahesh" , "saurabh", 'chetan'] 
# # print(Name[2])

# # stdName = list["Chetan", 2, True, 2.5, 1+7j]
# # print(type(stdName))

# # stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh","bittu" , "seenu" , "riya", "Gayatri"]
# # print(stdName[::3])
#  #------------------------------------------------------------------------------------------------
# # insert item

# # {.instert(index,element)}
# stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
# print(len(stdName))
# stdName.insert(3,"bittu")
# stdName.insert(7,"seenu")
# stdName.insert(5,"sarry")
# print(stdName)
# print(len(stdName))

# #-----------------------------------------------------------------------------------------------------

# #{ .append()}
# # stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
# # stdName.append("mahesh")
# # print(stdName)

# # -----------------------------------------------------------------------------------------------------
 
# # { .extend()} can add multiple data
# # stdName   = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
# # stdRollNo = [1,2,3,4,5]
# # stdclass  = ["A" , "B"]
# # school = stdName + stdRollNo
# # school.extend(stdclass)
# # print(school)

#  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< remove the intem from list >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# # .remove and pop function

# stdName   = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
# stdName.pop(4)
# stdName.remove("Chetan")
# stdRollNo = [1,2,3,4,5]
# stdclass  = ["A" , "B"]
# school = stdName + stdRollNo
# school.extend(stdclass)
# print(school)

# #----------------------------------- del key word--------------------------------------------------

# # stdname = ["Arjun","Nilima","Kavya","Rohan","Sneha","Vikram"]
# # stdroll = [
# #     "1",
# #     "5",
# #     "10",
# #     "20",
# #     "55",
# #     "100"
# # ]
# # stdname.extend(stdroll)
# # del stdname [0]
# # stdname.insert(0,"Tejuu")
# # print(stdname)

# # stdname = ["Arjun","Nilima","Kavya","Rohan","Sneha","Vikram"]
# # del stdname 
# # print(stdname)

# #--------------------------------------clear key word --------------------------------------------

# # stdname = ["Arjun","Nilima","Kavya","Rohan","Sneha","Vikram"]
# # stdname.clear ()
# # print(stdname)

# #---------------------------------------- Sort list-----------------------------------------
# # stdname = [
# #     'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
# #     'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
# #     'Z', 'X', 'C', 'V', 'B', 'N', 'M'
# # ]
# # stdname.sort()
# # print (stdname)

# #  #                                _________in decending order________

# # stdname.sort(reverse=True)
# # print(stdname) 


# # alpha = [
# #     'g', 'B', 'r', 'Q', 'a', 'M', 'z', 'E', 'h', 'T', 
# #     'y', 'L', 'p', 'O', 'c', 'X', 'v', 'I', 'd', 'K', 
# #     's', 'J', 'f', 'W', 'u', 'N', 'b', 'R', 'x', 'U', 
# #     'm', 'G', 'n', 'P', 'q', 'Y', 'e', 'H', 'j', 'V', 
# #     'k', 'S', 'o', 'A', 'w', 'D', 'i', 'Z', 't', 'F', 
# #     'l', 'C'
# # ]

# # alpha.sort()
# # print(alpha)
# # # alpha.sort(reverse=True)
# # # print(alpha)

# # alpha.reverse()
# # print(alpha)

# # alpha.sort(key = str.lower)
# # print(alpha)
# #----------------------------------------copy list-----------------------------------------------

# # stdname1 = ["Rahul", "Priya", "Amit", "Rahul", "Sneha", "Rahul"]
# # stdname2 = ["User_01", "500", "Admin", "1234", "Guest", "99"]
# # anotherlist=stdname2.copy()
# # stdname2.pop()
# # print(stdname2)
# # print(anotherlist)


# # #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< tuple>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # my_tuple= 1, 2, 3, "hey"
# # print(my_tuple)
# # print(type(my_tuple))

stdname = ["Arjun","Nilima","Kavya","Rohan","Sneha","Vikram"]
new_tuple= tuple(stdname)
print(new_tuple)
print(type(new_tuple))
num1 = set(new_tuple)
print(num1)
print(type(num1))

stdname = ("Arjun","Nilima","Kavya","Rohan","Sneha","Vikram")
print(stdname[0])







