from Dict_of_movies import movies

def average_imdb(l):
    d = [i["imdb"] for i in movies if i["name"] in l]
    return sum(d)/len(l)

# print(average_imdb(["Bride Wars", "Love", "Colonia", "The Help", "Usual Suspects"]))
