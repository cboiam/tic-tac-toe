import React from "react";
import "./Lobby.css";
import { getVisibilityClass } from "../../helpers/visibility";
import Countdown from "./countdown/Countdown";

export default class Lobby extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      players: [],
      invite: {
        player: null,
        countdown: 0,
      },
    };
  }

  componentDidMount() {
    this.props.connection.on("player_connect", (players) => {
      this.setState({ players: JSON.parse(players) });
    });

    this.props.connection.on("player_disconnect", (sid) => {
      const players = [...this.state.players];
      const player = players.findIndex((p) => p.sid === sid);
      players.splice(player, 1);

      this.setState({ players });
    });

    this.props.connection.on(`player_invite_receive`, (data) => {
      const invite = JSON.parse(data);

      if (invite.sid !== this.props.player?.sid) {
        return;
      }

      this.createInviteCountdown(data.player);
    });
  }

  createInviteCountdown = (player) => {
    this.setState({
      invite: {
        player: player,
        countdown: 100,
      },
    });

    this.startCountdown();
  };

  startCountdown = () => {
    let timer = setTimeout(() => {
      const countdown = this.state.invite.countdown - 1;
      this.setState({ invite: { countdown } });

      if (countdown === 0) {
        clearTimeout(timer);
        return;
      }

      timer = this.startCountdown();
    }, 100);
  };

  logout = () => {
    this.props.connection.emit(
      "player_leave",
      this.props.player.sid,
      this.props.logout
    );
  };

  invite = (sid) => {
    this.props.connection.emit("player_invite_send", sid, () => {
      this.createInviteCountdown(null);
    });
  };

  renderPlayer = (player) => {
    return (
      <div className="lobby-player" key={player.sid}>
        <div>{player.name}</div>
        <div>
          <button onClick={() => this.invite(player.sid)}>Invite</button>
        </div>
      </div>
    );
  };

  showCountdown = () => this.state.invite.countdown > 0;

  render() {
    return (
      <div className={`lobby ${this.props.visibility}`}>
        <div>
          <button onClick={this.logout}>Leave</button>
        </div>
        {this.state.players
          .filter((p) => p.sid !== this.props.player?.sid)
          .map(this.renderPlayer)}
        <Countdown
          invite={this.state.invite}
          visibility={getVisibilityClass(this.showCountdown)}
        />
      </div>
    );
  }
}
