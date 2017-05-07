import time
import os
import pandas as pd
import sqlalchemy as sa

from quanteodstocks.eod.constants import TABLE_COLUMNS, DB_CONNECTION, TABLE_COLUMN_TYPE, latest_partial_file

con = sa.create_engine(DB_CONNECTION)
list_of_files = latest_partial_file
latest_partial = max(list_of_files, key=os.path.getctime)
chunks = pd.read_csv(latest_partial, chunksize=100000, parse_dates=True, keep_date_col=True,
                     names=TABLE_COLUMNS)

for chunk in chunks:
    t = time.process_time()
    elapsed_time = time.process_time() - t
    print('-> Loading back history partial data to MySQL is taking {}'.format(elapsed_time) + ' seconds.')
    chunk.to_sql(name='test', if_exists='append', con=con, index=True, dtype=TABLE_COLUMN_TYPE)

    t = time.process_time()
    elapsed_time = time.process_time() - t
    print('-> Total elapsed time was {}'.format(elapsed_time) + ' seconds.')
print('-> File {}'.format(latest_partial) + ' loaded successfully!')
