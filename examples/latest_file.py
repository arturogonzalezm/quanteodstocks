import os
from quanteodstocks.eod.constants import latest_partial_file

list_of_files = latest_partial_file
latest_partial = max(list_of_files, key=os.path.getctime)
print(latest_partial)
