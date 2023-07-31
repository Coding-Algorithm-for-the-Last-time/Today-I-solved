/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function (num) {
  num = [...num.toString()]
    .map(Number)
    .filter((num) => !!num)
    .sort((a, b) => a - b);

  if (num.length === 1) return num[0];
  if (num.length === 2) return num[0] + num[1];
  if (num.length === 3) return num[0] * 10 + num[1] + num[2];
  return num[0] * 10 + num[1] * 10 + num[2] + num[3];
};
