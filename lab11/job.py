import psycopg2
from config import load_config
import re

def search_records(pattern):
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                query = """
                    SELECT * FROM phonebook
                    WHERE first_name LIKE %s OR phone_number LIKE %s;
                """
                cur.execute(query, (f'%{pattern}%', f'%{pattern}%'))
                
                records = cur.fetchall()
                
                if records:
                    for record in records:
                        print(record)
                else:
                    print("No records found.")
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while fetching records:", error)

def check_and_update_or_insert(name, phone_number):
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL check_and_update_or_insert_user(%s, %s);", (name, phone_number))
                conn.commit()
                print(f"Процедура для пользователя {name} завершена.")
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при вызове процедуры:", error)

def validate_phone_number(phone_number):
    return bool(re.match(r'^\d{10}$', phone_number))  # 10-digit number check

def insert_users(names, phones):
    config = load_config()
    invalid_data = [] 
    successful_inserts = 0

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for name, phone in zip(names, phones):
                    if validate_phone_number(phone):  # Проверяем номер
                        try:

                            cur.execute("CALL insert_user(%s, %s);", (name, phone))
                            successful_inserts += 1
                        except psycopg2.DatabaseError as e:
                            print(f"Error inserting {name} with phone {phone}: {e}")
                    else:
                        invalid_data.append(f"{name} - {phone}")

                conn.commit()  # Сохраняем изменения в базе

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting records:", error)

    # Выводим список неверных данных
    if invalid_data:
        print("Invalid data found:")
        for data in invalid_data:
            print(data)
    else:
        print("All data inserted successfully.")

    print(f"Total successful inserts: {successful_inserts}")

def get_paginated_data(limit, offset):

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                query = f"SELECT * FROM phonebook LIMIT %s OFFSET %s"
                cur.execute(query, (limit, offset))

                rows = cur.fetchall()

        cur.close()
        conn.close()

        return rows

    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
        return []

def delete_by_first_name(username):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Явный вызов SQL-процедуры через CALL
                cur.execute("CALL delete_by_nname(%s);", (username,))
                conn.commit()
                print(f"Записи с именем {username} были удалены.")
                
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при удалении записей:", error)

def delete_by_phone(phone):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Явный вызов SQL-процедуры через CALL
                cur.execute("CALL delete_by_phone(%s);", (phone,))
                conn.commit()
                print(f"Записи с именем {phone} были удалены.")
                
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при удалении записей:", error)



if __name__ == '__main__':
    mode = input("Что будем делать?: ")

    if mode == "p":
        pattern = input("Введите паттерн для поиска (например, часть имени или номера телефона): ")
        search_records(pattern)

    if mode == "i":
        name = input("Введите имя: ")
        number = input("Введите номер телефона: ")
        check_and_update_or_insert(name, number)

    if mode == "m":
        names = ['Alice', 'Bob', 'Charli', 'David']
        phones = ['1234567890', '987654a21', '1122334455', '1234']

        insert_users(names, phones)

    if mode == "q":
        data = get_paginated_data(limit=4, offset=5)
        for row in data:
            print(row)
    
    if mode == "d":
        a = input("По какому параметру хотите удалить?(name or phone) ")
        if a == "name":
            name = input()
            delete_by_first_name(name)
        if a == "phone":
            phone = input()
            delete_by_phone(phone)

