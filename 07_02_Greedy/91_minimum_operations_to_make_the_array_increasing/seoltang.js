/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function (nums) {
  let count = 0;

  nums.reduce((acc, cur) => {
    if (acc < cur) return cur;
    count += acc - cur + 1;
    return acc + 1;
  });

  return count;
};
