# 교재 p.270
# class Book:
#     def set_info(self, title, author):
#         self.title = title
#         self.author = author
#
# book1 = Book()
# book2 = Book()
#
# book1.set_info('파이썬', '이승아')
# book2.set_info('어린왕자', '생택쥐페리')
#
# print(book1.set_info)
# print(book2.set_info)

# 답
class Book:
    title = ""
    author = ""

    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'Title : {self.title}, Author: {self.author}')

book1 = Book()
book2 = Book()

book1.set_info('파이썬', '이승아')
book2.set_info('어린왕자', '생택쥐페리')

book_list = [book1, book2]

for book in book_list:
    book.print_info()