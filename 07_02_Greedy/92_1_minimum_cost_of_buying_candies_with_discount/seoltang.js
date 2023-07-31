// Runtime 64 ms Beats 60.16%
// Memory 41.9 MB Beats 95.12%
/**
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function (cost) {
  let sum = 0;

  cost
    .sort((a, b) => b - a)
    .forEach((candy, index) => {
      if ((index + 1) % 3 !== 0) sum += candy;
    });

  return sum;
};
