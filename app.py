from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    is_python = False
    if 'python' in user_agent:
        is_python = True

    return render_template('index.html', user_agent=user_agent, is_python=is_python)

