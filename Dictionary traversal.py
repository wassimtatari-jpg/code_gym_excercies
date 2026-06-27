person_informarion={
    "first name":"wassim",
    "last name":"tatari",
    "details":{
        "age":38,
        "date birth":1987,
        "nationality":"syrian",
        "contact information":{
            "phone":123456789
        }
    }
}
def print_all(d,intend=0):
    for key,value in d.items():
        print(" "*intend+str(key)+" :" ,end=" ")
        if isinstance(value,dict):
            print()
            print_all(value,intend+5)
        else:
            print(value)
print_all(person_informarion)