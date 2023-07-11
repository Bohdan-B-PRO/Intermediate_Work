import json

def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    note = {"title": title, "content": content}
    return note

def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")

def read_notes():
    with open("notes.json", "r") as file:
        for line in file:
            note = json.loads(line)
            print("Заголовок:", note["title"])
            print("Содержимое:", note["content"])
            print()

def edit_note():
    title = input("Введите заголовок заметки, которую хотите отредактировать: ")
    new_content = input("Введите новое содержимое заметки: ")
    with open("notes.json", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            note = json.loads(line)
            if note["title"] == title:
                note["content"] = new_content
            json.dump(note, file)
            file.write("\n")
        file.truncate()

def delete_note():
    title = input("Введите заголовок заметки, которую хотите удалить: ")
    with open("notes.json", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            note = json.loads(line)
            if note["title"] != title:
                json.dump(note, file)
                file.write("\n")
        file.truncate()

def main():
    while True:
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Заметка успешно создана и сохранена.")
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
            print("Заметка успешно отредактирована.")
        elif choice == "4":
            delete_note()
            print("Заметка успешно удалена.")
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()