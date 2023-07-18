import view
import Note


def start():
    while True:
        view.menu_console()
        user_input = input()
        if user_input == '1':
            show("all")
        elif user_input == '2':
            show("ID")
        elif user_input == '3':
            show("date")
        elif user_input == '4':
            show("all")
            change_note()
        elif user_input == '5':
            add_note()
        elif user_input == '6':
            show("all")
            del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break
        

def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Note.Note(title=title, body=body)
    array_notes = read_file()
    for i in array_notes:
        if Note.Note.get_id(note) == Note.Note.get_id(i):
            Note.Note.set_id(note)
    array_notes.append(note)
    write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")


def show(txt):
    array_notes = read_file()
    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for i in array_notes:
                print(Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Note.Note.get_id(i))
            id = input("\nВведите id заметки: ")
            flag = True
            for i in array_notes:
                if id == Note.Note.get_id(i):
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой!")


def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = read_file()
    flag = False

    for i in array_notes:
        if id == Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        write_file(array_notes, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Note.Note.get_id(i):
            i.title = input("измените  заголовок:\n")
            i.body = input("измените  описание:\n")
            Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        write_file(array_notes_new, 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("нет такого id")
        
        
def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('журнал заметок пустой')
    finally:
        return array
    
def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close
        