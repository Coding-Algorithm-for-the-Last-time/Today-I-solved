/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function (s) {
  let count = 0;
  let answer = 0;

  [...s].forEach((char) => {
    count += { L: -1, R: +1 }[char];
    if (count === 0) answer += 1;
  });

  return answer;
};
