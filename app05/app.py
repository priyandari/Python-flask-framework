from flask import Flask, render_template
from models import ArtikelModel

application = Flask(__name__)

content = '''
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[3] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more frequently than the core Flask program.
'''

@application.route('/')
def index():
    # buat objek dari kelas model ArtikelModel
    model = ArtikelModel()
    
    # isi nilai ke model
    model.setTitle('Belajar Flask')
    model.setDate('05/05/2020')
    model.setContent(content)
    
    # kirim nilai ke view
    return render_template('artikel.html',
        judul=model.getTitle(),
        tanggal=model.getDate(),
        isiartikel=model.getContent())

if __name__=='__main__':
    application.run(debug=True)
    
    
    
    
    