popular_cat_names={"mira","raina","tia","anbar","lina"}

attemps=0

while popular_cat_names:
    guess=input("Enter cat name : ")
    attemps+=1

    if guess in popular_cat_names:
        popular_cat_names.remove(guess)
        print(f"Correct, Remined name is {len(popular_cat_names)}")
    else:
        print("Incorrect,Try again")

print(f"You guess all cats name in {attemps}")

    