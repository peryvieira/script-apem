# Script APEM-MA
Esta é uma API utilizando Flask para retornar dados de determinados Navios de uma tabela do site da [apem-ma](http://www.apem-ma.com.br/?module=shipmaneuvering)

---
##  Installation
Install with pip:

```
$ pip install -r requirements.txt
```
##  Run

```
export FLASK_APP=app
```
```flask
flask run
```
---
##  Usage
Exemplo de uso da API.


Body : 
```json
{
    "ships": ["MARITIME GRACIOUS","PACIFIC MARINER"]
}
```
A API retornará dados(nome,bandeira,data,hora,berço) dos navios presentes no array caso conste na tabela do site da [APEM-MA](http://www.apem-ma.com.br/?module=shipmaneuvering)

Response:
```json
[
    {
        "nome": "MARITIME GRACIOUS", 
        "bandeira": "SINGAPURA", 
        "data": "16/03/22", 
        "hora": "11:32", 
        "berco": "106"
},
    {
        "nome": "PACIFIC MARINER", 
        "bandeira": "HONG KONG", 
        "data": "16/03/22", 
        "hora": "16:44", 
        "berco": "ILHA DO MEDO"
    }
]
```