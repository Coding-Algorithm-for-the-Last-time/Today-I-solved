/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function (num) {
  const nums = [...String(num)];
  const index = nums.indexOf('6');
  if (index === -1) return num;

  nums.splice(nums.indexOf('6'), 1, '9');
  return Number(nums.join(''));
};
