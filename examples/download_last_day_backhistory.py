import zipfile, urllib.request, shutil
from quanteodstocks.eod.constants import back_history, back_history_file, unzip_partial_to

url = back_history
file_name = back_history_file

with urllib.request.urlopen(url) as response, open(file_name, mode='wb') as out_file:
    shutil.copyfileobj(response, out_file)
    print('-> Downloading EOD partial backhistory file . . .')
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall(unzip_partial_to)
        print('-> Unzipping EOD partial backhistory file . . .')
        zf.close()
print('-> Done!')
