from sys import argv
import requests

print('''
___________________________________
|site status code checker by pr0xy|
```````````````````````````````````
''')

file = argv[1]
if file == '-h':
    print('usage: python statuschecker.py {filenamehere}')
else:
    with open(file, "r") as a_file:
        for line in a_file:
            url = line.strip()
            try:
                r = requests.get(url)
                print(f'{url} - {r.status_code}')
            except:
                print(f'an error occured while trying to get response from {url} please re-check the url')
    