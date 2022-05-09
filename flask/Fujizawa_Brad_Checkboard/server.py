from flask import Flask, render_template
app = Flask(__name__)

odd_row = [0,1]
even_row = [1,0]

@app.route('/')
def main():
    return render_template('index.html', odd_row=odd_row, even_row=even_row, number=8)



if __name__ == '__main__':
    app.run(debug=True)

