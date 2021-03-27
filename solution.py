# list = ['mango', 'apple', 'pearl', 'orange']
# print (list)
# name = "boy"
# print (name)
# numb = 35.876
# print (numb)
# print(type(numb))
# Upper_numb = 498
# lower_numb = 12.5
# subt = Upper_numb - lower_numb
# print (subt)
# print (type(subt))

# numb1 = 43//4
# print (numb1)
# numb2 = 43/4
# print (numb2)
# numb3 = 43%4
# print (numb3)

# new_string = "Hippopotamusisaseaor"
# print (new_string[7:13])
# dict = {'first_name': 'Ibrahim', 'last_name': 'Oladele', 'religion': 'Islam', 'marital_status': 'single', 'wristwatch_brand': 'seiko', 'favorite_qoute': 'fear no one', }
# print (dict)
# list = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 20, 21, 22, 23, 24, 25, 26, 27, 29, 29, 44]
# print (list)
# print (set(list))


# session 3 assignment
# num=12
# for i in range(1, 13):
#    print(num,'x',i,'=',num*i)
# if num<=12:
#     print(num, 'x',i, '=',num*i, end='\t')
# else:
#     print('error')

# number=[x for x in range(2, 13)]
# multiplier = [x for x in range (2,13)]
# switch = True
# while switch:
#     for num in number:
#         for factor in multiplier:
#             print(factor, "*", num, "=", num * factor, end='\t')
# list = ['Yinka', 'Deji', 'Tola',]
# print (len(list))
# switch=True
# Fruits = ['Banana', 'Papaya', 'Mango']
# while switch:
#     for x in Fruits:
#         if x=='Papaya':
#             continue
#         print(x)
#     switch=True
#     print(x)
#     x+=1
    
# for b in range(2, 24, 4):
#     print(b)

# for v in range(10):
#     print(v)
# else:
#     print('Completed!!!')

# adj = ['red', 'hard', 'soft']*1
# organ = ['heart', 'bone', 'muscle']*1
# for c in organ:
#     for b in adj:
#         print(c,b)




# def recur_fibo(nterms):
#     nterms=5
#     print("fibonacci series:")
#     for i in range(nterms):
#         print(recur_fibo(i))

#python function to print a fibonacci series up to 5th term

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms=5
if nterms<=1:
    print('yes')
else:
    print("Fibonacci series:")
    for i in range(nterms):
        print(recur_fibo(i))


# f = open("myfile.txt", "x")
# f = open("myfile.txt" "x")
# 

# f = open("myfile.txt", "x")
# f = open("myfile.txt", "a")
# f.write("Firstname: Ibrahim")
f = open("myfile.txt", "w")

f.write("Firstname: Ibrahim",)
f.write(" ")
f = open("myfile.txt", "a")

f.write("Surname: Oladele",)
f.write(" ")
f.write("Lastname: Olayinka",)
f.write(" ")
f = open("myfile.txt", "r")
print(f.read())


        




        
