from flask import Flask, request
from principal import ordenar


app = Flask('TesteAPI')

@app.route('/ordenalista', methods=['POST'])
def ordenaLista():
    body = request.get_json()

    if ('lista' not in body):
        return {'status': 400, 'mensagem': 'O parametro lista é obrigatório'}

    rtn = ordenar(body['lista'])

    return {'listaOrdenada': rtn}

app.run()
