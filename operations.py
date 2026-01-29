from data import library


def add_book(title, author):
    if title in library:
        return "Book already exists."
    library[title] = {"author": author, "available": True, "issued_to": None}
    return "Book added successfully."


def issue_book(title, person):
    if title not in library:
        return "Book not found."
    if not library[title]["available"]:
        return "Book already issued."
    library[title]["available"] = False
    library[title]["issued_to"] = person
    return "Book issued successfully."


def return_book(title):
    if title not in library:
        return "Book not found."
    if library[title]["available"]:
        return "Book was not issued."
    library[title]["available"] = True
    library[title]["issued_to"] = None
    return "Book returned successfully."


def get_issued_books():
    issued = []
    for idx, (title, details) in enumerate(library.items(), start=1):
        if not details["available"]:
            issued.append((title, details["issued_to"]))
    return issued


def get_available_books():
    available = []
    for idx, (title, details) in enumerate(library.items(), start=1):
        if details["available"]:
            available.append((title, details["author"]))
    return available

