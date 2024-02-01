from Dict_of_movies import movies

def categories(category):
    l = []
    for i in movies:
        if i["category"] == category:
            l.append(i['name'])
    return l