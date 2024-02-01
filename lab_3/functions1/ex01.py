def gram_to_ounce(x):
    return 28.3495231 * x

gram = int(input())
ounce = gram_to_ounce(gram)

print(ounce)