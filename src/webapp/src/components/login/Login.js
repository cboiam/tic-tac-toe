import React from "react";
import "./Login.css";

export default class extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
    };
  }

  updateUsername = (e) => {
    this.setState({ username: e.target.value });
  };

  submit = (e) => {
    e.preventDefault();

    const json = JSON.stringify({
      sid: this.props.connection.id,
      username: this.state.username,
    });

    this.props.connection.emit("player_enter", json, (data) => {
      this.props.login(JSON.parse(data));
    });
  };

  render() {
    return (
      <div className={`login ${this.props.visibility}`}>
        <div>
          <h1 className="login-title">Welcome to Tic tac toe!</h1>

          <div>
            <form onSubmit={this.submit}>
              <p>Enter your name to start</p>
              <input
                type="text"
                value={this.state.username}
                onChange={this.updateUsername}
              />
              <button>Start</button>
            </form>
          </div>
        </div>
      </div>
    );
  }
}
