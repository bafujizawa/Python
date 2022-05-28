// const num1A = 1;
// const num1B = 1;
// const expected1 = 1;

// const num2A = 5;
// const num2B = 10;
// const expected2 = 10;

// const num3A = 10;
// const num3B = 5;
// const expected3 = 10;

// const num4A = 6;
// const num4B = 8;
// const expected4 = 24;

// const num5A = 15;
// const num5B = 25;
// const expected5 = 75;


// function lowestCommonMultiple(a, b, i=1)
// {
//     // a + b
//     // console.log(i)
//     if(i % a == 0 && i % b == 0)
//     {
//         return i
//     }
//     return lowestCommonMultiple(a, b, ++i)
// }

// console.log(lowestCommonMultiple(num1A, num1B))
// console.log(lowestCommonMultiple(num2A, num2B))
// console.log(lowestCommonMultiple(num3A, num3B))
// console.log(lowestCommonMultiple(num4A, num4B))
// console.log(lowestCommonMultiple(num5A, num5B))

const two_str1 = "1?0?";
const two_expected1 = ["1000", "1001", "1100", "1101"];


function binaryStringExpansion(str, i=0, newList = [])
{
    if(i >= str.length)
    {
        return newList
    }
    if(str[i] === '?')
    {
        newList.push(str.replace('?', '0'))
        newList.push(str.replace('?', '1'))
    }
    return binaryStringExpansion(str, ++i)
}

console.log(binaryStringExpansion(two_str1))