import React from "react";
import "./App.css";
import Login from "./components/login/Login";
import Lobby from "./components/lobby/Lobby";
import Game from "./components/game/Game";
// import { Socket } from "engine.io-client";
import Socket from "socket.io-client";
import { getVisibilityClass } from "./helpers/visibility";

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      connection: null,
      player: null,
      showGame: false,
      showLogin: true,
      showLobby: false,
    };
  }

  componentDidMount() {
    const connection = Socket("ws://localhost:5000");

    connection.on("connect", () => {
      connection.on("disconnect", () => {
        this.setState({ player: null, showLogin: true, showLobby: false, showGame: false });
      });
    });

    this.setState({ connection });
  }

  login = (player) => {
    this.setState({ player, showLogin: false, showLobby: true });
  };

  logout = () => {
    this.setState({ player: null, showLogin: true, showLobby: false });
  };

  showGame = () => {
    this.setState({ showGame: true, showLogin: false, showLobby: false });
  };

  exitGame = () => {
    this.setState({ showGame: false, showLogin: false, showLobby: true });
  }

  render() {
    if (!this.state.connection) {
      return null;
    }

    return (
      <div className="app">
        <Login
          connection={this.state.connection}
          login={this.login}
          visibility={getVisibilityClass(this.state.showLogin)}
        />
        <Lobby
          connection={this.state.connection}
          player={this.state.player}
          logout={this.logout}
          visibility={getVisibilityClass(this.state.showLobby)}
        />
        <Game
          connection={this.state.connection}
          player={this.state.player}
          showGame={this.showGame}
          exitGame={this.exitGame}
          visibility={getVisibilityClass(this.state.showGame)}
        />
      </div>
    );
  }
}
