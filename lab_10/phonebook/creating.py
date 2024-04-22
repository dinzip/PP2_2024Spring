import psycopg2, tools

connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='1234', port='5432')

create_phonebook_table = '''
    CREATE TABLE IF NOT EXISTS Phone_book(
        PHONE_NUMBER TEXT PRIMARY KEY NOT NULL,
        NAME TEXT,
        SURNAME TEXT
    )
'''

cursor = connection.cursor()
cursor.execute('DROP TABLE Phone_book')
# creating table:
try:
    cursor.execute(create_phonebook_table)
    connection.commit()
    print('created')
except Exception as error:
    print(f'Error: {error}')

connection.close()
