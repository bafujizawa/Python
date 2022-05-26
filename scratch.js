const two_nums1 = [1, 3, 5, 6];
const two_searchNum1 = 4;
const two_expected1 = false;

const two_nums2 = [4, 5, 6, 8, 12];
const two_searchNum2 = 5;
const two_expected2 = true;

const two_nums3 = [3, 4, 6, 8, 12];
const two_searchNum3 = 3;
const two_expected3 = true;



function binarySearch(arr, n) {
    let mid = Math.floor(arr.length / 2);
    if (arr.length === 1 && arr[0] != n) {
    return false;
    }
    if (n === arr[mid]) {
        return true;
    } else if (n < arr[mid]) {
        return binarySearch(n, arr.slice(0, mid));
    } else if (n > arr[mid]) {
        return binarySearch(n, arr.slice(mid));
    }
}

console.log(binarySearch(two_nums1, two_expected1))
console.log(binarySearch(two_nums2, two_expected2))
console.log(binarySearch(two_nums3, two_expected3))
