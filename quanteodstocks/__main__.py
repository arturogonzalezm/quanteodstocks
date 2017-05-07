from quanteodstocks.eod.database import LoadEngine
import logs

logs.init()
worker = LoadEngine()
worker.load(everyday=False)

# task_allocation = thread_management
