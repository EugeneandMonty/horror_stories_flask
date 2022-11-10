from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from mongoengine import *
from models import Stories, Authors, Comments, short_for_loop_json, long_for_loop_json
from test_data import data, listready

password = os.environ.get("PASSWORD")
connect(host=f"mongodb+srv://Eugene:{password}@cluster.7wvqvhu.mongodb.net/horror_stories")

for num in range (0, 51):
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

CORS(app)

@app.route('/shortall', methods=['GET'])
def short_query():
    stories = Stories.objects()
    list_stories = short_for_loop_json(stories)
    return list_stories

@app.route('/longone', methods=['GET'])
def long_query():
    stories = Stories.objects()
    list_stories = long_for_loop_json(stories)
    return list_stories

if __name__ == "__main__":
    app.run(debug=True)

disconnect(alias='hororr_stories')
