// 귀여운 토끼들 ₍⑅ᐢ. ̬.ᐢ₎♡
// time complexity = O(n)
// space complexity = O(n)
/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function (answers) {
  const count = {};

  answers.forEach((answer) => {
    count[answer + 1] = count[answer + 1] ? count[answer + 1] + 1 : 1;
  });

  let sum = 0;

  for (const key in count) {
    sum += key * Math.ceil(count[key] / key);
  }

  return sum;
};
