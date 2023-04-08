/**
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function (cost) {
  cost.sort((a, b) => b - a);

  return cost.reduce((acc, cur, idx) => {
    if (idx % 3 !== 2) return acc + cur;
    return acc;
  }, 0);
};

// Runtime 72ms, 21.95%
// Memory 24.9 MB, 21.95%

var minimumCost2 = function (cost) {
  cost.sort((a, b) => b - a);
  let result = 0;
  for (let i = 0; i < cost.length; i++) {
    if (i % 3 !== 2) result += cost[i];
  }

  return result;
};

// Runtime 65ms, 55.29%
// Memory 42.3 MB, 65.4%
