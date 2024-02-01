from Dict_of_movies import movies
def sublist_above_5p5():
    l = []
    for i in movies:
        if i["imdb"] > 5.:
            l.append(i["name"])
    return l