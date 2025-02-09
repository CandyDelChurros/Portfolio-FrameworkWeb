from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)