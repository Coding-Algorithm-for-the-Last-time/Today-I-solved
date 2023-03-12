/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  const [sArr, tArr] = [s.split(''), t.split('')];

  const isContain = sArr.every((sLetter) => {
    const tIndex = tArr.indexOf(sLetter);
    if (tIndex === -1) return false;
    tArr.splice(tIndex, 1);
    return true;
  });

  return isContain && !tArr.length;
};
