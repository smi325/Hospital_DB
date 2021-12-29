import psycopg2
import PySimpleGUI as sg
from config import host, user, password, db_name

current_table = None

def requesttables():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            #cursor.execute("select * from pg_tables where schemaname='public';")
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            ret = cursor.fetchall()
    except Exception as _ex:
        #print("[INFO] Error while working with PostgreSQL", _ex)
        pass
    finally:
        if connection:
            connection.close()
            #print("[INFO] PostgreSQL connection closed")
    return ret


def requestrecords(table):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            #cursor.execute("select * from pg_tables where schemaname='public';")
            cursor.execute(f"SELECT * FROM public.\"{table}\";")
            ret = cursor.fetchall()
    except Exception as _ex:
        #print("[INFO] Error while working with PostgreSQL", _ex)
        pass
    finally:
        if connection:
            connection.close()
            #print("[INFO] PostgreSQL connection closed")
    return ret


def addrecord(table, args):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        tmp = ""
        for i in args:
            tmp += ", '" + i + "'"
        with connection.cursor() as cursor:
            #cursor.execute("select * from pg_tables where schemaname='public';")
            #cursor.execute(f"""INSERT INTO Patient (name, sex, age) VALUES (abc, def, ghj);""")
            postgres_insert_query = f" INSERT INTO public.\"{table}\" VALUES ({tmp[2:]})"
            #record_to_insert = ('asdda', 'One Plus 6', 'dfg')

            cursor.execute(postgres_insert_query, args)
            connection.commit()
    except Exception as _ex:
        #print("[INFO] Error while working with PostgreSQL", _ex)
        pass
    finally:
        if connection:
            connection.close()
            #print("[INFO] PostgreSQL connection closed")

def getattributes(table):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM public.\"{table}\" LIMIT 0;")
            colnames = [desc[0] for desc in cursor.description]

    except Exception as _ex:
        #print("[INFO] Error while working with PostgreSQL", _ex)
        pass
    finally:
        if connection:
            connection.close()
    return colnames
def deleterecord(table, args):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            #cursor.execute("select * from pg_tables where schemaname='public';")
            #cursor.execute(f"""INSERT INTO Patient (name, sex, age) VALUES (abc, def, ghj);""")
            #cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = public.\"Hospital\";");
            colnames = getattributes(table)
            tmp = ""
            for i in colnames:
                tmp += ", " + i
            postgres_insert_query = f"DELETE FROM public.\"{table}\" WHERE ({tmp[2:]}) = {args};"
            ##record_to_insert = ('asdda', 'One Plus 6', 'dfg')

            cursor.execute(postgres_insert_query, args)
            connection.commit()
    except Exception as _ex:
        #print("[INFO] Error while working with PostgreSQL", _ex)
        pass
    finally:
        if connection:
            connection.close()
            #print("[INFO] PostgreSQL connection closed")

def updaterecord(table, args, new_args):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            #cursor.execute("select * from pg_tables where schemaname='public';")
            #cursor.execute(f"""INSERT INTO Patient (name, sex, age) VALUES (abc, def, ghj);""")
            #cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = public.\"Hospital\";");
            colnames = getattributes(table)
            tmp = ""
            for i in colnames:
                tmp += ", " + i
            tmp_2 = ""
            for i in new_args:
                tmp_2 += ", '" + i + "'"
            cursor.execute(f"UPDATE public.\"{table}\" SET ({tmp[2:]}) = ({tmp_2[2:]}) WHERE ({tmp[2:]}) = {args};")
            #cursor.execute(postgres_insert_query, args)
            ##record_to_insert = ('asdda', 'One Plus 6', 'dfg')

            #cursor.execute(postgres_insert_query, new_args)
            connection.commit()
    except Exception as _ex:
        #print("[INFO] Error while working with PostgreSQL", _ex)
        pass
    finally:
        if connection:
            connection.close()
            #print("[INFO] PostgreSQL connection closed")

def findrecords(table, args):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            #cursor.execute("select * from pg_tables where schemaname='public';")
            cursor.execute(f"SELECT * FROM public.\"{table}\" WHERE {args};")
            ret = cursor.fetchall()
    except Exception as _ex:
        #print("[INFO] Error while working with PostgreSQL", _ex)
        pass
    finally:
        if connection:
            connection.close()
            #print("[INFO] PostgreSQL connection closed")
    return ret

