car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
print(car)

#another change, "color" doesn't exist. Insert "color" with the value "white":
x = car.setdefault("color", "white")

print(x)
print(car)