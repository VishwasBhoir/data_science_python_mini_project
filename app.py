import streamlit as st

st.set_page_config(
    page_title="Vishwas Library Management System",
    page_icon=":books:",
)

from auth import login
from operations import (
    add_book,
    issue_book,
    return_book,
    get_issued_books,
    get_available_books,
)
from utils import get_all_books

st.subheader("Welcome to")
st.title("📚 Vishwas's LMS")

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN

if not st.session_state.logged_in:

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if "attempts" not in st.session_state:
        st.session_state.attempts = 3
    if st.session_state.attempts > 0:
        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.success("Login successful")
                st.session_state.attempts = 3
                st.rerun()
            else:
                st.session_state.attempts -= 1
                st.error(
                    f"Login failed. You have {st.session_state.attempts} attempts left."
                )

# MAIN MENU
else:

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.success("Logged out successfully")
        st.rerun()

    options = [
        "View All Books",
        "View Available Books",
        "View Issued Books",
        "Add Book",
        "Issue Book",
        "Return Book",
    ]

    menu = st.segmented_control("Select Operation", options, selection_mode="single")

    if menu == "View All Books":
        st.subheader("All Books")
        all_books = get_all_books()

        for idx, title, author, status in all_books:
            st.write(f"{idx}. {title} | {author} | {status}")

    elif menu == "View Available Books":
        st.subheader("Available Books")
        available_books = get_available_books()
        print("available books", available_books)
        if available_books:
            for idx, (title, author) in enumerate(available_books, start=1):
                st.write(f"{idx}. {title} | by {author}")
        else:
            st.write("No books are currently available.")

    elif menu == "View Issued Books":
        st.subheader("Issued Books")
        issued_books = get_issued_books()
        if issued_books:
            for idx, (title, issued_to) in enumerate(issued_books, start=1):
                st.write(f"{idx}. {title} | Issued to: {issued_to}")
        else:
            st.write("No books are currently issued.")

    elif menu == "Add Book":
        st.subheader("Add a New Book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        if st.button("Add"):
            st.write(add_book(title, author))

    elif menu == "Issue Book":

        st.subheader("Issue a Book")

        available_books = get_available_books()
        titles_available = [title for title, _ in available_books]

        title = st.selectbox("Select Book", titles_available)
        person = st.text_input("Issued To")
        if st.button("Issue"):
            st.write(issue_book(title, person))

    elif menu == "Return Book":
        st.subheader("Return a Book")

        issued_books = get_issued_books()
        titles_issued = [title for title, _ in issued_books]
        title = st.selectbox("Select Book", titles_issued)
        if st.button("Return"):
            st.write(return_book(title))
