with open(file="rockyou.txt", mode="rt", encoding="LATIN-1") as file1:
    result = 0  # Змінна що відповідає за кількість схожих елементів
    lines_search = input("Введіть будьласка строчку для пошуку ")
    for search in file1:
        if (
            lines_search == search.strip()
        ):  # Функція що перевіряє чи є ця строка в файлі
            result += 1
            print(f"знайдено {result} схожих файлів")
    if result == 0:
        print("Нічого не знайдено(")
