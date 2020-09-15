import React from "react";
import "./Countdown.css";

export default (props) => {
  const message = props.invite.player
    ? `Invite received from ${props.invite.player.name}`
    : "Waiting to accept the invitation";

  const controls = props.invite.player ? (
    <div className="countdown-control">
      <button className="button" onClick={props.accept}>Accept</button>
      <button className="button" onClick={props.decline}>Decline</button>
    </div>
  ) : null;

  return (
    <div className={`countdown ${props.visibility}`}>
      <div className="countdown-modal">
        <div className="countdown-player">{message}</div>
        <div className="countdown-progress">
          <div
            className="countdown-progress-filler"
            style={{ width: `${props.invite.countdown}%` }}
          ></div>
        </div>
        {controls}
      </div>
    </div>
  );
};
