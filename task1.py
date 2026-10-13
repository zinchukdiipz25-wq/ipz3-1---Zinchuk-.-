lines = ["запуск", "вхід користувача", "помилка", "вихід"]

log = []
for line in lines:
    log.append(line)        # тільки додавання в кінець

log.reverse()               # порядок змінюємо після того, як усе зібрано
for line in log:
    print(line)
