/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const anagramMap = new Map();

  strs.forEach((str) => {
    const sortedStr = [...str].sort().join('');
    const anagrams = anagramMap.get(sortedStr) || [];
    anagrams.push(str);

    anagramMap.set(sortedStr, anagrams);
  });

  return [...anagramMap.values()];
};
