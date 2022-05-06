function isPalindrome(str)
{
    for(i=0;i<str.length/2;i++)
    {
        if(str[i] != str[str.length - 1 - i])
        {
            return false
        }
    }
    return true
}

str1 = "a x a";
str2 = "racecar";
str3 = "Dud";
str4 = "oho!";

// console.log(isPalindrome(str1))
// console.log(isPalindrome(str2))
// console.log(isPalindrome(str3))
// console.log(isPalindrome(str4))

function longestPalindrome(str)
{
    substr = ''
    temp = ''
    for(i=0;i<str.length;i++)
    {
        for(j=str.length;j>i;j--)
        {
            substr = str.substring(i,j)
            if(isPalindrome(substr) && substr.length>temp.length)
            {
                temp = substr
            }
        }
    }
    return temp
}


console.log(longestPalindrome("what up, daddy-o?"))
