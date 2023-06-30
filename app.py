from flask import Flask, render_template, request, send_file
import subprocess 
import os 

app = Flask(__name__)

#important note, when you first create .html and .css files, you need to restart the server to see the changes
@app.route('/', methods=['GET', 'POST'])
def index():
    # with open('outputs\MetaData.txt', 'r') as f:
    #     content = f.read()
    contents = None
    image_file = None 
    if request.method == 'POST':
        subprocess.call(['python', 'main.py'])
        for filename in os.listdir('outputs'):
            if filename=='MetaData.txt':
                with open(os.path.join('outputs', filename), 'r') as f:
                    contents = f.read()
            elif filename=='plot.png':
                image_file = os.path.join('outputs', filename)
    return render_template('index.html', contents=contents, image_file=image_file) 

@app.route('/image')
def image():
    return send_file('outputs/plot.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)