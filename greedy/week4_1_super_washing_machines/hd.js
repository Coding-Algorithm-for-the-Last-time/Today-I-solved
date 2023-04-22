/**
 * @param {number[]} machines
 * @return {number}
 */
var findMinMoves = function (machines) {
  const allDresses = machines.reduce((acc, cur) => acc + cur, 0);

  if (allDresses % machines.length !== 0) return -1;

  const average = allDresses / machines.length;
  const max = Math.max(...machines) - average;

  return machines.reduce(
    (acc, cur) => {
      let [max, sum] = acc;
      sum += cur - average;
      max = Math.max(max, Math.abs(sum));
      return [max, sum];
    },
    [max, 0]
  )[0];
};

// Runtime 60 ms Beats 83.5%
