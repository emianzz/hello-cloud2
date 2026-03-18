[13:23, 3/18/2026] +90 541 944 70 18: from flask import Flask, render_template_string, request
import os
import psycopg2

app = Flask(name)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://emirhan:3FrDCjv4mdIX0xWf7AMK0G0wxowYFw21@dpg-d6t8rhvdiees73cq91dg-a.oregon-postgres.render.com/hello_cloud2_db_2t1d")
HTML ="""

<! doctype html>

<html>
<head>
<title>Buluttan Selam !< /title>
<style>
body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
h1 { color: #333; }
form { margin: 20px auto; }
input { padding: 10px; font-size: 16px; }
button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; }
ul { list-style: none; padding: 0; }
li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }
</style>
[13:44, 3/18/2026] +90 541 944 70 18: from flask import Flask, render_template_string, request
import os
import psycopg2

app = Flask(name)

DATABASE_URL = os.getenv("DATABASE_URL", "")
HTML ="""
<! doctype html>
<html>
<head>
 <title>Buluttan Selam !< /title>
 <style>
  body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
  h1 { color: #333; }
  form { margin: 20px auto; }
  input { padding: 10px; font-size: 16px; }
  button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; }
  ul { list-style: none; padding: 0; }
  li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }
</style>
</head>
<body>
 <h1>Buluttan Selam !< /h1>
  <p>Adını yaz, selamını bırak </p>
  <form metho…
[13:51, 3/18/2026] +90 555 069 23 19: @app.route("/", methods=["GET", "POST"])
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT)")

    if request.method == "POST":
        isim = request.form.get("isim")
        if isim:
            cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s);", (isim,))
            conn.commit()

    cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
    isimler = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    return render_template_string(HTML, isimler=isimler)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
[15:03, 3/18/2026] +90 541 944 70 18: from flask import Flask, render_template_string, request
import os
import psycopg2

app = Flask(_name_)

DATABASE_URL = os.getenv("DATABASE_URL")

HTML = """
<!DOCTYPE html>
<html>
<head>
 <title>Buluttan Selam!</title>
 <style>
  body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
  h1 { color: #333; }
  form { margin: 20px auto; }
  input { padding: 10px; font-size: 16px; }
  button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; }
  ul { list-style: none; padding: 0; }
  li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }
 </style>
</head>
<body>
 <h1>Buluttan Selam!</h1>
 <p>Adını yaz, selamını bırak</p>
 <form method="POST">
   <input type="text" name="isim" placeholder="Adını yaz" required>
   <button type="submit">Gönder</button>
 </form>
 <h3>Ziyaretçiler:</h3>
 <ul>
  {% for ad in isimler %}
   <li>{{ ad }}</li>
  {% endfor %}
 </ul>
</body>
</html>
"""

def connect_db():
    return psycopg2.connect(DATABASE_URL)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS ziyaretciler (
            id SERIAL PRIMARY KEY,
            isim TEXT
        )
    """)

    if request.method == "POST":
        isim = request.form.get("isim")
        if isim:
            cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s);", (isim,))
            conn.commit()

    cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
    isimler = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()

    return render_template_string(HTML, isimler=isimler)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
