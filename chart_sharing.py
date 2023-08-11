"""pasta's script to automate getting level data for chart sharing"""
import json
import sys
from urllib.parse import urlparse

encodings = ['utf-8', 'utf-16']
for enc in encodings:
    try:
        with open('level.json', 'r', encoding = enc) as f:
            level = json.load(f)
    except UnicodeDecodeError:
        if encodings.index(enc) == (len(encodings) - 1):
            print('Unsupported file encoding.')
            print('Please re-encode your level.json with UTF-8 or UTF-16.')
            sys.exit()
    else:
        break

def is_valid_url(string):
    """Checks whether the string is a valid URL."""
    parsed = urlparse(string)
    return (parsed.scheme and parsed.netloc)
def is_valid_key(string):
    """Checks whether the given string is a valid key."""
    return (string in level and not (string is None) and len(string.strip()) > 0)
def print_title():
    """Print the title and localized title if it exists."""
    if is_valid_key('title_localized'):
        print(f'Title: {title}（{level["title_localized"]}）')
    else:
        print(f'Title: {title}')

def print_difficulties():
    """Print the list of chart difficulties."""
    difficulty_list = []

    for chart in level['charts']:
        difficulty_list.append(chart['difficulty'])

    difficulty_list.sort()
    if len(difficulty_list) == 1:
        print('Difficulty: ', end = '')
    else:
        print('Difficulties: ', end = '')
    print(*difficulty_list, sep = ', ')

def print_artist():
    """Print the artist and localized artist if it exists.
    Also links to the source if provided."""
    artist_string = level['artist']
    if is_valid_key('artist_localized'):
        artist_string += '（' + level['artist_localized'] + '）'
    if is_valid_key('artist_source') and is_valid_url(level['artist_source']):
        print(f'Artist: [{artist_string}](<{level["artist_source"]}>)')
    else:
        print(f'Artist: {artist_string}')

def print_illustrator():
    """Print the illustrator name.
    Also links to the source if provided."""
    if is_valid_key('illustrator_source') and is_valid_url(level['illustrator_source']):
        print(f'Illustrator: [{illustrator}](<{level["illustrator_source"]}>)')
    else:
        print(f'Illustrator: {level["illustrator"]}')

charter = level['charter']
artist = level['artist']
title = level['title']
illustrator = level['illustrator']


print('Post title:')
print(f"[{charter}] {artist} - {title}\n")

print('Description:')
print_title()
print(f"Level ID: {level['id']}")
print_artist()
print(f'Charter: {charter}')
print_difficulties()
print_illustrator()
