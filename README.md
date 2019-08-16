# storyboarding_data

This repository includes scripts to scrape data corresponding to the paper:
Storyboarding of Recipes: Grounded Contextual Generation

Link: https://www.aclweb.org/anthology/P19-1606

To download the text part and the corresponding image ids from both instrutables and snapguide, run the following command:

$ python get_storyboard_data.py

This forms instructables.json and snapguide.json separately.

Using each of the files, you can download the images by running:

$ python download_images.py
