#else:
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#if loop executed by break, else doesn't work
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")