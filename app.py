from flask import Flask, request, make_response

from test_proj.model import Request
from test_proj.service import sum_func

app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def sum_test():
    try:
        request_data = request.get_json()
        request_m = Request(request_data['a'], request_data['b'])
        r = sum_func(request_m)
        return make_response({'result': r}, 200)
    except ValueError as e:
        return make_response(e.__str__(), 400)
    except Exception as e:
        return make_response(e.__str__(), 500)


if __name__ == '__main__':
    app.run()
