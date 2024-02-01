from Dict_of_movies import movies

def average_imdb(l):
    sum = 0
    for names in l:
        for id in movies:
            if id['name'] == names:
                sum += id['imdb']
                break
    return sum / len(l)

# print(average_imdb(["Bride Wars", "Love", "Colonia", "The Help", "Usual Suspects"]))