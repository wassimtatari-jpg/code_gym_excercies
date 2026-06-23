book_information={"title":"casa summer","author":"wassim","year of puplication":2026}

print("author" in book_information)

if book_information.get("Publisher")is not None:
    print("publisher found in book information")
else:
    print("publisher is not found")
if"title" in book_information.keys():
    print("title found")
else:
    print("title not found")

