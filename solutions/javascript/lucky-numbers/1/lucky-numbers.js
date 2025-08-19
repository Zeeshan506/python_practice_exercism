// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  
  let num1 = String(array1);
  num1 = Number(num1.replace(/,/g , ""));
  let num2 = String(array2);
  num2 = Number(num2.replace(/,/g , ""));

  return num1 + num2
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
 let number = String(value)
 let newNumber = number.split("").reverse().join("")
 return number === newNumber
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
  if(!input){
    return 'Required field'
  } else if(!Number(input)){
    return "Must be a number besides 0"
  }
  return ""
}
