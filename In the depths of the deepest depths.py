person_information={
    "first name":"wassim",
    "age":38,
    "personl details":{
        "city born":"aleppo",
        "date birth":1987,
        "details":{
            "city":"tangier",
            "country":"morroco"  
        }
    }
}
print(person_information)

person_information["first name"]="ahmed"
person_information["personl details"]["details"]["city"]="casablanca"
print(person_information)
person_information["personl details"]["details"]["location"]="africa"
person_information["last name"]="tatari"
print(person_information)
del person_information["personl details"]["details"]["country"]
print(person_information)
