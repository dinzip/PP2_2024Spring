import psycopg2, game_objects


def open():
    global connection, cursor
    connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='1234', port='5432')
    cursor = connection.cursor()

def close():
    global connection
    connection.close()

def find_name(user_name):
    open()
    find_name_query = '''
        SELECT * FROM snake
        WHERE user_name = %s
    '''
    answer = []
    try:
        cursor.execute(find_name_query, (user_name, ))
        answer = cursor.fetchall()
    except Exception as error:
        print("ERROR:", error)
    close()
    return answer

def create_new_user(user_name):
    open()
    insert_query = '''
        INSERT INTO snake
        VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor.execute(insert_query, (user_name, 1, 0, ''))
        connection.commit()
        print('created')
    except Exception as error:
        print("ERROR:", error)
    close()

def points_to_text(points):
    res = ''
    for id, point in enumerate(points):
        res += f'{point.x}:{point.y}'
        if id < len(points)-1:
            res += ';'
    print(res)
    return res

def update_information(user_name, lvl, score, points):
    open()
    update_query = '''
        UPDATE snake 
        SET lvl = %s, score = %s, points_snake = %s
        WHERE user_name = %s
    '''
    try:
        cursor.execute(update_query, (lvl, score, points_to_text(points), user_name ))
        connection.commit()
    except Exception as error:
        print("ERROR:", error)
    close()

def text_to_points(text): # 100:200;120:400;740:20;474:10
    points = []
    id = 0
    while len(text) > 0:
        x = int(text[:text.find(':')])
        text = text[text.find(':')+1 : ]
        if text.find(';') > 0:
            y = int(text[:text.find(';')])
        else:
            y = int(text)
            text = ''
        text = text[text.find(';')+1 : ]
        # print(x, y)
        points.append(game_objects.Point(x, y))
    return points
# text_to_points('100:200;120:400;740:20;474:10')