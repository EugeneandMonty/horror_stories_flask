from flask import Flask, jsonify, request
import os
from mongoengine import *
from models import Stories
from test_data import data, listready

password = os.environ.get("PASSWORD")
connect(host=f"mongodb+srv://Eugene:{password}@cluster.7wvqvhu.mongodb.net/horror_stories")

for num in range (0, 6):
    story = Stories(
        title = data[num]['title'],
        story = data[num]['story'],
        story_image = listready[num],
        tags = data[num]['tags'].replace(',', '').split(),
        short_description = str(data[num]['short_description'])[:100],
        author = data[num]['author'],
        likes = data[num]['likes']
    )

    # story.save()

app = Flask(__name__)

@app.route('/mainquery', methods=['GET'])
def query():
    list_stories = []
    stories = Stories.objects()
    for each in stories:
        x = {
            'title': each.title,
            'story': each.story,
            'story_image': each.story_image,
            'tags': each.tags,
            'short_description': each.short_description,
            'author': each.author,
            'likes': each.likes
        }
        list_stories.append(x)
    return jsonify(list_stories)


if __name__ == "__main__":
    app.run(debug=True)


disconnect(alias='hororr_stories')