def open_window(atr, vals, find):
    if find == False:
        tmp = ""
        if vals != None:
            for i in vals:
                tmp += "/" + i
            tmp = tmp[1:]
    if find == True:
        tmp = ""
        if vals != None:
            for i in vals:
                tmp += i + " IS NOT NULL AND "
            tmp = tmp[:len(tmp)-5]
    layout_1 = [[sg.Text("Введите ВСЕ значения атрибутов через слэш - \"/\":", key="new")], [sg.Text("Данная таблица содержит следующие атрибуты: " + str(atr))], [sg.InputText(default_text=tmp, key='inp'), sg.Button('ПРИМЕНИТЬ', size=(23, 1))], [sg.Text("Для поиска по ключам замените *IS NOT NULL* на *='<нужное значение параметра>'*", key="new", visible = True if find else False)], [sg.Text("Пример: ...name ='Sergey' AND...", key="new", visible = True if find else False)], [sg.Text("Если не трогать условия, будут показаны все записи текущей таблицы", key="new", visible = True if find else False)]]
    window_1 = sg.Window("Second Window", layout_1, modal=True)
    choice = None

    while True:
        event, values = window_1.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'ПРИМЕНИТЬ':
            window_1.close()
            return window_1['inp'].get()


    window.close()
layoutTable = [
    [ sg.Listbox(values=requesttables(), select_mode = True, right_click_menu=['&Right', ['Показать все записи']], enable_events=True, size=(80, 40), key="-TABLE MENU-"), sg.Text("Вы просматриваете все таблицы.\nЧтобы просмотреть записи\nконкретной таблицы:\n1. Выделите её (ЛКМ)\n2. Вызовите меню действий (ПКМ)\n\n Для взаимодействия с записями\n так же используйте меню,\n вызываемое ПКМ,\n предварительно выбрав нужную.")]
]

layoutRecords = [
    [sg.Text("", key="attrs")],[sg.Listbox(values=[], select_mode = True, right_click_menu=['&Right', ['Удалить запись', 'Добавить запись', 'Обновить запись', 'Найти запись по ключу(-ам)']], enable_events=True, size=(80, 40), key="-RECORDS LIST-"), sg.Button('Вернуться к таблицам', size=(23, 1))]
]

layout = [[sg.Column(layoutTable, key='-COL1-',  visible=True), sg.Column(layoutRecords, key='-COL2-',  visible=False)]]

window = sg.Window('БДСМ (не Сергея Михайловича, а Сладкова Михаила) v1.0', layout, size=(840, 650))
layout = 1
while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if layout == 1:
        if event == "Показать все записи":
            if len(window['-TABLE MENU-'].get()) != 0:
                window[f'-COL{layout}-'].update(visible=False)
                layout = 2
                window[f'-COL2-'].update(visible=True)
                window['attrs'].update(value=getattributes(window['-TABLE MENU-'].get()[0][0]))
                window.Element('-RECORDS LIST-').Update(values=requestrecords(window['-TABLE MENU-'].get()[0][0]))
    if layout == 2:
        if event == "Вернуться к таблицам":
            window[f'-COL{layout}-'].update(visible=False)
            layout = 1
            window[f'-COL1-'].update(visible=True)
            window.Element('-TABLE MENU-').Update(values=requesttables())
        if event == "Добавить запись":
            tmp = open_window(getattributes(window['-TABLE MENU-'].get()[0][0]), None, False)
            if tmp != None:
                args = tmp.split("/")
                addrecord(window['-TABLE MENU-'].get()[0][0], args)
                window.Element('-RECORDS LIST-').Update(values=requestrecords(window['-TABLE MENU-'].get()[0][0]))
        if event == "Удалить запись":
            if len(window['-RECORDS LIST-'].get()) != 0:
                args = window['-RECORDS LIST-'].get()[0]
                deleterecord(window['-TABLE MENU-'].get()[0][0], args)
                window.Element('-RECORDS LIST-').Update(values=requestrecords(window['-TABLE MENU-'].get()[0][0]))
        if event == "Обновить запись":
            if len(window['-RECORDS LIST-'].get()) != 0:
                tmp = open_window(getattributes(window['-TABLE MENU-'].get()[0][0]), window['-RECORDS LIST-'].get()[0], False)
                if tmp != None:
                    args = window['-RECORDS LIST-'].get()[0]
                    updaterecord(window['-TABLE MENU-'].get()[0][0], args, tmp.split("/"))
                    window.Element('-RECORDS LIST-').Update(values=requestrecords(window['-TABLE MENU-'].get()[0][0]))
        if event == "Найти запись по ключу(-ам)":
            tmp = open_window(getattributes(window['-TABLE MENU-'].get()[0][0]), getattributes(window['-TABLE MENU-'].get()[0][0]), True)
            if tmp != None:
                window.Element('-RECORDS LIST-').Update(values=findrecords(window['-TABLE MENU-'].get()[0][0], tmp))
