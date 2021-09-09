import hashlib


def hash_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for link in hash_string('names_links.txt'):
    print(link)

