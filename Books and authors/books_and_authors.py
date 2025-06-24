library = {
    "Достоевский": ["Преступление и наказание", "Идиот"],
    "Толстой": ["Война и мир", "Анна Каренина"],
    "Булгаков": ["Мастер и Маргарита"]
}

def book_addition(library):
    while True:
        if input('Готов добавить новую книгу? (да/нет): ').lower() in ['да', 'д', 'yes']:
            author, *book_title = input('Отлично! Введи фамилию автора, а затем название книги через пробел:').split()
            cur_book = ' '.join(book_title)

            if author in library and cur_book not in library[author]:
                library[author].append(cur_book)
            else:
                library.setdefault(author, [cur_book.rstrip()])
        else:
            break

    return library

def check_book(library):
    if input('Хочешь посмотреть книги какого-нибудь автора? (да/нет): ').lower() in ['да', 'д', 'yes']:
        while True:
            author = input('Супер! Введи фамилию автора:')
            if author in library:
                author_books = library[author]
                print(f'Книги автора {author}:', end=' ')
                print(*author_books, sep=', ')
                if input('Хочешь посмотреть книги кого-нибудь ещё? (да/нет): ').lower() in ['да', 'д', 'yes']:
                    continue
                else:
                    break
            else:
                print('Такого автора нет в библиотеке.')
                continue
    return 


print('Привет!')
library = book_addition(library)
author_books = check_book(library)
max_author = max(library, key=lambda x: len(library[x]))
if input('Хочешь увидеть все книги в библиотеке? (да/нет): ').lower() in ['да', 'д', 'yes']:
    for author in sorted(library):
        print(f"{author}: {', '.join(sorted(library[author]))}")
print(f'Автор с наибольшим количеством книг в библиотеке: {max_author}.')