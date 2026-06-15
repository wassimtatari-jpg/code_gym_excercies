fruits={"orange","cherry","lemmon","apple"}

for index,fruit in enumerate(fruits,start=1):
    print(f"{index}: {fruit}")

number_replace=int(input("Enter a number for replacment : "))-1

new_fruit=input("Enter a new fruit name : ")

fruit_list=list(fruits)

fruit_list[number_replace]=new_fruit

fruits=set(fruit_list)

print("Updated list",fruits)