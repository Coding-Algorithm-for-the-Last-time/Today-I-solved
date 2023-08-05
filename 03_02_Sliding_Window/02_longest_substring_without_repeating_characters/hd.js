/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s === '') return 0;
  if (s.length === new Set(s).size) return s.length;

  let temp = [];
  let left = 0;
  let right = 0;

  let answer = [];

  while (left < s.length) {
    if (temp.includes(s[right])) {
      answer.push(temp.filter((item) => item).length);
      temp = [];
      left += 1;
      right = left;
    } else {
      temp.push(s[right]);
      right += 1;
    }
  }

  return Math.max(...answer, temp.length);
};
