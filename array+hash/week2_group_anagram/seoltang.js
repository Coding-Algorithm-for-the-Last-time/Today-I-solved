/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const anagramGroup = {};
  const sortedStrs = strs.map((str) => str.split('').sort().join(''));

  sortedStrs.forEach((sortedStr, index) => {
    const originalStr = strs[index];

    anagramGroup[sortedStr] = anagramGroup.hasOwnProperty(sortedStr)
      ? [...anagramGroup[sortedStr], originalStr]
      : [originalStr];
  });

  return Object.values(anagramGroup);
};
