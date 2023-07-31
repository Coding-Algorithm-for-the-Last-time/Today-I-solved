/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function (s) {
  const strings = [...new Set([...s])];
  const lastIndexMap = new Map();
  strings.forEach((string) => {
    lastIndexMap.set(string, s.lastIndexOf(string));
  });
  const result = [];

  let size = 0;
  let max = 0;
  for (let i = 0; i < s.length; i++) {
    size += 1;
    max = Math.max(max, lastIndexMap.get(s[i]));
    if (max === i) {
      result.push(size);
      size = 0;
    }
  }

  return result;
};

// Runtime 57 ms, 96.76%
// Memory 43.6 MB, 62.27%
