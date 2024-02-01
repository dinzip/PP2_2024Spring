from Dict_of_movies import movies

def category_imdb(cat):
    sum = t = 0
    for i in movies:
        if i['category'] == cat:
                sum += i['imdb']
                t += 1
    return sum / t

# print(category_imdb('Thriller'))