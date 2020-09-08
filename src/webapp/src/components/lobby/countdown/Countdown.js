import React from "react";
import "./Countdown.css";

export default (props) => (
  <div className={`countdown ${props.visibility}`}>
    <div className="countdown-modal">
      <div className="countdown-player">
        {props.invite.player
          ? `Game invitation received from ${props.invite.player.name}`
          : "Waiting to accept the invitation"}
      </div>
      <div className="countdown-progress">
        <div
          className="countdown-progress-filler"
          style={{ width: `${props.invite.countdown}%` }}
        ></div>
      </div>
      <div className="countdown-control">
        <button>Accept</button>
        <button>Decline</button>
      </div>
    </div>
  </div>
);
