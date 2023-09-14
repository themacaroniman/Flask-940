from flask import Flask
import random 

daftar_fakta = ['Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
                "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan" ,
                "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita"]

app = Flask(__name__)

@app.route("/")
def home():
    return '<a href="/facts">Klik disini untuk melihat sebuah fakta</a>'

@app.route("/facts")
def hello_world():
    return f'<p>{random.choice(daftar_fakta)}</p><a href="/ALAMAT">klik link ini untuk melihat jokes</a>'

@app.route("/ALAMAT")
def memes():
    return '<h1> Ikan apa yang romantis?........Ikant stop falling in love with you wkwkkwwk</h1>'


app.run(debug=True)