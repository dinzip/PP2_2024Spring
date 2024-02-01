from Dict_of_movies import movies

def check(name):
    for i in movies:
        if i["name"] == name:
            return i["imdb"] > 5.5
    return False