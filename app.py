from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from flask_wtf.csrf import CSRFProtect
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lf_fVctAAAAAOp-gD5LJ9jFldNwIv3HdQd8grmC'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lf_fVctAAAAAKGhagxL4Ksp4tS0BTe7tV_onpA4'
csrf = CSRFProtect(app)

def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, discord TEXT, tiktok TEXT, img_url TEXT)')
    conn.close()

init_db()

class UserForm(FlaskForm):
    discord = StringField('Discord Username')
    tiktok = StringField('TikTok Username')
    img_url = StringField('Profile Image URL')
    recaptcha = RecaptchaField()
    submit = SubmitField('تسجيل')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
