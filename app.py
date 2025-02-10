from flask import Flask, render_template,request, session,render_template_string, jsonify,flash, redirect, url_for
from datetime import datetime
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("index.html")


@app.route ("/projetos")
def portfolio():
    return render_template("portfolio.html")

@app.route("/projetos/lista1exercicio1")
def l1e1():
    return render_template('l1e1.html')

@app.route("/projetos/lista1exercicio2")
def l1e2():
    return render_template('l1e2.html')

def generate_data():
    data = []
    for i in range(1, 998):
        data.append({
            'id': i,
            'name': f'Nome {i}',
            'lastname': f'Sobrenome {i}',
            'email': f'email{i}@example.com',
            'action': f'Ação {i}'
        })
    return data

@app.route("/projetos/lista1exercicio3")
def l1e3():
    data = generate_data()
    return render_template('l1e3.html', data=data)

USER = "snake"
PASSWORD ="solidsnake"

@app.route("/projetos/lista2/login", methods=["GET", "POST"])
def login():
    if "try" not in session:
        session["try"] = 0

    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]

        if session["try"] >= 12:
            return render_template("login.html", msg="Você atingiu o limite de tentativas erradas. Tente novamente mais tarde.", block=True)

        if user == USER and password == PASSWORD:
            datenow = datetime.now().hour

            if 5 <= datenow < 12:
                hello = "Bom dia!"
            elif 12 <= datenow < 18:
                hello = "Boa tarde!"
            else:
                hello = "Boa noite!"
                
            session["try"] = 0
            return render_template("welcome.html", hello=hello)
        else:
            session["try"] += 1
            return render_template("login.html", msg="Login ou senha incorretos.", block=False)
    
    return render_template("login.html", msg=None, block=False)

def template_json(json_data):
    form_fields = json.loads(json_data)  
    html_fields = ""
    
    for field in form_fields:
        field_type = field['type']
        field_name = field['name']
        field_label = field['label']
        
        if field_type == 'text':
            html_fields += f'<label for="{field_name}">{field_label}</label><input type="text" id="{field_name}" name="{field_name}"><br><br>\n'
        elif field_type == 'number':
            html_fields += f'<label for="{field_name}">{field_label}</label><input type="number" id="{field_name}" name="{field_name}"><br><br>\n'
        elif field_type == 'email':
            html_fields += f'<label for="{field_name}">{field_label}</label><input type="email" id="{field_name}" name="{field_name}"><br><br>\n'

    template_html = f"""
    <html>
    <head>
    <title>Script Python</title>
    <link rel="stylesheet" href="{{{{ url_for('static', filename='css/l2e2.css') }}}}">
    </head>
    <body>
        <form method="POST" action="/projetos/l2e2/submit_form">
            {html_fields}
            <input type="submit" value="Enviar">
        </form>
        <a href="{{{{ url_for('portfolio') }}}}"><button>Voltar!</button></a>
    </body>
    </html>
    """
    return template_html

@app.route('/projetos/l2e2')
def forms():
    json_data = json.dumps([
        {"name": "nome", "label": "Nome", "type": "text"},
        {"name": "idade", "label": "Idade", "type": "number"},
        {"name": "email", "label": "E-mail", "type": "email"}
    ])
    
    html_form = template_json(json_data)
    return render_template_string(html_form)

@app.route('/projetos/l2e2/submit_form', methods=['POST'])
def submit_form():
    dados = request.form.to_dict()
    lista_strings = [f"{key}: {value}" for key, value in dados.items()]
    return jsonify(lista_strings)

users_db = {
    "snake": generate_password_hash("solidsnake"),
    "admin": generate_password_hash("admin"),
}

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def authenticate(username, password):
        if username in users_db and check_password_hash(users_db[username], password):
            return User(username, password)
        return None

@app.route('/projetos/l2e3/login', methods=['GET', 'POST'])
def l2e3():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.authenticate(username, password)
        if user:
            session['username'] = user.username
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválidos', 'danger')

    return render_template('l2e3.html')


@app.route('/projetos/l2e3/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('l2e3'))


user_l3 = {
    "snake": "solidsnake",
    "admin": "admin"
}

@app.route("/projetos/l3")
def l3():
    return render_template("l3.html")

@app.route("/projetos/l3/login", methods=["POST"])
def l3_forms():
    if "attempts" not in session:
        session["attempts"] = 0
    
    if session["attempts"] >= 2:
        return jsonify({"success": False, "message": "Limite de tentativas atingido."}), 403
    
    data = request.get_json()
    
    if not data or "username" not in data or "password" not in data:
        return jsonify({"success": False, "message": "Dados inválidos ou ausentes."}), 400
    
    username = data["username"]
    password = data["password"]
    
    if username in user_l3 and user_l3[username] == password:
        session.pop("attempts", None)  
        return jsonify({"success": True, "message": "Login bem-sucedido!"})
    else:
        session["attempts"] += 1
        return jsonify({"success": False, "message": "Usuário ou senha incorretos."}), 401

posts = []

@app.route('/projetos/prova1')
def p1():
    return render_template('blog.html', posts=sorted(posts, key=lambda x: x['timestamp'], reverse=True))

@app.route('/projetos/prova1/add', methods=['POST'])
def add_post():
    content = request.form.get('content')
    if content:
        posts.append({'content': content, 'timestamp': datetime.now()})
    return redirect(url_for('p1'))

users_p2 = {
    'admin': 'admin',
    'snake': 'solidsnake'
}

attempts = []

@app.route("/projeto/prova2", methods=["GET", "POST"])
def p2():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username in users_p2 and users_p2[username] == password:
            attempts.append({'username': username, 'status': 'Success', 'date': datetime.now()})
            return render_template('authenticator.html', message="Logado com sucesso", success=True)
        else:
            attempts.append({'username': username, 'status': 'Success', 'date': datetime.now()})
            return render_template('authenticator.html', message="Dados Incorretos", success=False)
    return render_template('authenticator.html')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/projetos/prova3', methods=['GET', 'POST'])
def p3():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Nenhum arquivo enviado', 'danger')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('Nenhum arquivo selecionado', 'warning')
            return redirect(request.url)
        
        if file:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            filename = f"{timestamp}_{file.filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash(f'Upload bem-sucedido! Arquivo salvo em: {filepath}', 'success')
            return redirect(url_for('p3'))

    return render_template('photos.html')

appointments = [
    {"id": 1, "patient": "Carlos Santos", "doctor": "Dr. Pedro", "date": "2025-01-14"},
    {"id": 2, "patient": "Ana Paula", "doctor": "Dr. Maria", "date": "2025-01-16"}
]

@app.route('/projetos/prova')
def p4():
    sorted_appointments = sorted(appointments, key=lambda x: x['date'])
    return render_template('lession.html', appointments=sorted_appointments)

@app.route('/projetos/prova/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        patient = request.form['patient']
        doctor = request.form['doctor']
        date = request.form['date']
        
        new_id = max([appointment['id'] for appointment in appointments]) + 1 if appointments else 1
        
        appointments.append({"id": new_id, "patient": patient, "doctor": doctor, "date": date})
        return redirect(url_for('p4'))
    
    return render_template('add.html')

@app.route('/projetos/prova/delete/<int:id>')
def delete(id):
    global appointments
    appointments = [appointment for appointment in appointments if appointment['id'] != id]
    return redirect(url_for('p4'))

if __name__ == "__main__":
    app.run(debug=True)