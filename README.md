
Library Management System




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file [POSGRESSQL]

`NAME`

`PASSWORD`

`HOST`

`PORT`

`USERNAME`





## Installation

install virtual enviroment

```bash
  python3 -m venv venv
```
install required packages

```bash
  pip install -r requirements.txt
```

activate virtual environment
```bash
Mac OS
source venv/bin/activate

windows
C:\>venv\scripts\activate

```

make migrations
```bash
python manage.py migrate
python manage.py makemigrations

```

run server
```bash
python manage.py runserver
```


    
## API Endpoints

### Books

#### Get all books

- **Endpoint:** `GET /books/`
- **Parameters:** None
- **Description:** Get a list of all books in the library.

#### Get a specific book

- **Endpoint:** `GET /books/<id>/`
- **Parameters:**
  - `id` (int): The unique identifier of the book.
- **Description:** Get details of a specific book using its ID.

#### Add a new book

- **Endpoint:** `POST /books/`
- **Parameters:**
  - `title` (string, required): The title of the book.
  - `ISBN` (string, required): The ISBN of the book.
  - `published_date` (string): The published date of the book.
  - `genre` (string): The genre of the book.
  - `details` (object): Additional details of the book, including the number of pages, publisher, and language.

#### Update a book

- **Endpoint:** `POST /books/<id>/`
- **Parameters:**
  - `id` (int): The unique identifier of the book.
  - Any fields you want to update.
- **Description:** Update the details of a specific book using its ID.

#### Delete a book

- **Endpoint:** `DELETE /books/<id>/`
- **Parameters:**
  - `id` (int): The unique identifier of the book.
- **Description:** Remove a book from the library.

#### Borrow a book

- **Endpoint:** `POST /books/borrowed/`
- **Parameters:**
  - `book_id` (int, required): The ID of the book to be borrowed.
  - `user_id` (int, required): The ID of the user borrowing the book.
- **Description:** Borrow a book from the library.

#### Return a book

- **Endpoint:** `POST /books/return/`
- **Parameters:**
  - `book_id` (int, required): The ID of the book to be returned.
  - `user_id` (int, required): The ID of the user returning the book.
- **Description:** Return a borrowed book to the library.

#### Get all borrowed books

- **Endpoint:** `GET /books/allborrowed/`
- **Parameters:** None
- **Description:** Get a list of all currently borrowed books.

### Users

#### Get all users

- **Endpoint:** `GET /user/`
- **Parameters:** None
- **Description:** Get a list of all users.

#### Get a specific user

- **Endpoint:** `GET /user/<id>/`
- **Parameters:**
  - `id` (int): The unique identifier of the user.
- **Description:** Get details of a specific user using their ID.

#### Add a new user

- **Endpoint:** `POST /user/`
- **Parameters:**
  - `name` (string, required): The name of the user.
  - `email` (string, required): The email of the user.
  - `address` (string): The address of the user.

#### Update a user

- **Endpoint:** `POST /user/<id>/`
- **Parameters:**
  - `id` (int): The unique identifier of the user.
  - Any fields you want to update.
- **Description:** Update the details of a specific user using their ID.

#### Delete a user

- **Endpoint:** `DELETE /user/<id>/`
- **Parameters:**
  - `id` (int): The unique identifier of the user.
- **Description:** Remove a user from the system.


## Sample Usage
```bash

# Add a new book
{"title": "Sample Book", "ISBN": "1234567890", "published_date": "2022-01-31", "genre": "Fiction", "details": {"number_of_pages": 200, "publisher": "Sample Publisher", "language": "English"}}'
