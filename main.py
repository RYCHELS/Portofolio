from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Menghubungkan SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Membuat sebuah DB
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}>'

# Data Sosial Media sebagai variabel individu
github_url = 'https://github.com/username'
twitter_url = 'https://twitter.com/username'
instagram_url = 'https://www.instagram.com/username/'

github_icon = 'github.png'
twitter_icon = 'twitter.png'
instagram_icon = 'instagram.png'

# Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html', 
                           github_url=github_url, 
                           twitter_url=twitter_url, 
                           instagram_url=instagram_url,
                           github_icon=github_icon,
                           twitter_icon=twitter_icon,
                           instagram_icon=instagram_icon)

# Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', 
                           button_python=button_python, 
                           button_discord=button_discord, 
                           button_html=button_html, 
                           button_db=button_db,
                           github_url=github_url, 
                           twitter_url=twitter_url, 
                           instagram_url=instagram_url,
                           github_icon=github_icon,
                           twitter_icon=twitter_icon,
                           instagram_icon=instagram_icon)

@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form['email']
    text = request.form['text']

    # Tugas #3. Buat agar data pengguna direkam ke dalam database
    feed = Feedback(email=email, text=text)
    db.session.add(feed)
    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)