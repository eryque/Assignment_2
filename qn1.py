# Question1:
#     Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#     between 2000 and 3200 (both included).
#     The numbers obtained should be printed in a comma-separated sequence on a single line.
numberz=[]
for numba in range(2000, 3201):
    if (numba%7==0) and (numba%5!=0):
        numberz.append(str(numba))

print(numberz,sep=',')
