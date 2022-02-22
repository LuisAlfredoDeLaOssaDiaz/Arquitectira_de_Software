class Document(object):

    def __init__(self, id_libro : int = 0, title : str = 'Title', authors : str = 'Authors', pub_date : str = 'PublicationDate' ,edition : str = 'Edition' ,num_pages : int = 0):
        self._id_libro = id_libro
        self._title = title
        self._authors = authors
        self._pub_date = pub_date
        self._edition = edition
        self._num_pages = num_pages 


    @property
    def id_libro(self) -> int:
        return self._id_libro

    @id_libro.setter
    def id_libro(self, id_libro: int):
        self._id_libro = id_libro

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def authors(self) -> str:
        return self._authors

    @authors.setter
    def authors(self, authors: str):
        self._authors = authors

    @property
    def pub_date(self) -> str:
        return self._pub_date

    @pub_date.setter
    def pub_date(self, pub_date: str):
        self._pub_date = pub_date

    @property
    def edition(self) -> str:
        return self._edition

    @edition.setter
    def edition(self, edition: str):
        self._edition = edition

    @property
    def num_pages(self) -> int:
        return self._num_pages

    @num_pages.setter
    def num_pages(self, num_pages: int):
        self._num_pages = num_pages

    def __str__(self):
        return '( {0}, {1}, {2}, {3} , {4} , {5} )'.format(self.id_libro, self.title, self.authors, self.pub_date, self.edition, self.num_pages)

if __name__ == '__main__':
    osso = Document(

        id_libro = 0 ,
        title = "Title Prueba" ,
        authors = "Authors Prueba" ,
        pub_date = "Publication date Prueba" ,
        edition = "Edition Prueba" ,
        num_pages = "Number pages Prueba" ,
    )
    print(osso)