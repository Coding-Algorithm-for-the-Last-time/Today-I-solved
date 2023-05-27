/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function (s) {
  const temp = [];

  let countL = 0;
  let countR = 0;
  let start = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === 'R') countR += 1;
    else countL += 1;
    if ((countL !== 0) & (countL === countR)) {
      temp.push(s.slice(start, i + 1));
      start = i + 1;
      countL = 0;
      countR = 0;
    }
  }

  return temp.length;
};
