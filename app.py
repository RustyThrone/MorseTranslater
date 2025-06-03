from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        user_input = request.form.get('message')
        response = f"You said: {user_input}"
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run()
