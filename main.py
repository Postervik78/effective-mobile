import sys
import json

#создание класса "книга"
class Book:
    bid = 1
    books = []

    #инициализация переменных через конструктор
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.name_status = "В наличии"

    #создание функции, которая добавляет книгу. Имея 3 параметра на ввод
    def add_book(self):

        print("Введите название книги:")
        self.title = input()
        print("Введите автора:")
        self.author = input()
        try:
            print("Введите год выпуска:")
            self.year = int(input())
        except ValueError:
            print("Вы ввели неверное значение, пожалуйста введите данные в числовом формате \n")
            return Book.add_book(self)

        book = {'id': self.bid, 'title': self.title, 'author': self.author, 'year': self.year,
                'status': self.name_status} #создание словаря
        Book.books.append(book) #добавление словаря в ранее созданный список
        Book.bid += 1
        print("Книга успешно добавлена \n")

    # создание функции, которая удаляет книгу по параметру 'id'
    def delete_book(self, tmpbid):
        if not Book.books:
            print("Библиотека пуста")
        else:
            for x in range(len(Book.books)):
                if Book.books[x]['id'] == tmpbid:
                    Book.books.remove(Book.books[x])
                else:
                    print("Книги не существует")
    #создание функции, которая осуществляет поиск книги по нескольким параметрам
    def find_book(self, findkey):
        findbook = []
        checkkey = str(input())
        if checkkey == "title":
            for x in range(len(Book.books)):
                if Book.books[x]['title'] == findkey:
                    findbook.append(Book.books[x])
            else:
                print("Книга не найдена")
        elif checkkey == "author":
            for x in range(len(Book.books)):
                if Book.books[x]['author'] == findkey:
                    findbook.append(Book.books[x])
            else:
                print("Книга не найдена")
        elif checkkey == "year":
            for x in range(len(Book.books)):
                if Book.books[x]['year'] == findkey:
                    findbook.append(Book.books[x])
            else:
                print("Книга не найдена")
        else:
            print("Такой команды не существует")
        print(*findbook)

    #создание функции, для отображение полного списка книг
    def list_books(self):
        print(*Book.books)

    #создание функции, которая меняет статус книги в зависимости от текущего
    def change_status(self, tmpbid):
        for x in range(len(Book.books)):
            if Book.books[x]['id'] == tmpbid:
                if Book.books[x]['status'] == "В наличии":
                    Book.books[x]['status'] = "Выдан"
                else:
                    Book.books[x]['status'] = "В наличии"

def main():
    book = Book(title="", author="", year=int) #создание экземпляра класса 'Book'
    print("Введите команду \nОсновные команды: \n addbook - добавить книгу \n deletebook - удалить книгу\
    \n findbook - найти книгу \n listbooks - отображение всех книг \n changestatus - изменить статус книги \n save - сохранить книги \n exit - выйти")
    command = str(input())

    if command == "addbook":
        book.add_book()
    if command == "deletebook":
        try:
            book.delete_book(int(input()))
        except ValueError:
            print("Введен неверный формат данных")
    if command == "findbook":
        book.find_book(input())
    if command == "changestatus":
        book.change_status(int(input()))
    if command == "listbooks":
        book.list_books()
    if command == "exit":
        sys.exit()
    if command == "save":
        with open("список.json", "w", encoding="utf-8") as file:
            json.dump(Book.books, file)
        print("Данные сохранены")
        sys.exit()


try:
    while True:
        main()
except:
    print("\n ПРИЛОЖЕНИЕ ЗАКРЫТО")
