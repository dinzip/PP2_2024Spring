
def insert_data():
    return '''
        INSERT INTO phone_book 
        values (%s, %s, %s);
    '''

def delete_by_number():
    return '''
        DELETE FROM phone_book
        WHERE phone_number = %s
    '''

def delete_by_name():
    return '''
        DELETE FROM phone_book
        WHERE name = %s
    '''

def delete_by_surname():
    return '''
        DELETE FROM phone_book
        WHERE surname = %s
    '''

def update_name_by_name():
    return '''
        UPDATE phone_book
        SET name = %s
        WHERE name = %s
    '''

def update_name_by_number():
    return '''
        UPDATE phone_book
        SET name = %s
        WHERE phone_number = %s
    '''

def update_number_by_number():
    return '''
        UPDATE phone_book
        SET phone_number = %s
        WHERE phone_number = %s
    '''

def update_number_by_fullname():
    return '''
        UPDATE phone_book
        SET phone_number = %s
        WHERE name = %s AND surname = %s
    '''

def select_by_names_start():
    return '''
        SELECT * FROM phone_book
        WHERE name LIKE '{}%'
    '''

def select_by_surnames_start():
    return '''
        SELECT * FROM phone_book
        WHERE surname LIKE '{}%'
    '''

def select_by_number_start():
    return '''
        SELECT * FROM phone_book
        WHERE phone_number LIKE '{}%'
    '''