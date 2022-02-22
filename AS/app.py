from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model2 = []


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
    data2 = [(

        j.id_libro,
        j.title,
        j.authors,
        j.pub_date,
        j.edition,
        j.num_pages
    ) for j in model2]
    print(data2)
    return render_template('libro.html', value=data2)


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
    document = Document(id_libro = id_libro, title = title, authors = authors, pub_date = pub_date, edition = edition, num_pages = num_pages)
    model2.append(document)
    print(document)
    return render_template('document_detail.html', value=document)

@app.route("/person_delete/<id>")
def delete_person(id):
    for i in model:
        if i.id_person == id:
            temp = i
            model.remove(i)

    return "Eliminado la persona: " + temp.id_person + temp.name
    

@app.route("/document_delete/<id>")
def delete_document(id):
    for i in model2:
        if i.id_libro == id:
            temp = i
            model2.remove(i)

    return "Eliminado el documento: " + temp.id_libro + temp.title


if __name__ == '__main__':
    app.run(debug=True)