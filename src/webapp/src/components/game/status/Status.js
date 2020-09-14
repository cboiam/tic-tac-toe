import React from "react";

export default (props) => {
  const player = props.players.find((p) => p.sid === props.turn);

  let turn = "Your turn";
  if (player.sid !== props.player.sid) {
    turn = `${player.name}'s turn`;
  }

  return <h4 className="status">{turn}</h4>;
};
