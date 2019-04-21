import React from 'react';
import './puzzle.css';
import axios from 'axios';


function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}

class Board extends React.Component {
  renderSquare(i) {
    return (
      <Square
        value={this.props.squares[i]}
        onClick={() => this.props.onClick(i)}
      />
    );
  }


  render() {
    return (
      <div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

const LoadingSpinner = () => (
      <div>
        <i className="fa fa-spinner fa-spin" /> Loading...
      </div>
    );


class Puzzle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      history: [
        {
          squares: Array(9).fill(null)
        }
      ],
      stepNumber: 0,
      counter: 0,
      state: null,
      moves: [],
      loading: false,
      display: false,
    };

    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleClick(i) {
    const history = this.state.history.slice(0, this.state.stepNumber + 1);
    const current = history[history.length - 1];
    const squares = current.squares.slice();
    this.setState({display: false});
    if (squares[i] || squares[i] === 0) {
      return;
    }
    this.setState({counter: this.state.counter + 1})
    squares[i] = this.state.counter;
    this.setState({
      history: history.concat([
        {
          squares: squares
        }
      ]),
      stepNumber: history.length,
    });
    this.setState({moves: []})
  }

  handleSubmit(event) {
        event.preventDefault();
        this.setState({loading: true})
        if (this.state.stepNumber > 8) {
          const history = this.state.history;
          const current = history[this.state.stepNumber];
          const squares = current.squares.slice();
          const puzzle = {tiles: squares}
          console.log("Squares: " + squares)
          const puzzleStr = JSON.stringify(puzzle);
          console.log("Posting Data: ", puzzleStr)
          var headers = {
            'Content-Type': 'application/json;charset=UTF-8',
          }
          try{
              axios.post("http://localhost:5000/api/SolvePuzzle", { squares }, {headers: headers})
              .then((res) =>
               {
                console.log("Post Received Moves: " + res.data['__Node__']['path']);
                let path = res.data['__Node__']['path'];
                for(let i= 0; i < path.length; i++)
                {
                    this.state.moves.push(path[i]);
                }
                this.setState({display: true});
              })
              .catch((error) =>
              {
                if(error.response)
                {
                    if(error.response.status === 400)
                    {
                        alert("Invalid Puzzle Input.")
                    }
                    else {
                        alert("Oops...Something Went Wrong...");
                    }
                }
                if(error.request)
                {
                    console.log(error.request);
                }
              })
          } catch(e) {
            console.log(`Axios Request Failed: ${e}`);
          }
      } else if (this.state.stepNumber <= 8){
        alert("Please Enter All Numbers 0-9 Into the Puzzle")
      }
      this.setState({loading: false});
  }

  jumpTo(step) {
    this.setState({
      stepNumber: step,
      counter: step,
    });
  }

  render() {
    const history = this.state.history;
    const current = history[this.state.stepNumber];

    const placements = history.map((step, move) => {
      const desc = move ?
        'Go to input #' + move :
        'Restart';
      return (
        <li key={move}>
          <button onClick={() => this.jumpTo(move)}>{desc}</button>
        </li>
      );
    });


    let status = this.state.loading ? "Solving Puzzle: Searching For Solution Using A* Misplaced Tile Hueristic..." : this.state.stepNumber < 9 ? "Enter Tile : " + (this.state.stepNumber) : this.state.display ? "Puzzle Solved!" : "Click Submit to Solve The Puzzle!";
    console.log("Moves Before Return: " + this.state.moves)
    return (
        <div>
          <div className="game">
            <div className="game-board">
              <Board
                squares={current.squares}
                onClick={i => this.handleClick(i)}
              />
            </div>
            <div className="game-info">
              <div>{status}</div>
              <ol>{placements}</ol>
            </div>
          </div>
          <button onClick={this.handleSubmit}> Submit </button>
          {console.log("display:" + this.state.display)}
          {console.log("moves length:" + this.state.moves.length)}
          {this.state.loading ? <LoadingSpinner />
            : ((this.state.moves.length > 0) && this.state.display) ?
                    <div>
                        <h2> Moves to Solution </h2>
                        <div> {this.state.moves.map((move) => (<li> {move} </li>))} </div>
                    </div>
                    : <div> </div> }
        </div>
    );
  }
}

export default Puzzle;




