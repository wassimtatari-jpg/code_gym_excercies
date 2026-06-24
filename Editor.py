book_inf={"title":"The editor","author":"codegym","year of publication":2026}
print(book_inf)
book_inf["year of publication"]=2025
print(book_inf)
new=book_inf.setdefault("publisher","wassim")
print(book_inf)
new={"title":"coding skiles","author":"codecamping"}
book_inf.update(new)
print(book_inf)