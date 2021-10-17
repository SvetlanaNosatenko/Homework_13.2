from functions import *
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/book/<int:id>')
def book(id: int):
    """Получение книги по id."""
    book_found = data_id(id)
    if data_id(id):
        return jsonify(book_found), 200
    return jsonify({"status": "failed"}), 400


@app.route('/new/', methods=['POST'])
def new_book():
    """Создание новой книги с генерацией id и isbn"""
    new_book = request.json
    new_id = create_id(book)
    new_book["id"] = new_id
    isbn = create_isbn()
    new_book['isbn'] = isbn
    if add_data(new_book):
        return jsonify({"status": "success"}), 201
    return jsonify({"status": "failed"}), 400


if __name__ == '__main__':
    app.run(debug=True)
