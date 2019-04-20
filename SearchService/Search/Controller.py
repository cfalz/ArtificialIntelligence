from flask import Flask, request, jsonify

# Instantiate App
app = Flask(__name__)

help_message = """
API Usage:

- POST   /api/SolvePuzzle data={"key": "value"}

"""

@app.route('/api', methods=['GET'])
def help():
    return help_message

@app.route('/api/SolvePuzzle', methods=['POST'])
def index():
    try:
        payload = request.json
        return "Received Payload: {} \n".format(payload)
    except Exception as e:
        print("Failed POST: ", payload, ", Threw exception :", e)


if __name__ == '__main__':
    app.run(debug=True)
