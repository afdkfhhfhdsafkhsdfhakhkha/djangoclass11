#def function1():
 #   print("hello i m in this function")

    
#function1()
#print("i m outside the funcion")

#function1()
#print("function gapping")
#function1()

#def function2(x):
    
    #return 2*x

#a =function2(3)
#print(a)


#def function3(x,y):
 #return x+y
#b=function3(2,3)
#print(b)

def function4(l):
   print(l)
   print("i m still in this function")
   return l*l
c=function4(6)
print(c)


name1="anil"
height1=2.5
weight1=60

name2="sunil"
height2=3
weight2=70

name3="rabin"
height3=5
weight3=100

def bmicalculatorfF(name,height,weight):
   
    bmi=weight/(height**2)


    print("bmi:",bmi)

    if bmi < 25:
        return name +" is not overweight"
    else :
      return name +" is over weight "
     
result1=bmicalculatorfF(name1,height1,weight1)
result2=bmicalculatorfF(name2,height2,weight2)
result3=bmicalculatorfF(name3,height3,weight3)

print(result1)
print(result2)
print(result3)