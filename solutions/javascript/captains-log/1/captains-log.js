// @ts-check

/**
 * Generates a random starship registry number.
 *
 * @returns {string} the generated registry number.
 */
export function randomShipRegistryNumber() {
  let randomNumber = Math.random() * (9998 - 1001) + 1001;
  randomNumber = Math.floor(randomNumber); 
  return `NCC-${randomNumber}` 
}

/**
 * Generates a random stardate.
 *
 * @returns {number} a stardate between 41000 (inclusive) and 42000 (exclusive).
 */
export function randomStardate() {
  let randomNumber = Math.random() * (42000 - 41001) + 41001;
  return randomNumber;
}

/**
 * Generates a random planet class.
 *
 * @returns {string} a one-letter planet class.
 */
export function randomPlanetClass() {
  let obj = {
    1: "D",
    2: "H",
    3: "J",
    4: "K",
    5: "L",
    6: "M",
    7: "N",
    8: "R",
    9: "T",
    10: "Y",
  }
  let min = 1; 
  let max = 11; 
  let randomNumber = Math.random() * (max-min) + min;
  randomNumber = Math.floor(randomNumber);
  return obj[randomNumber];

  
  console.log(obj)
}
