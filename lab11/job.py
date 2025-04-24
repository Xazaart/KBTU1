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

def check(name, phone_number):
    """ Проверка, существует ли пользователь с таким именем, и обновление или добавление записи """
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверка, существует ли пользователь с таким именем
                cur.execute("""
                    SELECT 1 FROM phonebook WHERE first_name = %s LIMIT 1;
                """, (name,))
                
                if cur.fetchone() is not None:
                    print("Пользователь существует. Обновляем номер телефона.")
                    update_vendor(phone_number, name)  # Обновляем номер телефона, если пользователь существует
                else:
                    print("Пользователь не найден. Добавляем новый.")
                    insert_vendor(name, phone_number)  # Добавляем нового пользователя, если не существует
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при проверке пользователя:", error)

def insert_vendor(first_name, phone_number):
    """ Вставка нового пользователя в таблицу phonebook """
    sql = """INSERT INTO phonebook(first_name, phone_number)
             VALUES(%s, %s) RETURNING contact_id;"""

    contact_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Выполнение INSERT запроса
                cur.execute(sql, (first_name, phone_number))

                # Получаем сгенерированный id
                rows = cur.fetchone()
                if rows:
                    contact_id = rows[0]

                # Фиксация изменений в базе данных
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при вставке данных:", error)
    finally:
        return contact_id

def update_vendor(phone_number, name):
    """ Обновление номера телефона для пользователя по имени """
    sql = """UPDATE phonebook
             SET phone_number = %s
             WHERE first_name = %s"""

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Выполнение UPDATE запроса
                cur.execute(sql, (phone_number, name))
                updated_row_count = cur.rowcount
            # Фиксация изменений в базе данных
            conn.commit()
            print(f"Обновлено {updated_row_count} записей.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при обновлении данных:", error)

def validate_phone_number(phone_number):
    """
    Validate if the phone number is a valid 10-digit number.
    """
    return bool(re.match(r'^\d{10}$', phone_number))  # 10-digit number check

def insert_users(names, phones):
    config = load_config()
    invalid_data = [] 
    successful_inserts = 0

    try:

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for name, phone in zip(names, phones):
   
                    if validate_phone_number(phone):

                        try:
                            cur.execute("""
                                INSERT INTO phonebook (first_name, phone_number)
                                VALUES (%s, %s)
                            """, (name, phone))
                            successful_inserts += 1
                        except psycopg2.DatabaseError as e:
                            print(f"Error inserting {name} with phone {phone}: {e}")
                    else:
                        invalid_data.append(f"{name} - {phone}")

                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting records:", error)


    if invalid_data:
        print("Invalid data found:")
        for data in invalid_data:
            print(data)
    else:
        print("All data inserted successfully.")

    print(f"Total successful inserts: {successful_inserts}")

if __name__ == '__main__':
    mode = input("Что будем делать?: ")

    if mode == "p":
        pattern = input("Введите паттерн для поиска (например, часть имени или номера телефона): ")
        search_records(pattern)

    if mode == "i":
        name = input("Введите имя: ")
        number = input("Введите номер телефона: ")
        check(name, number)

    if mode == "m":
        names = ['Alice', 'Bob', 'Charlie', 'David']
        phones = ['1234567890', '987654a21', '1122334455', '1234']

        insert_users(names, phones)
