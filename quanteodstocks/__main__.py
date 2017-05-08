from quanteodstocks.eod.database import LoadEngine
from quanteodstocks.eod.temp import SFTP
import logs


logs.init()
worker = LoadEngine()
worker.load(everyday=False)

# task_allocation = thread_management
sftp = SFTP()
sftp.load_files()