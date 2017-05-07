import zipfile, urllib.request, shutil
from quanteodstocks.eod.constants import master_data, master_data_file, unzip_master_to

url = master_data
file_name = master_data_file

with urllib.request.urlopen(url) as response, open(file_name, mode='wb') as out_file:
    shutil.copyfileobj(response, out_file)
    print('-> Downloading EOD file . . .')
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall(unzip_master_to)
        print('-> Unzipping EOD file . . .')
        zf.close()
print('-> Done!')


# command-line: python -m zipfile -e data/EOD.zip data/
