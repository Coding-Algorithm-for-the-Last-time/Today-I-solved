/**
 * @param {number} num
 * @return {number}
 */
var splitNum = function (num) {
  num = [...String(num)].sort().filter((_num) => Boolean(Number(_num)));
  let num1 = '';
  let num2 = '';
  num.forEach((_num, idx) => {
    if (!(idx % 2)) num1 += _num;
    else num2 += _num;
  });

  return Number(num1) + Number(num2);
};
