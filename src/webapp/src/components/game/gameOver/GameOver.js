import React from "react";
import "./GameOver.css";

export default (props) => {
  if (!props.winner) {
    return null;
  }

  const label =
    props.winner.sid === props.player.sid ? "You won!" : "You lose!";

  setTimeout(props.exit, 3000);

  return (
    <div className="game-over">
      <div className="game-over-modal">
        <div>{label}</div>
      </div>
    </div>
  );
};
