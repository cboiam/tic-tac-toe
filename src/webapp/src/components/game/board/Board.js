import React from "react";
import "./Board.css";

export default (props) => {
  const fields = [];

  for (let row = 0; row < props.board.size; row++) {
    for (let column = 0; column < props.board.size; column++) {
      fields.push(
        <div
          className="board-field"
          key={`fields[${row}][${column}]`}
          onClick={() => props.fieldClicked(row, column)}
        >
          <div>{getFieldValue(props.board.fields, row, column)}</div>
        </div>
      );
    }
  }

  return <div className="board">{fields}</div>;
};

const getFieldValue = (fields, row, column) => {
  const field = fields.find(
    (f) => f.coordinate.row === row && f.coordinate.column === column
  );
  return field?.symbol?.value;
};
