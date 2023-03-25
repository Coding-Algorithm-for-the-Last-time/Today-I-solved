/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
  nums = nums.filter((num) => num > 0).sort((a, b) => a - b);
  nums = [...new Set(nums)];

  let answer = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== i + 1) {
      answer = i + 1;
      break;
    }
  }

  return !answer ? nums.length + 1 : answer;
};
