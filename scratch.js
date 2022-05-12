/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/
newString = 'Hello World'

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";

const rotateAmnt6 = 5;
const expected6 = "WorldHello ";

const two_strA1 = "ABCD";
const two_strB1 = "CDAB";
// CDAB -> BCDA -> ABCD
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const two_expected1 = true;

const two_strA2 = "ABCD";
const two_strB2 = "CDBA";
// CDBA -> ACDB -> BACD -> DBAC -> CDBA
// Explanation: all same letters in 2nd string, but out of order
const two_expected2 = false;

const two_strA3 = "ABCD";
const two_strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const two_expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {
    //compare str lengths first
    if (s1.length != s2.length) {
        return false;
    }
    //initalize rotations to push rotations of s1 into array
    let rotations = [];
    for (let i = 0; i < s1.length; i++) {
        rotations.push(rotateStr(s1, i));
    }
    //rotations now has rotations of s1! 
    //going through the rotations to see if any of the permutation is == s2
    for (let temp of rotations) {
        if (temp === s2) {
            return true;
        }
    }
    //if the array is completely through and s2 is NOT a permutation of s1? return false.
    return false;
}



function rotateStr(str, amnt) {
    amnt = amnt % str.length
    let first_half = str.slice(0, str.length - amnt);
    let second_half = str.slice(str.length - amnt);
    return second_half + first_half;
}

console.log(rotateStr(newString, 2))
console.log(rotateStr(newString, 13))
console.log(rotateStr(newString, 123))

// console.log(isRotation(two_strA1, two_strB1));
// console.log(isRotation(two_strA2, two_strB2));
// console.log(isRotation(two_strA3, two_strB3));