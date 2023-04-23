import sqlite3

import pandas as pd

query = '''
select *
from core_link
where player = 'Y' and current = 1
'''

db_path = "../../data/external/db.sqlite3"

with sqlite3.connect(db_path) as conn:
    c = conn.cursor()
    c.execute(query)
    raw_data = c.fetchall()
    df = conn.execute('select * from core_link')

names = list(map(lambda x: x[0], df.description))
print(names)

df_lk = pd.DataFrame(raw_data, columns=names)

df_lk.to_csv("../../data/processed/core_link.csv", header=True)
