from Dict_of_movies import movies

def categories(category = "Romance"):
    l = [i['name'] for i in movies if i['category']==category]
    return l

# print(categories())