import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request
from app.curr_exchange_api import CurrencyExchangeAPI
from app.utils import to_int, to_float

app = Flask(__name__)
HOST_IP = os.getenv("HOST_IP")
HOST_PORT = os.getenv("HOST_PORT")

@app.route('/')
def index():
    return "Welcome to Currency Exchange API Server!"


@app.route('/exchange', methods=['GET'])
def exchange():
    """
    Currency Exchange by specifying the quotes of source and destination.

    """

    source = request.args.get('source')
    destination = request.args.get('destination')
    value = request.args.get('value')

    if to_float(value) == 0: 
        error_msg = "Value must be set as valid number."
        return error_msg, 403, {'Content-Type': 'text/plain; charset=utf-8'}

    print ("Getting currency exchange rate from: " + source + ", to: " + destination + ", value: " + value)

    try:
        api = CurrencyExchangeAPI()

        response = api.get_exchange(source=source, destination=destination)
        
        if response.status_code != 200:
            error_msg = "An error occurred during the call to Currency Exchange API."
            if response.text != None and response.text != "":
                error_msg = response.text
            return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}
        
        data = response.text
        exchange_rate = to_float(data)
        original_value = to_float(value)

        if exchange_rate == 0:
            error_msg = "An error occurred during calculating currency value."
            return error_msg, response.status_code, {'Content-Type': 'text/plain; charset=utf-8'}

        converted_value = exchange_rate * original_value
        return format(converted_value, ".2f"), 200, {'Content-Type': 'text/plain; charset=utf-8'}
            
    except Exception as e:
        return e, 400, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == "__main__":
    app.run(host=HOST_IP, port=to_int(HOST_PORT), debug=True)
