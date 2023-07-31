/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function (answers) {
  const _answers = {};
  answers.forEach((answer) => {
    _answers[answer + 1] = (_answers[answer + 1] || 0) + 1;
  });

  return Object.entries(_answers).reduce(
    (sum, [a, b]) => sum + Math.ceil(b / Number(a)) * Number(a),
    0
  );
};
