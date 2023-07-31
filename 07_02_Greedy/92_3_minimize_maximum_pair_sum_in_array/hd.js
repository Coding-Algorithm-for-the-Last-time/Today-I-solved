/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function (nums) {
  nums.sort((a, b) => a - b);
  let max = 0;
  let tail = nums.length - 1;
  for (let i = 0; i < nums.length / 2; i++) {
    max = Math.max(max, nums[i] + nums[tail - i]);
  }

  return max;
};

// Runtime 361ms, 75%
// Memory 56.6 MB, 88.51%
