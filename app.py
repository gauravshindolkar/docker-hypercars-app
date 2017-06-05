from flask import Flask, render_template
import random

app = Flask(__name__)

# list of car images
images = [
    "https://media.giphy.com/media/3o7abLiNUwnxRhQGME/giphy.gif",
    "https://media.giphy.com/media/uCPmqlHKSNZrG/giphy.gif",
    "https://media.giphy.com/media/ZAkltzJTslMSQ/giphy.gif",
    "https://media.giphy.com/media/Pbze4qQvrvagw/giphy.gif",
    "https://media.giphy.com/media/7jEqpAevFtuWQ/giphy.gif",
    "https://media.giphy.com/media/1432wQNLGP5Qty/giphy.gif",
    "https://media.giphy.com/media/nnrxk2VhBByxO/giphy.gif",
    "https://media.giphy.com/media/xqeOvi8mwo3yU/giphy.gif",
    "https://media.giphy.com/media/MK27hITj2n4d2/giphy.gif",
    "https://media.giphy.com/media/ErpkgJJ480WOY/giphy.gif",
    "https://media.giphy.com/media/RHtk9vcmlxeA8/giphy.gif",
    "https://media.giphy.com/media/bfd8hxbntgfBu/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
