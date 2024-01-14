# # ДЗ - 7
# # Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# # - домашній номер телефону (тільки цифри та довжина номера)
# # - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# # - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# # - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
#
# # додатково:
# # - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля
# # – від 8 до 16 символів)
#
#
#
# import re
#
#
# def validate_home_phone(phone_number):
#     regular_pattern = r"\d{7,15}$"
#     return re.match(regular_pattern, phone_number) is not None
#
#
# def validate_mobile_phone(phone_number):
#     regular_pattern = r"^\+?[0-9]{12}$"
#     return re.match(regular_pattern, phone_number) is not None
#
#
# def validate_email(email):
#     regular_pattern = r"^[a-zA-Z]+[._]?[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
#     return re.match(regular_pattern, email) is not None
#
#
# def validate_full_name(full_name):
#     regular_pattern = r"^[a-zA-Zа-яА-ЯіІїЇєЄёЁ\'-]{2,20}( [a-zA-Zа-яА-ЯіІїЇєЄёЁ\'-]{2,20}){2}$"
#     return re.match(regular_pattern, full_name) is not None
#
#
# def validate_password(password):
#     regular_pattern = r"^.*(?=.{8,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$"
#     return re.match(regular_pattern, password) is not None
#
#
# home_phone = "1234567"
# print(f"Домашній номер телефону: {validate_home_phone(home_phone)}")
#
#
# mobile_phone = "+380971234567"
# print(f"Мобільний номер телефону: {validate_mobile_phone(mobile_phone)}")
#
#
# email = "user@gmail.com"
# print(f"Email: {validate_email(email)}")
#
#
# full_name = "Іван Іванович Іванов"
# print(f"ПІБ: {validate_full_name(full_name)}")
#
#
# user_password = "ADmin12345$"
# print(f"Пароль користувача: {validate_password(user_password)}")
#
#