/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function (num) {
  const nums = [...num.toString()].map((num) => Number(num)).sort((a, b) => a - b);
  return (nums[0] + nums[1]) * 10 + nums[2] + nums[3];
};
