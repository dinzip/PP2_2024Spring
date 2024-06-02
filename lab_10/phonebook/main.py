import psycopg2, tools

connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='1234', port='5432')

cursor = connection.cursor()

def insert(data_list):
    # print(data_list)
    cursor.execute(tools.insert_data(), data_list)
    connection.commit()


def delete_num(number):
    cursor.execute(tools.delete_by_number(), number)
    connection.commit()

def delete_name(name):
    cursor.execute(tools.delete_by_name(), name)
    connection.commit()

def update_name_by_name(previous_name, new_name):
    cursor.execute(tools.update_name_by_name(), [new_name, previous_name])
    connection.commit()

def update_name_by_number(phone_number, new_name):
    cursor.execute(tools.update_name_by_number(), [new_name, phone_number])
    connection.commit()

def update_number_by_number(previous_number, new_number):
    cursor.execute(tools.update_number_by_number(), [new_number, previous_number])
    connection.commit()

def update_number_by_fullname(name, surname, new_number):
    cursor.execute(tools.update_number_by_fullname(), [new_number, name, surname])
    connection.commit()

def select_by_start_name(start_name):
    cursor.execute(tools.select_by_names_start().format(start_name))
    connection.commit()

def select_by_start_surname(start_surname):
    cursor.execute(tools.select_by_surnames_start().format(start_surname))
    connection.commit()

def select_by_start_number(start_number):
    cursor.execute(tools.select_by_number_start().format(start_number))
    connection.commit()
#insert one more

# data = ['87770292727', 'Daryn', 'Abdykadyr']
# try:
#     insert(data)
# except Exception as error:
#     print("Unexpected error ---", error)

# UPDATING:
# try:
#     # update_name_by_name('Daryn', 'Kes')
#     # update_name_by_number(phone_number = '92012345678', new_name = 'HERO')
#     # update_number_by_number(previous_number = '87012345678', new_number = '87774547145')
#     update_number_by_fullname(name = 'HERO', surname = "Barnes", new_number = '11111111')
#     print('updated')
# except Exception as error:
#     print("Unexpected error ---", error)

# DELETING
# try:
#     # delete_name('Kes')
#     cursor.execute('''
#         DELETE FROM phone_book
#         WHERE name = 'Kes'
#     ''')
#     connection.commit()
#     print('deleted')
# except Exception as error:
#     print("Unexpected error ---", error)

# QUERYING:
try:
    select_by_start_number('9')
    for row in cursor.fetchall():
        print(row)
except Exception as error:
    print("Unexpected error ---", error)
connection.close()
print(1)
