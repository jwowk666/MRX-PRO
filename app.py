from flask import Flask, render_template, request, redirect, flash
import sqlite3
import requests

app = Flask(__name__)
app.secret_key = 'super_secret_key_change_me' # للحماية

# إعداد قاعدة البيانات
def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, discord TEXT, tiktok TEXT, img_url TEXT)')
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # تنظيف البيانات (حماية من XSS)
        d = request.form['discord'].replace('<', '').replace('>', '')
        t = request.form['tiktok'].replace('<', '').replace('>', '')
        i = request.form['img_url']
        
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users (discord, tiktok, img_url) VALUES (?, ?, ?)", (d, t, i))
        user_id = cur.lastrowid
        conn.commit()
        conn.close()
        return f"تم التسجيل بنجاح! رقمك الخاص هو: {user_id}"
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_id = request.form['id']
    conn = sqlite3.connect('users.db')
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    
    if user:
        # هنا يمكنك إضافة كود إرسال Webhook للديسكورد
        return f"البيانات: ديسكورد: {user[1]}, تيك توك: {user[2]}"
    return "لم يتم العثور على مستخدم"

if __name__ == '__main__':
    app.run(debug=False) # تأكد أن debug False للحماية عند التشغيل الفعلي
