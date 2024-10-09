from flask import Flask, render_template, request
from textGenerationCode import generate_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def generate_story():
    if request.method == 'POST':
        story = request.form['story']
        updated_story = '. '.join(generate_text(story).split('.')[:-1]) + '.'
        return render_template('index.html', updated_story = updated_story)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
