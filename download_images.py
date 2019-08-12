import json
import os

recipes = json.load(open("./instructables.json", 'r'))

for recipe in recipes:
    context = recipe['context']
    for step in context:
        step_images = step['step_images']
        for img in step_images:
            os.system('wget -O '+ img[1] +' img[0]')
