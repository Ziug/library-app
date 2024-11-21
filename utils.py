import json

# ----------------------- utils -----------------------
def is_canceled(inputs):
	return any(input.strip() == '--' for input in inputs)

def validate_book_input(title, author, year, status):
    if not all([title, author, year, status]):
        print('Ошибка: Все поля должны быть заполнены!')
        return False

    try:
        int(year)
        status = int(status)
        
        if status not in [0, 1]:
            print('Ошибка: Статус должен быть 0 или 1')
            return False
    except ValueError:
        print('Ошибка: Год и статус должны быть числами')
        return False
    
    return True