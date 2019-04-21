from flask import Flask, request, abort
from flask_cors import CORS
import numpy as np
from Classes.Problem import *
from Classes.Search import *
import time
import json

# Instantiate App
app = Flask(__name__)
CORS(app)

help_message = """ 
API Usage:
- POST   /api/SolvePuzzle data={"key": "value"}
"""

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, np.ndarray):
            return o.tolist()
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}

@app.route('/api', methods=['GET'])
def help():
    return help_message

@app.route('/api/SolvePuzzle', methods=['POST'])
def index():
    try:
        print("Received: ", request.json)

        tiles = request.get_json()['squares']
        print("tiles: ", tiles)
        n = 3
        initial_state = np.array([tiles[i:i + n] for i in range(0, len(tiles), n)])
        puzzle = PuzzleProblem(initial_state)
        if not puzzle.validate_initial_state(initial_state):
            abort(400, "Invalid Initial Puzzle State")
        start_time = time.time()
        searcher = AstarMisplacedTileSearch(puzzle)
        print("[!] Searching For Solution Using A* Misplaced Tile Hueristic....")
        solution = searcher.search()
        print("[+] Found Solution in ", time.time() - start_time, 's')
        print("[+] Solution Was Found At Depth ", solution.path_cost)
        print("[+] Printing the Found Puzzle Solution...")
        print(solution.state)
        print("[+] Printing the Moves to get to the Solution...")
        print(solution.path)
        print("\n")
        print("\n")
        print("Returning Payload: ", json.dumps(solution, cls=CustomEncoder))

        return json.dumps(solution, cls=CustomEncoder)
    except Exception as e:
        print("Failed with request: ", request.json, ", Threw exception :", e)
        return e


if __name__ == '__main__':
    app.run(debug=True)
