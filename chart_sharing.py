# pasta's script to automate getting level data for chart sharing
import json

with open('level.json', 'r', encoding = 'utf-8') as f:
    level = json.load(f)

def list_difficulties():
    difficulty_list = []

    for chart in level['charts']:
        difficulty_list.append(chart['difficulty'])
    
    difficulty_list.sort()
    return difficulty_list

charter = level['charter']
artist = level['artist']
title = level['title']
difficulties = list_difficulties()


print('Post title:')
print(f"[{charter}] {artist} - {title}\n")

print('Description:')
print(f"""Title: {title}
Level ID: {level['id']}
Artist: {artist}
Charter: {charter}""")
if (len(difficulties) == 1):
    print('Difficulty: ', end = '')
else:
    print('Difficulties: ', end = '')
print(*difficulties, sep = ', ')
print(f'Illustrator: {level["illustrator"]}')
