from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
#from ecommbot.retrieval_generation import generation
#from ecommbot.ingest import ingestdata

app = Flask(__name__)

load_dotenv()

#vstore=ingestdata("done")
#chain=generation(vstore)

@app.route("/")
def index():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(debug= True)