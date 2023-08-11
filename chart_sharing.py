# pasta's script to automate getting level data for chart sharing
import json
from urllib.parse import urlparse

with open('level.json', 'r', encoding = 'utf-8') as f:
    level = json.load(f)

def is_valid_url(str):
    parsed = urlparse(str)
    return (parsed.scheme and parsed.netloc)
def print_title():
    if ('title_localized' in level and not (level['title_localized'] is None)):
        print(f'Title: {title}（{level["title_localized"]}）')
    else:
        print(f'Title: {title}')

def print_difficulties():
    difficulty_list = []

    for chart in level['charts']:
        difficulty_list.append(chart['difficulty'])
    
    difficulty_list.sort()
    if (len(difficulty_list) == 1):
        print('Difficulty: ', end = '')
    else:
        print('Difficulties: ', end = '')
    print(*difficulty_list, sep = ', ')

def print_artist():
    global artist
    if ('artist_localized' in level and not (level['artist_localized'] is None)):
        artist += '（' + level['artist_localized'] + '）'
    if (is_valid_url(level['artist_source'])):
        print(f'Artist: [{artist}](<{artist_source}>)')
    else:
        print(f'Artist: {level["artist"]}')

def print_illustrator():
    if (is_valid_url(level['illustrator_source'])):
        print(f'Illustrator: [{illustrator}](<{illustrator_source}>)')
    else:
        print(f'Illustrator: {level["illustrator"]}')

charter = level['charter']
artist = level['artist']
title = level['title']
artist_source = level['artist_source']
illustrator = level['illustrator']
illustrator_source = level['illustrator_source']


print('Post title:')
print(f"[{charter}] {artist} - {title}\n")

print('Description:')
print_title()
print(f"Level ID: {level['id']}")
print_artist()
print(f'Charter: {charter}')
print_difficulties()
print_illustrator()
