from Dict_of_movies import movies
def sublist_above_5p5():
    l = [i["name"] for i in movies if i["imdb"] > 5.5]
    return l

# print(sublist_above_5p5())