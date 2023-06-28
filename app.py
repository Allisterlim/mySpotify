from flask import Flask, render_template, request
import subprocess 
import os 

app = Flask(__name__)

#important note, when you first create .html and .css files, you need to restart the server to see the changes
@app.route('/', methods=['GET', 'POST'])
def index():
    # with open('outputs\MetaData.txt', 'r') as f:
    #     content = f.read()
    contents = None
    if request.method == 'POST':
        subprocess.call(['python', 'main.py'])
        for filename in os.listdir('outputs'):
            if filename=='MetaData.txt':
                with open(os.path.join('outputs', filename), 'r') as f:
                    contents = f.read()
    return render_template('index.html', contents=contents) #add this back later :, content=content




if __name__ == '__main__':
    app.run(debug=True)