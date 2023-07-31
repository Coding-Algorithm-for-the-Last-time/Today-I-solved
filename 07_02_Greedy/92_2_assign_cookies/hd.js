/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);

  let answer = 0;
  for (let i = 0; i < g.length; i++) {
    const idx = s.findIndex((num) => num >= g[i]);
    if (idx === -1) break;

    answer += 1;
    s = s.slice(idx + 1);
  }

  return answer;
};

// Runtime 168ms, 9.55%
// Memory 49.5 MB, 65.4%

/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren2 = function (g, s) {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);

  let j = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= g[j]) j += 1;
  }

  return j;
};

// Runtime 65ms, 92.62%
// Memory 42.3 MB, 43.60%
