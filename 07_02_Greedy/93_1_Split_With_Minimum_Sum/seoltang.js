// time complexity = O(n log n)
// space complexity = O(n)
/**
 * @param {number} num
 * @return {number}
 */
var splitNum = function (num) {
  const [num1, num2] = [[], []];

  [...num.toString()]
    .sort((a, b) => a - b)
    .forEach((num, index) => {
      index % 2 ? num1.push(num) : num2.push(num);
    });

  const arrToNum = (arr) => Number(arr.join(''));
  return arrToNum(num1) + arrToNum(num2);
};
