from flask import Flask

app = Flask(__name__)

@app.route('/personas')
def home():
  
    personas = [
        {
            "nombre": "Laura",
            "edad": 25
        },0
        {
            "nombre": "Kevin",
            "edad": 30
        },
        {
            "nombre": "Matheo",
            "edad": 40
        },
        {
            "nombre": "Valentina",
            "edad": 50
        },
        {
            "nombre": "Andres",
            "edad": 60
        }
        
    ]

    return personas


if __name__ == '__main__':
    app.run()