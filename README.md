# Prova Técnica - Desenvolvedor Python

Resale is a Brazilian technology startup for real estate. With significant growth each year, Resale has been featured in the specialized media.
The purpose of this test is to develop a REST API to control real estate and real estate registration. In that application they must contain listing, registration, edition and deletion.

## Getting Started

Go to ///.../src/ and run the app.py file.

### Prerequisites

Python3
Python-Flask
SQLAlchemy
MySQLClient


### Installing

```
sudo apt-get install Python3

```
```
sudo pip3 install flask SQLAlchemy MySQLClient
```


## Running the tests

Use Python3 app.py
At your localhost it is possible to access the routes.

### Samples

List of all 'imobiliarias'. Your information is collected from the insert and allocated to an object to return.
Json is used for this return.

```
#imobiliaria listar todos
@app.route('/imobiliaria/listar')
def listar_imobiliarias():
    imobiliarias = Imobiliaria.query.all()
    imobiliarias = [x.to_obj() for x in imobiliarias]
    return jsonify(imobiliarias=imobiliarias)
```

### Samples

Def of 'Imobiliaria', and allocation of values ​​in an object

```
class Imobiliaria(Base):
    __tablename__ = 'imobiliaria'
    id = Column(Integer, primary_key=True)
    nome = Column(String(200), nullable=False)
    endereco = Column(String(200))
    imovel_rel = relationship("Imovel", lazy='selectin')    #enviando id imobiliaria para tabela imoveis

    def __init__(self, nome=None, endereco=None):
        self.nome = nome
        self.endereco = endereco

#definicao objeto imobiliaria
    def to_obj(self):
        return {'id': self.id, 'nome': self.nome, 'endereco': self.endereco}
```

## Built With

* [Python3](https://www.python.org/download/releases/3.0/) - Programming language
* [Python-Flask](https://flask.palletsprojects.com/en/1.1.x/) - Micro framework web for Python

## Authors

* **Rafael Resende** - (https://github.com/RafaelResende)

## License

This project was developed in order to join the company Resale and must not be reproduced by anyone other than the developer.

## Acknowledgment

I thank the entire Resale team that made the challenge available and Ana Carolina Buschinelli for informing me of the Job vacancy.
