"""Task 1"""

# ns=input("Enter 10 numbers by \",\": ")
# ns_list=ns.split(",")
# evens=0
# odds=0

# for n in ns_list:
#     if int(n)%2==0:evens+=1
#     else:odds+=1

# print(f"Odds:{round(odds/len(ns_list)*100)}%\nEvens:{round(evens/len(ns_list)*100)}%")

"""Task 2"""

# n=input("Enter a number: ")
# int_n=int(n)
# rev_n=[]
# curr=0

# while curr<len(n):
#     rev_n.append(int_n%10)
#     int_n//=10
#     curr+=1

# if "".join(map(str, rev_n))==n:print(f"{n} is polindrom!")
# else:print(f"{n} isn't polindrom!")

"""Task 3"""

# n=input("Enter a number: ")
# slc_z=int(input("Enter a sice zone(number): "))
# slc_n=n[slc_z:]
# org_n=n[:slc_z]
# print(f"Output: {slc_n+org_n}")

"""Task 4"""

# acc=1
# primes=0

# while acc<100:
#     acc+=1
#     curr=1
#     while curr<acc:
#         curr+=1
#         if acc==2:primes+=1
#         elif acc%curr==0:break
#         else:
#             if curr!=acc-1:continue
#             else:primes+=1

# print(primes)

"""Task 5"""

# from datetime import datetime


# date=input("Enter current date (DD.MM.YYYY): ").replace(".","-")
# dt = datetime.strptime(date, "%d-%m-%Y")
# print(dt.strftime("%A"))
