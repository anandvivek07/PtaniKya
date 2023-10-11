#Print
#print("Hello")
#print("Hello World")
#print("My name is Vivek Anand")
#print("My senior is Rahul Dev.")

#Percentage
#a=int(input("enter the value of 1st digit"))
#b=int(input("enter the value of 2nd digit"))
#c=a/b*100
#print(c)

#Variable_Declare
#__name__="RAJ"
#print(__name__)

#multiple_value
#1
#a=b=c=78
#print(a,b,c)

#2
#a,b,c=88,55,66
#print(a,b,c)

#Sum
#a=int(input("enter the value of 1st digit"))
#b=int(input("enter the value of 2nd digit"))
#c=a+b
#print(c)


#1Integer
#a=10
#print(type(a))

#2float
#a=54.55
#print(type(a))

#3complex
#a=123+55j
#print(type(a))

#Boolean
#a=45>44
#print(type(a))

#Dictionary
#a={1:"Ram",2:"Sita",2:"Geeta"}
#print(a)
#print(type(a))

#a={1:"Ram",2:"Sita",3:"Geeta"}
#print(a)
#print(type(a))

#Converters
#1currency
#Rupee=82.7
#Dollar=int(input("Enter the number of dollar"))
#converted=Rupee*Dollar
#print(converted)

#2temprature
#celcius=33.8
#fahrenheit=int(input("number"))
#result=celcius*fahrenheit
#print(result)

#DataTypes
#1numeric
#2dictionary
#3boolean
#4set
#5sequence

#1numeric
#a)integer
#a=55
#print(a)
#print(type(a))

#b)float
#a=12.2
#print(a)
#print(type(a))

#c)complex
#a=44+4j
#print(a)
#print(type(a))

#2dictionary
#a={1:"Rahul",2:"Raj",3:"888"}
#print(a)
#print(type(a))

#3boolean
#a=456.5==456.55
#print(a)
#print(type(a))

#4set
#a={132,546123546123,132}
#print(a)
#print(type(a))

#5sequence
#a)string
#a="Qwert@123#!$%^^|/\';hfia465"
#print(a)
#print(type(a))

# a='k654jhldfuisyfd$@#'
# print(a)
# print(type(a))

# a="'k654jhldfuisyfd$@#'"
# print(a)
# print(type(a))

#b)list
#a=[465,1.4,"hjijho"]
#print(a)
#print(type(a))


# a=[1,1,1,"afsj",{456,546}]
# print(a)
# print(type(a))\

#c)tuple
# a=("gfafd",465,132.5)
# print(a)
# print(type(a))

#OPERATORS
#1ArithmeticOperators
# +,-,*,%,/,**,++,--
# a=20
# b=2
# c=a%b
# print(c)

#2Comparision Operators
#==,>=,<=,<,>

# a=54
# b=55
# c=a>b
# print(c)

#3Assignment Operators
# a=45
# b=23
# c=a+=b
# print(c)

#4Logical Operators
# 1=true 0=false
#AND(*) OR(+) NOT(REVERSE)

#Bitwise Operators
#(&,!,^,~,<<,>>)
#<< left shift (multiply twice)
# a=45
# b=a << 2
# print(b)

# >> right shift (divide twice) 
# a=45
# b=a >> 2
# print(b)

#6Membership Operators
#(IN)  (NOT IN)
# L=[1,2,3,4,5]
# check=6;
# if check in L:
#     print('yes')
# else:
#     print("no")


#7Identity Operators
# (IS)  (IS NOT)
# a=54
# b=56
# c=a is b
# print(c)

# a=54
# b=56
# c=a is not b
# print(c)

#Flow Control Statements
#1 Conditional Statements
# if,if as,if-elif-else,nested-if-else

# a=11
# if(a==10):
#     print("Right")
# else:
#     print("Wrong")

# a=11
# if(a>=10):
#     print("Right")
# else:
#     print("Wrong")




#Calculator

operator=input("enter the operator,+,-,*,/:")
a=int(input("enter the 1st value"))
b=int(input("enter the 2nd value"))
if(operator=="+"):
    print(a+b)
elif(operator=="-"):
    print(a-b)
elif(operator=="*"):
    print(a*b)
elif(operator=="/"):
    print(a/b)
elif(operator=="%"):
    print(a/b*100)
else:
    print("enter the valid value")



#2. Iterative statement
# marks=int(input("enter the marks obtained"))
# if(marks<33 and marks>=0):
#     print("Fail")
# elif(marks<50 and marks>33):
#     print("Fail")
# elif(marks<70 and marks>=50):
#     print("C")
# elif(marks<80 and marks>=70):
#     print("B")
# elif(marks<=100 and marks>=80):
#     print("A")
# else:
#     print("Please enter the valid value")