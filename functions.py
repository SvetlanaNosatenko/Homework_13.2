import json
from random import randint


def save_data(book):
    # запись данных в файл
    with open('books.json', "w", encoding='utf-8') as f:
        json.dump(book, f)
    return True


def get_data():
    # чтение данных из файла json
    with open('books.json', encoding='utf-8') as f:
        book = json.load(f)
        return book


def add_data(new_book):
    old_book = get_data()
    old_book.append(new_book)
    save_data(old_book)
    return True


def create_id(books):
    books = get_data()
    if not books:
        return 1
    max_id = 0
    for book in books:
        if book['id'] > max_id:
            max_id = book['id']
    return max_id + 1


def create_isbn() -> str:
    def gen_digits(count) -> str:
        return ''.join(map(lambda x: str(randint(0, 9)), range(count)))

    return '{}-{}-{}-{}-{}'.format(
        gen_digits(3),
        randint(1, 7),
        gen_digits(3),
        '0' + gen_digits(4),
        randint(1, 4)
    )


def data_id(id):
    """При получении книги по id читаем файл с книгами, находим нужную и ее отдаем клиенту"""
    books = get_data()
    book_found = []
    for book in books:
        if book['id'] == id:
            book_found.append(book)
    return book_found
