İşte kodunun tüm hatalardan arındırılmış, kopyalayıp doğrudan çalıştırabileceğin en temiz hali.

Dosya adının app.py olduğunu varsayarsak, Render üzerinde sorunsuz çalışması için tüm yazım hatalarını (özellikle from/form ve ½/% karışıklıklarını) düzelttim:

Python
from flask import Flask, render_template_string, request
import os
import psycopg2

app = Flask(__name__)

# Veritabanı URL'i (Render Environment Variable'dan alır veya varsayılanı kullanır)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://emirhan:3FrDCjv4mdIX0xWf7AMK0G0wxowYFw21@dpg-d6t8rhvdiees73cq91dg-a.oregon-postgres.render.com/hello_cloud2_db_2t1d")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Buluttan selam!</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
        h1 { color: #333; }
        form { margin: 20px auto; }
        input { padding: 10px; font-size: 16px; border-radius: 4px; border: 1px solid #ccc; }
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; }
        button:hover { background: #45a049; }
        ul { list-style: none; padding: 0; }
        li { background: white; margin: 5px auto; width: 250px; padding: 10px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>Buluttan Selam!</h1>
    <p>zebuncel sunar</p>
    <form method="POST">
        <input type="text" name="isim" placeholder="Adınızı yazın..." required>
        <button type="submit">Gönder</button>
    </form>
    <h3>Son Ziyaretçiler:</h3>
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
    
    # Tabloyu oluştur (Türkçe karakter riskine karşı 'ziyaretciler')
    cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT)")
    conn.commit()

    if request.method == "POST":
        isim = request.form.get("isim")
        if isim:
            cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s)", (isim,))
            conn.commit()

    # Verileri çek
    cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
    isimler = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    
    return render_template_string(HTML, isimler=isimler)

if __name__ == "__main__":
    # Render için dinamik port ayarı
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
