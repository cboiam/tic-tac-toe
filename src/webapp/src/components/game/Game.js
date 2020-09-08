import React from "react";

export default class Game extends React.Component {
  componentDidMount() {
    this.props.connection.on("game_create", (data) => {
      const sids = JSON.parse(data);

      if (
        this.props.player.sid !== sids.inviter &&
        this.props.player.sid !== sids.invited
      ) {
        return;
      }

      this.props.showGame();
    });
  }

  render() {
    return <div className={this.props.visibility}>game</div>;
  }
}
