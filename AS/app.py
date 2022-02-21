from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
dmodel = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/libro')
def libro():
    ddata = [(

        j.id_libro,
        j.title,
        j.authors,
        j.pub_date,
        j.edition,
        j.num_pages,
        j.document,   
    ) for j in dmodel]
    print(ddata)
    return render_template('libro.html', value=ddata)


@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')

@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_libro  = request.form['id_libro']
    title = request.form['title']
    authors = request.form['authors']
    pub_date = request.form['pub_date']
    edition = request.form['edition']
    num_pages = request.form['num_pages']
    document = Document(
        id_libro = id_libro,
        title = title,
        authors = authors,
        pub_date = pub_date,
        edition = edition,
        num_pages = num_pages)
    model.append(Document)
    return render_template('document_detail.html', value=document)


if __name__ == '__main__':
    app.run()