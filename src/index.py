from flask import Flask,redirect,render_template,url_for

app = Flask(__name__); 

@app.route("/")
def pagina_inicial():
    return render_template("pagina_inicial.html"); 


if __name__ == "__main__":
    app.run(debug=True,port=5003); 
    