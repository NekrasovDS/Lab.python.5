import getpass

def check_user1(in_user):
    rez = True if getpass.getuser() == in_user else False
    return rez


def check_user2(in_user):
    rez = True if in_user.isalpha() and in_user[0].isupper() else False
    return rez


def val_user(in_user):
    if not check_user2(in_user):
        raise ValueError("Некорректное имя пользователя")
    return in_user


# Пример использования функций
try:
    username = input("Введите имя пользователя: ")
    validated_username = val_user(username)
    print(f"Имя пользователя {validated_username} корректно.")
except ValueError as e:
    print(f"Ошибка: {e}")
