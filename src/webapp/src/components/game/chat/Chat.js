import React from "react";
import "./Chat.css";

export default class Chat extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      message: "",
    };
  }

  updateMessage = (e) => {
    this.setState({ message: e.target.value });
  };

  onKeyDown = (e) => {
    if (e.key === "Enter") {
      this.sendMessage();
    }
  };

  sendMessage = () => {
    const message = {
      sid: this.props.sid,
      player_sid: this.props.player.sid,
      text: this.state.message,
    };

    this.props.connection.emit("game_message_send", JSON.stringify(message));
    this.setState({ message: "" });
  };

  renderMessage = (message, index) => {
    let messageClass = "chat-message";
    if (this.props.player?.sid === message.sid) {
      messageClass += " chat-message-mine";
    }

    return (
      <div className={messageClass} key={`message-${index}`}>
        <p className="chat-message-text">{message.text}</p>
      </div>
    );
  };

  componentDidMount() {
    this.props.connection.on("game_message_sent", (data) => {
      const message = JSON.parse(data);
      this.props.addMessage(message);
    });
  }

  render() {
    return (
      <div className="chat">
        <div className="chat-messages">
          {this.props.messages.map(this.renderMessage)}
        </div>
        <div className="chat-message-input">
          <input
            onKeyDown={this.onKeyDown}
            type="text"
            value={this.state.message}
            onChange={this.updateMessage}
          />
          <button onClick={this.sendMessage}>Send</button>
        </div>
      </div>
    );
  }
}
