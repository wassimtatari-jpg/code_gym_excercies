string=input("Enter your sting : ")
substring=input("Enter your substring : ")

is_in=substring in string

find=string.find(substring)

count=string.count(substring)

print(f"the check result is : {is_in}")

print(f"find result : {find}")

print(f'count result {count}')