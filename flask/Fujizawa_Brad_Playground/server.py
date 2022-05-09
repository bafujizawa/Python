from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:boxes>')
def play(boxes):
    return render_template('play.html', boxes = boxes)

if __name__ == '__main__':
    app.run(debug=True)