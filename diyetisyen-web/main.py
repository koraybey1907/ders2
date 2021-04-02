from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def baslangic():
    return render_template("anasayfa.html")

@app.route('/hakkimizda')
def hakkimizda():
    return render_template("hakkimizda.html")

@app.route('/hesapla' , methods=['POST'])
def hesapla():
    boy = int (request.form.get('boy'))
    kilo = int (request.form.get('kilo'))
    boy = boy/100

    vki = kilo / (boy * boy)
    cinsiyet = request.form.get('cinsiyet')
    if cinsiyet == "K":
        if 00.0 < vki < 18.4:
            return "Vücüt kitle indeksine göre ZAYIF kategorisindesiniz"        
        if 18.5 < vki < 24.9:
            return "Vücüt kitle indeksine göre NORMAL kategorisindesiniz"
        if 25.0 < vki < 29.9:
            return "Vücüt kitle indeksine göre FAZLA KİLOLU kategorisindesiniz"
        if 30.0 < vki < 34.9:
            return "Vücüt kitle indeksine göre Şişman (Obez) - I. Sınıf kategorisindesiniz"
        if 35.0 < vki < 44.9:
            return "Vücüt kitle indeksine göre Şişman (Obez) - II. Sınıf kategorisindesiniz"
        if 45.0 < vki < 2000.0:
            return "Vücüt kitle indeksine göre Aşırı Şişman (Aşırı Obez) - III. Sınıf kategorisindesiniz"
          
    if cinsiyet == "E":
        if 00.0 < vki < 18.4:
            return "Vücüt kitle indeksine göre ZAYIF kategorisindesiniz"
    else:
        if 18.5 < vki < 24.9:
            return "Vücüt kitle indeksine göre NORMAL kategorisindesiniz"
        if 25.0 < vki < 29.9:
            return "Vücüt kitle indeksine göre FAZLA KİLOLU kategorisindesiniz"
        if 30.0 < vki < 34.9:
            return "Vücüt kitle indeksine göre Şişman (Obez) - I. Sınıf kategorisindesiniz"
        if 35.0 < vki < 44.9:
            return "Vücüt kitle indeksine göre Şişman (Obez) - II. Sınıf kategorisindesiniz"
        if 45.0 < vki < 2000.0:
            return "Vücüt kitle indeksine göre Aşırı Şişman (Aşırı Obez) - III. Sınıf kategorisindesiniz"

@app.route('/slayt')
def slayt():
    return render_template("slayt.html")


if __name__ == "__main__":
    app.run()

