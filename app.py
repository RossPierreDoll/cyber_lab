from flask import Flask, request, render_template_string
import sqlite3
app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, secret_flag TEXT)')
    cursor.execute("DELETE FROM users")
    cursor.execute("INSERT INTO users (username, password, secret_flag) VALUES ('admin', 'SuperTajneHaslo123!', 'FLAG{SQLi_Master_Fedora_2026}')")
    cursor.execute("INSERT INTO users (username, password, secret_flag) VALUES ('jan', 'haslo123', 'FLAG{Normal_User_Flag}')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return '''
        <h2>Laboratorium Cyberbezpieczeństwa: SQL Injection</h2>
        <form action="/login" method="POST">
            <label>Użytkownik:</label><br>
            <input type="text" name="username"><br>
            <label>Hasło:</label><br>
            <input type="password" name="password"><br><br>
            <input type="submit" value="Zaloguj się">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # BEZPIECZNE ZAPYTANIE PARAMETRYZOWANE
    query = "SELECT username, secret_flag FROM users WHERE username = ? AND password = ?"
    
    try:
        # Przekazujemy dane w krotce (tuple), a baza danych sama dba o bezpieczne podstawienie wartości
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"<h3>Zalogowano pomyślnie!</h3><p>Witaj <b>{user[0]}</b>. Twoja flaga to: <b>{user[1]}</b></p><hr><p><small>Wykonane zapytanie SQL: <code>{query}</code></small></p>"
        else:
            return f"<h3>Błąd logowania!</h3><p>Nieprawidłowy login lub hasło.</p><hr><p><small>Wykonane zapytanie SQL: <code>{query}</code></small></p>"
    except Exception as e:
        return f"<h3>Błąd bazy danych!</h3><p>{e}</p><hr><p><small>Wykonane zapytanie SQL: <code>{query}</code></small></p>"
@app.route('/xss_page')
def xss_page():
    query = request.args.get('query', '')
    
    # CELOWO WPROWADZONA PODATNOŚĆ (Reflected XSS)
    html_template = f'''
        <h3>Wyszukiwarka laboratorium (Podatna na XSS)</h3>
        <form action="/xss_page" method="GET">
            <input type="text" name="query" value="{query}">
            <input type="submit" value="Szukaj">
        </form>
        <hr>
        <p>Wyniki wyszukiwania dla frazy: <b>{query}</b></p>
    '''
    return render_template_string(html_template)
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)