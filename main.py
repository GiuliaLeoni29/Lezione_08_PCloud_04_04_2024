import json

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

db = {}
#db = {
#    's1' : [[data1, val1],[data2, val2],...]
#    's2' : [[data1, val1],[data2, val2],...]
#       ...
#}

@app.route('/graph')
def graph():
    return redirect(url_for('static', filename='graph.html'))



@app.route('/sensors',methods=['GET'])
def sensors():
    return json.dumps(list(db.keys())), 200


@app.route('/sensors/<s>',methods=['POST'])
#<s> è parametro delle url --> sensors/s1, sensors/s2, ...
def add_data(s):
    data = request.values['data']
    #request.values[] è dizionario passato a POST
    val = float(request.values['val'])
    if s in db:
        db[s].append([data,val])
        #andavano bene anche le tuple -> (data,val)
    else:
        db[s] = [[data,val]]
    return 'ok',200

@app.route('/sensors/<s>',methods=['GET'])
def get_data(s):
    if s in db:
        # return json.dumps(db[s])
        #se il sensore è nel db restituisco al client le sue informazioni in formato json

    #per fare grafico perchè il codice richiedeva numeri crescenti e non date
        r = []
        #r = [
        #   [0,val0]
        #   [1, val1]
        #   ...
        #]
        for i in range(len(db[s])):
            r.append([i,db[s][i][1]])
        return json.dumps(r),200
    else:
        return 'sensor not found',404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

