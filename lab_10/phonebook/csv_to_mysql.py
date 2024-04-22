import psycopg2, tools
import pandas as pd
connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='1234', port='5432')



data = pd.read_csv(r"phonebook\data.csv")
df = pd.DataFrame(data)
# print(df)

cursor = connection.cursor()

for row in df.itertuples():
    print(row.phone_number)
    cursor.execute(
        """
        INSERT INTO phone_book (phone_number, name, surname)
        VALUES (%s, %s, %s)
        """,
        [row.phone_number,
        row.name,
        row.surname]
    )
connection.commit()
