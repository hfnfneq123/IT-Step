def login(username, password):
    try:
        correct_username = "admin"
        correct_password = "12345"

        assert username == correct_username and password == correct_password, "Невірне ім'я користувача або пароль"

        print("Вхід виконано успішно")

    except AssertionError as error:
        print(error)

login("admin", "12345")
login("user", "12345")
login("admin", "00000")



