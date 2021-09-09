import json


class Countries:

    def __init__(self, file):
        with open(file,'r', encoding='utf-8') as f:
            self.countries = json.load(f)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration
        new_name = self.countries.pop().get('name').get('common')
        new_link = 'https://en.wikipedia.org/wiki/' + new_name.replace(' ','_')
        return new_name, new_link


countries = Countries('countries.json')


with open('names_links.txt', 'w', encoding='utf-8') as file:
    for name, link in countries:
        string = name + ' - ' + link + '\n'
        file.write(string)

