person_dict={
    "name":"wassim",
    "age":38,
    "city":"tangier"
}
print(person_dict)
name=person_dict["name"]
print(f"name: {name}")
print(person_dict.get("age"))
print(person_dict.setdefault("country","morroco"))