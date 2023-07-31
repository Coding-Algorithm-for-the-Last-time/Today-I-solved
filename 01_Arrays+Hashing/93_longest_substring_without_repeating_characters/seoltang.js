/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let left = 0;
  let maxLength = 0;
  let charSet = new Set();

  for (let right = 0; right < s.length; right++) {
    const char = s[right];

    while (charSet.has(char)) {
      charSet.delete(s[left]);
      left += 1;
    }

    charSet.add(char);

    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
};
