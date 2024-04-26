import psycopg2

connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='1234', port='5432')
cursor = connection.cursor()

def create_query(query):
    try:
        cursor.execute(query)
        connection.commit()
        print('created!')
    except Exception as error:
        print('ERROR:', error)
def query_function(func_name, variables):
    try:
        cursor.callproc(func_name, variables)
        print('RESULT:')
        print('{:20}{:15}{}'.format('phone_number', 'name', 'surname'))
        for row in cursor.fetchall():
            print('{:-<20}{:-<15}{}'.format(row[0], row[1], row[2]))
    except Exception as error:
        print('ERROR:', error)


''' 
    1-st task:
        Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
'''

func_record_pattern = '''
    DROP FUNCTION IF EXISTS record_by_{0};
	
    CREATE OR REPLACE FUNCTION record_by_{0}(IN pattern TEXT)
    RETURNS TABLE(sel_number TEXT, sel_name TEXT, sel_surname TEXT)
    AS 
    $$
    BEGIN
        RETURN QUERY

        SELECT phone_book.phone_number, phone_book.name, phone_book.surname
        FROM phone_book
        WHERE {0} ILIKE '%'||pattern||'%';
    END;
    $$
    LANGUAGE plpgsql;
'''

func_record_pattern_name = func_record_pattern.format('name')
func_record_pattern_surname = func_record_pattern.format('surname')
func_record_pattern_number = func_record_pattern.format('phone_number')

create_query(func_record_pattern_name)
create_query(func_record_pattern_surname)
create_query(func_record_pattern_number)

def record_by_name(name_pattern):
    query_function('record_by_name', (name_pattern, ))

def record_by_surname(surname_pattern):
    query_function('record_by_surname', (surname_pattern, ))

def record_by_phone_number(number_pattern):
    query_function('record_by_phone_number', (number_pattern, ))

'''
    2-nd task:
        Create procedure to insert new user by name and phone, update phone if user already exists
'''

procedure_insert_query = '''
    CREATE OR REPLACE PROCEDURE insert_or_update(IN new_number TEXT, IN new_name TEXT, IN new_surname TEXT)
    AS
    $$
    BEGIN
        IF EXISTS(SELECT * FROM phone_book WHERE phone_book.name = new_name AND phone_book.surname = new_surname) THEN
            UPDATE phone_book 
            SET phone_number = new_number
            WHERE phone_book.name = new_name AND phone_book.surname = new_surname;
        ELSE
            INSERT INTO phone_book 
            VALUES (new_number, new_name, new_surname);
        END IF;
    END;
    $$

    LANGUAGE plpgsql;
'''

create_query(procedure_insert_query)

def insert_or_update(new_number, new_name, new_surname):
    try:
        cursor.execute('CALL insert_or_update(%s, %s, %s)', (new_number, new_name, new_surname))
        connection.commit()
        print('inserted/updated!')
    except Exception as error:
        print('ERROR:', error)

'''
    4-th task:
        Create function to querying data from the tables with pagination (by limit and offset)
'''

query_limit_offset = '''
    CREATE OR REPLACE FUNCTION query_limit_offset(IN limit_num INT, IN offset_num INT)
    RETURNS TABLE(phone_number TEXT, name TEXT, surname TEXT)
    AS
    $$
    BEGIN
        RETURN QUERY

        SELECT * FROM phone_book 
        LIMIT limit_num
        OFFSET offset_num;
    END;
    $$
    LANGUAGE plpgsql;
'''

create_query(query_limit_offset)
def query_limit_offset(limit, offset):
    query_function('query_limit_offset', (limit, offset))

'''
    5-th task:
        Implement procedure to deleting data from tables by username or phone
'''

deleting_by_name = '''
    CREATE OR REPLACE PROCEDURE deleting_by_name(IN q_name TEXT, IN q_surname TEXT)
    AS
    $$
    BEGIN
        DELETE FROM phone_book 
        WHERE phone_book.name ~~* q_name AND phone_book.surname ~~* q_surname;
    END;
    $$
    LANGUAGE plpgsql;
'''

deleting_by_number = '''
    CREATE OR REPLACE PROCEDURE deleting_by_number(IN q_number TEXT)
    AS
    $$
    BEGIN
        DELETE FROM phone_book 
        WHERE phone_book.phone_number ~~* q_number;
    END;
    $$
    LANGUAGE plpgsql;
'''

create_query(deleting_by_name)
create_query(deleting_by_number)

def deleting_by_name(name, surname):
    try:
        cursor.execute('CALL deleting_by_name(%s, %s)', (name, surname))
        connection.commit()
        print('deleted!')
    except Exception as error:
        print('ERROR:', error)

def deleting_by_number(number):
    try:
        cursor.execute('CALL deleting_by_number(%s)', (number,))
        connection.commit()
        print('deleted!')
    except Exception as error:
        print('ERROR:', error)



query_limit_offset(50, 0)