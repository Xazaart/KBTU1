import psycopg2
import csv
from config import load_config


def insert_vendor(first_name, phone_number):
    """ Insert a new vendor into the vendors table """

    sql = """INSERT INTO vendors(first_name, phone_number)
             VALUES(%s, %s) RETURNING contact_id;"""

    contact_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (first_name, phone_number))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    contact_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return contact_id
    
def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table  """


    sql = "INSERT INTO phonebook(first_name, phone_number) VALUES(%s, %s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.executemany(sql, vendor_list)

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def take_data(file_name):

    vendor_list = []

    with open(file_name, "r", encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f, delimiter=';')
        for row in csv_reader:
            first_name = row["Name"]
            phone_number = row["Number"]
            vendor_list.append((first_name, phone_number))

    insert_many_vendors(vendor_list)

def update_vendor(vendor_id, vendor_data):
    """ Update vendor name based on the vendor id """
    a = input("Что обновляем: name или phone? ")

    updated_row_count = 0
    if a == "name":
        sql = """ UPDATE vendors
                    SET first_name = %s
                    WHERE contact_id = %s"""
    elif a == "phone":
        sql = """ UPDATE vendors
                    SET phone_number = %s
                    WHERE contact_id = %s"""
        
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (vendor_data, vendor_id))
                updated_row_count = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

def get_vendors():
    """ Retrieve data from the vendors table with sorting option """

    a = input("Сортировать по (name / id / phone): ").strip().lower()

    order_column = {
        "name": "first_name",
        "id": "contact_id",
        "phone": "phone_number"
    }.get(a)

    if not order_column:
        print("Неверный ввод! Введите 'name', 'id' или 'phone'.")
        return

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vendors ORDER BY {order_column}")
                rows = cur.fetchall()

                print(f"\nНайдено записей: {len(rows)}\n")
                for row in rows:
                    print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка:", error)

def delete_vendor():
    a = input("Удалить по 'name' или по 'phone': ").strip().lower()

    order_column = {
        "name": "first_name",
        "phone": "phone_number"
    }.get(a)

    value = input(f"Введите значение для удаления по {a}: ").strip()

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM vendors WHERE {order_column} = %s", (value,))
                deleted_count = cur.rowcount
                conn.commit()

                if deleted_count:
                    print(f"Удалено записей: {deleted_count}")
                else:
                    print("Совпадений не найдено.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка:", error)


if __name__ == '__main__':

    mode = input("Что будем делать? ")

    if mode == "i":
        name = input("Ведите имя: ")
        number = input("Ведите номер телефона: ")
        insert_vendor(name, number)
    
    if mode == "c":
        csv_data = take_data("contacts.csv")

    if mode == "u":
        update_data = input("Ваш текст: ")
        vendor_id = int(input("ID: "))
        update_vendor(vendor_id, update_data)

    if mode == "q":
        get_vendors()

    if mode == "d":
        delete_vendor()