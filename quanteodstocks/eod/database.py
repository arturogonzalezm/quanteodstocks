import logging
import os
import ntpath
import time
import pandas as pd
import sqlalchemy as sa

from quanteodstocks.eod.constants import TABLE_COLUMNS, DB_CONNECTION
from settings import DATA


logger = logging.getLogger('DATABASE')


class LoadEngine():
    def __init__(self, chunksize=100000, parse_dates=True, keep_date_col=True, column_name=TABLE_COLUMNS):
        self.engine = sa.create_engine(DB_CONNECTION)
        self.files_directory = None
        self.chunksize = chunksize
        self.parse_dates = parse_dates
        self.keep_date_col = keep_date_col
        self.column_name = column_name
        self._latest_file = None


    @property
    def market(self):
        return 'us_market',

    @property
    def everyday_dir(self):
        return 'partial_backhistory_data'

    @property
    def history(self):
        return 'master_data'

    def get_latest_file(self, dir):
        if not dir or not ntpath.exists(dir):
            return
        csv_files = []
        for root, _, files in os.walk(dir):
            for file in files:
                if file.endswith('.csv'):
                    csv_files.append(os.path.join(root, file))

        return max(csv_files, key=os.path.getctime) if csv_files else ''

    def _load(self, file_to_load):

        if not file_to_load or not os.path.exists(file_to_load):
            logger.info('File empty or not exists')
            return
        logger.info('start loading')
        try:
            chunks = pd.read_csv(file_to_load, chunksize=100000, parse_dates=True, keep_date_col=True,
                                 names=self.column_name)

            for chunk in chunks:
                t = time.process_time()
                elapsed_timer = time.process_time() - t
                logger.debug('Loading Master Data to mysql and the estimated time is: {}'.format(
                    elapsed_timer) + ' seconds. Please wait . . .')
                chunk.to_sql(name='eod_us', if_exists='append', con=self.engine, index=True)
        except:
            logger.info('Load failed')
        finally:
            logger.info('Finished loading')

    def load(self, everyday=True):
        target_data_location = self.everyday_dir if everyday else self.history
        for market in self.market:
            dir_to_search = os.path.join(DATA, market, target_data_location)
            logger.info('Load latest file from {}'.format(dir_to_search))
            latest_file = self.get_latest_file(dir_to_search) or 'N/A'
            logger.info('The file to load: {}'.format(latest_file))
            if not latest_file:
                continue
            self._load(latest_file)

