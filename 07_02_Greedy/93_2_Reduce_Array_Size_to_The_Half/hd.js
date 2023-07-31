/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function (arr) {
  const numbers = {};
  arr.forEach((num) => {
    numbers[num] = (numbers[num] || 0) + 1;
  });

  let sum = 0;
  let answer = 0;
  Object.values(numbers)
    .sort((a, b) => b - a)
    .some((num) => {
      sum += num;
      answer += 1;
      return sum >= arr.length / 2;
    });

  return answer;
};
