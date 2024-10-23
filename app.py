from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>Welcome to the Flask Server Homepage</h1><p>This is a test page to confirm that the server is running.</p>"

@app.route('/receive_trade_order', methods=['GET'])
def receive_trade_order():
    # Retrieve parameters from the request
    action = request.args.get('action')
    symbol = request.args.get('symbol')
    price = float(request.args.get('price'))
    take_profit = float(request.args.get('take_profit'))
    stop_loss = float(request.args.get('stop_loss'))

    print(f"Received trade order: {action} {symbol} at {price}, TP: {take_profit}, SL: {stop_loss}")

    # Respond with JSON data for MT4
    response = {
        "action": action,
        "symbol": symbol,
        "price": price,
        "takeProfit": take_profit,
        "stopLoss": stop_loss
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Bind to all interfaces
