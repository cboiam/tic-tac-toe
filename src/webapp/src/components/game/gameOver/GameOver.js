import React from "react";

export default (props) => {
  if (!props.winner) {
    return null;
  }

  const label =
    props.winner.sid === props.player.sid ? "You won!" : "You lose!";

  return (
    <div className="game-over">
      <div>{label}</div>
    </div>
  );
};
