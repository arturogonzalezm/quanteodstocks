import time
import os
import pandas as pd
import sqlalchemy as sa

from quanteodstocks.eod.constants import TABLE_COLUMNS, DB_CONNECTION, TABLE_COLUMN_TYPE, latest_master_file

con = sa.create_engine(DB_CONNECTION)
list_of_files = latest_master_file
latest_master = max(list_of_files, key=os.path.getctime)
chunks = pd.read_csv(latest_master, chunksize=100000, parse_dates=True, keep_date_col=True, names=TABLE_COLUMNS)

for chunk in chunks:
    t = time.process_time()
    elapsed_time = time.process_time() - t
    print('Loading Master Data to mysql and the estimated time is: {}'.format(
        elapsed_time) + ' seconds. Please wait . . .')
    chunk.to_sql(name='eod_us', if_exists='append', con=con, index=True, dtype=TABLE_COLUMN_TYPE)

t = time.process_time()
elapsed_time = time.process_time() - t
print('Total Elapsed Time: {}'.format(elapsed_time))
print("Data has been loaded into mysql successfully!")
