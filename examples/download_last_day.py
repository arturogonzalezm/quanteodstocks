import zipfile, urllib.request, shutil

url = 'https://www.quandl.com/api/v3/databases/EOD/data?api_key=<YOUR_KEY>&download_type=partial'
file_name = 'EOD.partial.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    print('Unzipping EOD partial file . . .')
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()

print('Done!')
