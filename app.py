from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        username = request.form['username']
        return f'Merhaba, {username}!'
    return '''
        <form method="POST">
            <label for="username">Kullanıcı Adı:</label>
            <input type="text" id="username" name="username" required>
            <button type="submit">Gönder</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
