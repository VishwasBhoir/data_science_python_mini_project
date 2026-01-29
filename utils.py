from data import library

def get_all_books():
    books = []
    for idx, (title, details) in enumerate(library.items(), start=1):
        status = (
            "Available" if details["available"] else f"Issued to {details['issued_to']}"
        )
        books.append((idx, title, details["author"], status))
    return books
