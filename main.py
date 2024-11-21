import json, os

from utils import validate_book_input, is_canceled

# Функция для добавления книги в библиотеку
def add_book():
	print('Название, автор, год издания, статус через пробел: \n')
	while True:

		# Последовательный ввод характеристик книги
		title = input('Название книги: ').strip()
		author = input('Автор: ').strip()
		year = input('Год издания: ').strip()
		status = input('Статус книги (0 - Выдана, 1 - В наличии): ').strip()

		# Статус = “в наличии”, если пользователь ничего не ввёл
		if not status:
			status = '1'

		# Проверка на отмену операции
		if is_canceled([title, author, year, status]):
			print('Операция отменена')
			return
        
        # Валидация введенных данных
		if validate_book_input(title, author, year, status):
			break
		print('Пожалуйста, введите корректные данные.')

	# Запись книги в файл library.json
	with open('library.json', 'r+') as file:
		library = json.load(file)
		
		# Генерация нового уникального идентификатора
		new_id = len(library) + 1
		
		# Создание словаря с информацией о новой книге
		new_book = {
			'title': title,
			'author': author,
			'year': int(year),
			'status': 'в наличии' if status == '1' else 'выдана'
		}
		
		# Добавление новой книги в библиотеку
		library[str(new_id)] = new_book

		# Перенос указателя в начало файла
		file.seek(0)

		# Обновление библиотеки
		json.dump(library, file, indent=2, ensure_ascii=False)
		file.truncate()
		print(f'*** Книга "{title}" добавлена с ID {new_id}. ***')

# Функция для удаления книги из библиотеки
def delete_book():
	# Открытие файла библиотеки для чтения
	with open('library.json', 'r') as file:
		library = json.load(file)
		while True:
			# Ввод ID книги для удаления
			book_id = input('Введите ID книги, которую вы хотите удалить: ')

			# Проверка на отмену операции
			if book_id == '--':
				print('Операция отменена')
				return

			# Проверка на отмену операции
			if book_id.isnumeric() and book_id in library.keys():
				break

			# Проверка на существование книги с данным ID
			if not book_id in library.keys():
				print('Книги с данным ID не существует')
			else:
				print('ID книги указан неправильно. ID - число')

	# Удаление книги из библотеки
	del library[book_id]

	# Обновление библиотеки
	with open('library.json', 'w') as file:
		json.dump(library, file, indent=2)
		print(f'*** Книга с ID {book_id} была удалена. ***')


# Поиск книги по её ID
def search_book():
	# Открытие файла библиотеки для чтения
	with open('library.json', 'r') as file:
		library = json.load(file)
		while True:
			# Ввод ID книги для удаления
			book_id = input('Введите ID книги, которую вы хотите удалить: ')

			# Проверка на отмену операции
			if book_id == '--':
				print('Операция отменена')
				return

			# Проверка на отмену операции
			if book_id.isnumeric() and book_id in library.keys():
				break

			# Проверка на существование книги с данным ID
			if not book_id in library.keys():
				print('Книги с данным ID не существует')
			else:
				print('ID книги указан неправильно. ID - число')
		
		# Извлечение книги из библиотеки по указанному ID
		book = library[book_id]

		# Вывод информации о книге
		print(f"ID: {book_id:<5}"
				f"\nНазвание: {book['title']}"
				f"\nАвтор: {book['author']}"
				f"\nГод издания: {str(book['year'])}"
				f"\nСтатус: {book['status']}")

def all_books():
	# Открытие файла библиотеки для чтения
	with open('library.json', 'r') as file:
		library = json.load(file)
        
		# Проверка на наполненность книги
		if not library:
			print("Библиотека пуста.")
			return
        
        # Вывод верхней строки/названия столбцов
		print(f"{'ID':<5}{'Название':<25}{'Автор':<20}{'Год':<10}{'Статус':<15}")
		print("-" * 75)
        
        # Вывод информации о книгах с форматированием текста
		for book_id, book_info in library.items():
			
			# Извлечение информации о книге и её форматирование
			title = book_info['title'][:23] if len(book_info['title'])<25 else book_info['title'][:19]+'...'
			author = book_info['author'][:20] if len(book_info['author'])<20 else book_info['aut'][:20]+'...'
			year = str(book_info['year'])
			status = book_info['status']

			# Вывод отформатированной информации о книге
			print(f"{book_id:<5}"
				f"{title:<25}"
				f"{author[:20]:<20}"
				f"{year:<10}"
				f"{status:<15}")


# Изменение статуса книги по её ID
def change_status():
	# Открытие файла библиотеки для чтения
	with open('library.json', 'r+') as file:
		library = json.load(file)
		while True:
			# Ввод ID книги которая будет меняться и её новый статус
			book_id = input('Введите ID книги, которую вы хотите редактировать: ')
			status = input('Статус книги (0 - Выдана, 1 - В наличии): ')

			# Проверка на правильность ввода статуса
			if not status in ["0", "1"]:
				print('Ошибка: Статус должен быть 0 или 1')
			
			else:
				status = 'в наличии' if int(status) == 1 else 'выдана'
			
					
			# Проверка на отмену операции
			if book_id == '--':
				print('Операция отменена')
				return

			# Проверка на отмену операции
			if book_id.isnumeric() and book_id in library.keys():
				break

			# Проверка на существование книги с данным ID
			if not book_id in library.keys():
				print('Книги с данным ID не существует')
			else:
				print('ID книги указан неправильно. ID - число')

		print(f'*** Статус книги с ID {book_id} был изменён на {status}. ***')

		# Смена статуса книги
		library[book_id]['status'] = status

		# Перенос указателя в начало файла
		file.seek(0)

		# Обновление библиотеки
		json.dump(library, file, indent=2, ensure_ascii=False)
		file.truncate()



def main():
	# Вывод загаловка программы 
	print(f'{'Консольная библиотека':=^30}')

	# Вывод справочного меню
	menu = ('Команды управления библиотекой:'
	    '\na - добавить книгу' 
	    '\nd - удалить книгу'
	    '\ns - поиск книги по её названию, автору или году издания'
	    '\nA - отобразить все книги'
	    '\nc - изменить статус киниги'
	    '\n-- (два минуса) - отмена операции'
	    '\nh - список команд'
	    '\nq - выйти из приложения')

	print(menu)

	# Основной цикл программы, обрабатывающий введённые команды
	# Работвет до выхода пользователем из программы 
	while True:
		# Полчуение команды от пользователя
		cmd = input('\nКоманда: ')

		# Выполнение определённых функций, в зависимости от введённой команды
		match cmd:
			case 'a':
				add_book()

			case 'd':
				delete_book()

			case 's':
				search_book()

			case 'A':
				all_books()

			case 'c':
				change_status()

			case 'h':
				print(menu)

			case 'q':
				break

			case _:
				print("Введена неправильная команда")

# Инициализация программы
if __name__ == '__main__':
	# Создание файла библиотеки, если такового нет или является пустым
	if not os.path.exists('library.json') or os.path.getsize('library.json') == 0:
		with open('library.json', 'w') as file:
			json.dump({}, file)
	# Запуск программы
	main()