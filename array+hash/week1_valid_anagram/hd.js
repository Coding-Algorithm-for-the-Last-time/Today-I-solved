/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const strMap = new Map();

  s.split('').forEach((str) => {
    strMap.set(str, (strMap.get(str) | 0) + 1);
  });

  t.split('').forEach((str) => {
    strMap.set(str, (strMap.get(str) | 0) - 1);
  });

  for ([_, value] of strMap) {
    if (value !== 0) return false;
  }

  return true;
};
