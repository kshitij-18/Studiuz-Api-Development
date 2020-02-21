from flask import Flask, request, jsonify
from support import chunkstring

app = Flask(__name__)


@app.route("/api2", methods=['GET'])
def api2():
    inp_string = request.args.get('string')
    inp_li = inp_string.split(',')
    count_dict = {}
    for word in inp_li:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return jsonify(count_dict)


@app.route("/api1", methods=['GET'])
def api1():
    string = request.args.get('string')
    number = request.args.get('number')
    #out_dict = {}
    li = list(chunkstring(string[::-1], int(number)))
    li = li[::-1]
    print(li)
    string2 = ""
    for word in li:
        string2 += word[::-1]+" "

    print(string2)
    return jsonify({'output': string2})


if __name__ == '__main__':
    app.run(debug=True)
