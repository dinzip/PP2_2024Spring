from datetime import *
print("Yesterday: ", (datetime.today() - timedelta(days=1)).strftime('%x'))
print("Today: ", datetime.today().strftime('%x'))
print("Tomorrow: ", (datetime.today() + timedelta(days=1)).strftime('%x'))
