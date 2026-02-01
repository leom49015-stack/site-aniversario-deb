from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Feliz Aniversário Deb</title>

    <!-- Fontes -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Dancing+Script:wght@600&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            height: 100vh;
            font-family: 'Playfair Display', serif;
            background-color: #fff7d6;
            background-image:
                radial-gradient(circle at 20px 20px, #f1c40f 8px, transparent 9px),
                radial-gradient(circle at 60px 60px, #f39c12 10px, transparent 11px),
                radial-gradient(circle at 100px 30px, #f1c40f 7px, transparent 8px);
            background-size: 120px 120px;
            animation: moveBg 40s linear infinite;
        }

        @keyframes moveBg {
            from { background-position: 0 0; }
            to { background-position: 400px 400px; }
        }

        .overlay {
            background: rgba(255, 255, 255, 0.78);
            height: 100%;
            padding: 30px;
            text-align: center;
        }

        h1 {
            font-size: 3.5rem;
            margin-bottom: 40px;
            color: #5a3e1b;
        }

        h2 {
            font-size: 2rem;
            margin-bottom: 20px;
        }

        .card {
            width: 300px;
            height: 130px;
            margin: 0 auto;
            background: #fff3cd;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            font-weight: bold;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            transition: opacity 0.4s ease;
        }

        .buttons {
            margin-top: 20px;
        }

        button {
            font-size: 1.5rem;
            padding: 10px 20px;
            border: none;
            border-radius: 12px;
            background: #f1c40f;
            cursor: pointer;
            margin: 0 10px;
        }

        button:hover {
            background: #e1b90d;
        }

        footer {
            margin-top: 50px;
        }

        footer p {
            font-family: 'Dancing Script', cursive;
            font-size: 2.3rem;
            color: #6b4f1d;
        }
    </style>
</head>
<body>

<div class="overlay">
    <h1>Feliz Aniversário DEB 🌻</h1>

    <h2>Motivos para você ser incrível:</h2>

    <div class="card" id="card"></div>

    <div class="buttons">
        <button onclick="prev()">◀</button>
        <button onclick="next()">▶</button>
    </div>

    <footer>
        <p>Que você tenha um excelente dia ✨</p>
    </footer>
</div>

<script>
    const adjetivos = {{ adjetivos | safe }};
    let index = 0;
    const card = document.getElementById("card");

    function show() {
        card.style.opacity = 0;
        setTimeout(() => {
            card.textContent = adjetivos[index];
            card.style.opacity = 1;
        }, 200);
    }

    function next() {
        index = (index + 1) % adjetivos.length;
        show();
    }

    function prev() {
        index = (index - 1 + adjetivos.length) % adjetivos.length;
        show();
    }

    show();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    adjetivos = [
        "Linda", "Especial", "Carinhosa", "Inteligente", "Me Acha Bonito :)",
        "Gentil", "Gosta de Maracujá", "Divertida", "Doce", "Encantadora",
        "Autêntica", "Engraçada", "Sorridente", "Criativa", "Única",
        "Maravilhosa", "Doidinha", "Brilhante", "Determinada", "Cor de Papelão",
        "Radiante", "Sensível", "Corajosa", "Aí que deliciaaan", "Me Acha Gatinho:)",
        "Tem Uma Voz Linda", "Sabe Conversar", "Bom Gosto Para Música", "Verdadeira", "Cativante",
        "Calma", "Sincera", "Sorriso Bonito", "Tem Um Jeito de Me Deixar Sem Graça", "Amável",
        "Gatinha", "Paciente", "Tem Um Cabelo Bonito", "Conhecedora de Muitas Coisas (Bota Muito Nisso kkk)", "Leve",
        "Graciosa", "Afetuosa", "Encantante", "Valiosa", "Ilustre",
        "Cheio de Doença, Mas Ainda Viva", "Magnífica", "Tem Bom Humor"
    ]
    return render_template_string(HTML, adjetivos=adjetivos)

if __name__ == "__main__":

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)


