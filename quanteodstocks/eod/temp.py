import paramiko


class SFTP():
    def __init__(self):
        self.sftp_client = paramiko.SSHClient()
        self.private_key = paramiko.RSAKey.from_private_key_file('path/to/id_rsa/')

    def get_files(self):
        self.sftp_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        conn = self.sftp_client.connect('host', port=22, username='art', pkey=self.private_key, timeout=30,
                                        banner_timeout=45)

        conn.close()

    def sftp_transfer(self, filename, conn):
        print('Transfer of %r is in progress' % filename)

        # sftp = self.sftp_client.open_sftp()
        conn.chdir('/directory/to/file')
        # for filename in sorted(sftp.listdir()):
        #     if filename.startswith('Tax'):
        #         callback_for_filename = functools.partial(sftp_callback, filename)
        #         sftp.get(filename, filename, callback=callback_for_filename)

        latest = 0
        latestfile = None
        files = []

        for file_attr in conn.listdir_attr():
            if file_attr.startswith('Tax'):
                files.append(file_attr)

            if latestfile is not None:
                conn.get(filename)
