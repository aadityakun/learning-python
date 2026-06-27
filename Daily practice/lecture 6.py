# def sum(a, b, c):
#     sum = a + b + c
#     print(sum)
#     return sum

# sum(5, 10, 0)
# sum("aadi", "kun", " here")

#funcation definition
# def x(a, b, c, d): #parameter
#     x = a+b+c+d
#     return x


# y= x(1,3,4,5) #funcation call; arguments
# print(y)

# def print_hello():
#     print("hello")

# y= print_hello()   
# print(y)

# def avg(a,b,n):
#     sum= a+b+n
#     avg = sum/3
#     print(avg)
#     return avg
# avg(1,2,3)
# print("aadi", "kun")
# print("aadi")
# print("kun")
# print("aadi", end="$")
# print("kun")

# def cal(a=1,b=1):
#     print(a*b)
#     return a * b

# cal(1,3) 

# lists = [1,3,4,5,5]
# names = ["aadi", "ashu","abhi", "wtf"]

# def p_len(list): #any variable can be used inside the "def"
#     print(len(list))

# def p_list(list):
#     print(list, end=" ")


# p_list(names)

# n=5 
# fact = 1
# for i in range(1, n+1): #start to stop-1 ka rule hai so 6 bhe hona par value 5 tak he calculate ho ga
#     fact = fact * i
#     print(fact)

# n = 5 
# def cal_f(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact *i 
#     print(fact)

# # cal_f(6)

# def cal_c(usd):
#     # usd = int(input("type the value "))
#     inr= usd * 90
#     print(usd, "usd =" , inr, "inr" )

# cal_c(89)

# def show(n):
#     if(n==0):
#         return
    

# recursion
# def show(n):
#     if(n == 0 ):
#         return
#     print(n)
#     show(n-1) 
#     print("end")
# show(6)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return n * fact(n-1)
# print(fact(4))  

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return n * fact(n-1)
# print(fact(int(input("fuck "))))

def fact(n):
    if(n==0):
        return 0
    return n + fact(n-1)
print(fact(int(input("s'th num "))))
