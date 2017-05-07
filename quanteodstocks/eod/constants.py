import sqlalchemy
import glob
import os

# db_connection = 'mysql+pymysql://root:root@127.0.0.1:3306/securities_master'
DB_CONNECTION = 'sqlite:///securities_master.db'

master_data = 'https://www.quandl.com/api/v3/databases/EOD/data?api_key=<YOUR_KEY>'
back_history = 'https://www.quandl.com/api/v3/databases/EOD/data?api_key=<YOUR_KEY>&download_type=partial'

master_data_file = os.path.abspath('~/data/us_market/master_data/EOD.zip')
back_history_file = os.path.abspath('~/data/us_market/partial_backhistory_data/EOD-partial.zip')
unzip_master_to = os.path.abspath('~/data/us_market/master_data/')
unzip_partial_to = os.path.abspath('~/data/us_market/partial_backhistory_data/')
latest_master_file = glob.glob('~/data/us_market/master_data/*.csv')
latest_partial_file = glob.glob('~/data/us_market/partial_backhistory_data/*.csv')

TABLE_COLUMNS = ('ticker',
                 'eod_date',
                 'unadjusted_open',
                 'unadjusted_high',
                 'unadjusted_low',
                 'unadjusted_close',
                 'unadjusted_volume',
                 'dividend',
                 'split',
                 'adjusted_open',
                 'adjusted_high',
                 'adjusted_low',
                 'adjusted_close',
                 'adjusted_volume',
                 )

# For MySQL and PostgreSQL
TABLE_COLUMN_TYPE = {'ticker': sqlalchemy.String(length=25),
                     'eod_date': sqlalchemy.Date(),
                     'unadjusted_open': sqlalchemy.Float(precision=3, asdecimal=True),
                     'unadjusted_high': sqlalchemy.Float(precision=3, asdecimal=True),
                     'unadjusted_low': sqlalchemy.Float(precision=3, asdecimal=True),
                     'unadjusted_close': sqlalchemy.Float(precision=3, asdecimal=True),
                     'unadjusted_volume': sqlalchemy.Float(precision=3, asdecimal=True),
                     'dividend': sqlalchemy.Float(precision=3, asdecimal=True),
                     'split': sqlalchemy.Float(precision=3, asdecimal=True),
                     'adjusted_open': sqlalchemy.Float(precision=3, asdecimal=True),
                     'adjusted_high': sqlalchemy.Float(precision=3, asdecimal=True),
                     'adjusted_low': sqlalchemy.Float(precision=3, asdecimal=True),
                     'adjusted_close': sqlalchemy.Float(precision=3, asdecimal=True),
                     'adjusted_volume': sqlalchemy.Float(precision=3, asdecimal=True)
                     }
