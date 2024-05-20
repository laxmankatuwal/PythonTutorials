#CHAPTER2 STRINGS

name=input("enter your name:")
 print("length of str=", len(name))


str="i am $ if $ ah $hasfgaty$"
print(str.count("$"))

age=34
if(age>=18):
    print("vote")
else:
    print("not vote")    

mark=int(input("marks of the student:"))

if(mark>=90):
   grade="A"
elif(mark>=80  and mark<90):
   grade="B"
elif(mark>=70 and mark<80):
    grade="c"
else:
   grade="D"

num=int(input("enter num:"))

if (num % 2==0):
    print("EVEN")
else:
    print("ODD")    


a=int(input("enter first num:"))
b=int(input("enter second num:"))
c=int(input("enter third num:"))

if(a>=b and b>=c):
    print("First nu is largest", a)
elif(b>=c):
    print("second num is largest", b)
else:
    print("Third num is largest", c)        

x=int(input("enter  num:"))
if(x % 7 ==0):
    print("multiple of 7")
else:
    print("not multiple of 7")    