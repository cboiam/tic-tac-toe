import React from "react";
import Board from "./board/Board";
import Chat from "./chat/Chat";
import Status from "./status/Status";
import GameOver from "./gameOver/GameOver";
import "./Game.css";

export default class Game extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      game: null,
    };
  }

  componentDidMount() {
    this.props.connection.on("game_create", (data) => {
      const sids = JSON.parse(data);

      if (
        this.props.player.sid === sids.inviter.sid ||
        this.props.player.sid === sids.invited.sid
      ) {
        this.props.showGame();

        this.props.connection.emit("game_start", data, (data) => {
          const game = JSON.parse(data);
          const player = game.players.find(
            (p) => p.sid === this.props.player.sid
          );
          this.setState({ game, player });
        });

        this.props.connection.on("game_movement_sent", this.updateBoard);
      }
    });
  }

  updateBoard = (data) => {
    const game = { ...this.state.game };
    const json = JSON.parse(data);

    game.board = json.board;
    game.turn = json.turn;
    game.winner = json.winner;

    this.setState({ game });
  };

  fieldClicked = (row, column) => {
    if (this.state.game.winner) {
      return;
    }

    const movement = {
      sid: this.state.game.sid,
      player_sid: this.state.player.sid,
      row,
      column,
    };

    this.props.connection.emit("game_movement_send", JSON.stringify(movement));
  };

  addMessage = (message) => {
    const game = { ...this.state.game };
    game.chat = [...this.state.game.chat];
    game.chat.push(message);

    this.setState({ game });
  };

  getWinner = () => {
    return this.state.game.players.find(
      (p) => p.sid === this.state.game.winner
    );
  };

  exitGame = () => {
    this.setState({
      game: null,
      player: null,
    });

    this.props.exitGame();
  };

  render() {
    if (!this.state.game) {
      return null;
    }

    return (
      <div className={`game ${this.props.visibility}`}>
        <div className="game-board">
          <Board
            board={this.state.game.board}
            player={this.state.player}
            fieldClicked={this.fieldClicked}
          />
          <Status
            players={this.state.game.players}
            player={this.state.player}
            turn={this.state.game.turn}
          />
        </div>
        <div className="game-chat">
          <Chat
            connection={this.props.connection}
            sid={this.state.game.sid}
            player={this.state.player}
            messages={this.state.game.chat}
            addMessage={this.addMessage}
          />
        </div>
        <GameOver
          winner={this.getWinner()}
          player={this.state.player}
          exit={this.exitGame}
        />
      </div>
    );
  }
}
