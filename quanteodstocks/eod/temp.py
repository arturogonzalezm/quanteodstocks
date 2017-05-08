import paramiko
import logging
import socket
import os
import shutil
from settings import SSH, REMOTE_DIR, LOCAL_DIR, LOCAL_TEMP

logger = logging.getLogger('SFTP')


class SFTP(object):
    def __init__(self):
        self.sftp_client = paramiko.SSHClient()
        self.private_key = paramiko.RSAKey.from_private_key_file(SSH['pkey_path'])
        self.local_tmp_dir = LOCAL_TEMP
        self.local_destination = LOCAL_DIR
        self.remote_dir = REMOTE_DIR
        self.files_to_load = 3
        self.number_of_try = 10

    def load_files(self):
        self.sftp_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        conn = self.sftp_client.connect(SSH['host'], port=SSH['port'], username=SSH['username'],
                                        pkey=self.private_key, timeout=SSH['timeout'],
                                        banner_timeout=SSH['banner_timeout'])

        number_of_files_downloaded = 0
        counter = 1
        while number_of_files_downloaded < self.files_to_load:
            if counter < self.number_of_try:
                logger.info('No.{} try'.format(counter))
                number_of_files_downloaded = self._get_tax_files(conn)
                logger.info('Totally {} files are downloaded'.format(number_of_files_downloaded))
                counter += 1
            else:
                break

        conn.close()

    def _get_tax_files(self, conn):
        """
        This  method is to donwload files start with 'Tax' from remote sftp server
        :param conn: 
        :return: 
        """

        # set remote directory to self._remote_dir
        logger.debug('change remote file dir to {}'.format(self.remote_dir))
        conn.chdir(self.remote_dir)
        filed_downloaded = 0
        for file in conn.listdir(self.remote_dir):
            if file.startswith('Tax'):
                try:
                    # download file from remote direcotory to local temp dir and then moved to local destination
                    logger.info('Transfer of {} is in progress'.format(file))
                    local_tmp_filepath = os.path.join(self.local_tmp_dir, file)
                    local_filepath = os.path.join(self.local_destination, file)
                    remote_file_path = os.path.join(self.remote_dir, file)
                    stat = conn.stat(remote_file_path)
                    conn.get(remote_file_path, local_tmp_filepath)
                    logger.info('{file} is downloaded to {localdir}, size: {size}'.format(
                        file=remote_file_path, localdir=local_tmp_filepath, size=stat.st_size))
                    if os.path.exists(remote_file_path):
                        os.remove(remote_file_path)
                    shutil.move(local_tmp_filepath, local_filepath)
                    logger.info('{file} is moved to {localdir}, size: {size}'.format(
                        file=local_tmp_filepath, localdir=local_filepath, size=stat.st_size))
                    filed_downloaded += 1
                except (socket.error, paramiko.SSHException, OSError):
                    logger.exception('Failed @ {}'.format(file))

        return filed_downloaded


