// @ts-check

/**
 * Double every card in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with every card doubled
 */
export function seeingDouble(deck) {
  const newDeck = deck.map((card) => card *2)
  return newDeck;
}

/**
 *  Creates triplicates of every 3 found in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with triplicate 3s
 */
export function threeOfEachThree(deck) {
  const result = deck.reduce((ax , val) => {
    if (val === 3){
      for (let num = 0; num < 3; num++)
      {ax.final.push(3)}
    }
    else{
      ax.final.push(val);
    }
    return ax;
  }, {final: []});
  return result.final
}


/**
 * Extracts the middle two cards from a deck.
 * Assumes a deck is always 10 cards.
 *
 * @param {number[]} deck of 10 cards
 *
 * @returns {number[]} deck with only two middle cards
 */
export function middleTwo(deck) {
  const removed = deck.splice(4,2);
  return removed;
}

/**
 * Moves the outside two cards to the middle.
 *
 * @param {number[]} deck with even number of cards
 *
 * @returns {number[]} transformed deck
 */

export function sandwichTrick(deck) {
  let arrayCenter = 0
  if (deck.length % 2 === 0)
  {
  arrayCenter =  Math.floor(deck.length/2) -1;
  }
  else{
  arrayCenter =  Math.floor(deck.length/2);
  }
  const first = deck.shift()
  const last = deck.pop()
  deck.splice(arrayCenter,0, first)
  deck.splice(arrayCenter,0, last)
  console.log(deck)
  return deck;
  
}

/**
 * Removes every card from the deck except 2s.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with only 2s
 */
export function twoIsSpecial(deck) {
  const twos = deck.filter((card) => card === 2)
  return twos
}

/**
 * Returns a perfectly order deck from lowest to highest.
 *
 * @param {number[]} deck shuffled deck
 *
 * @returns {number[]} ordered deck
 */
export function perfectlyOrdered(deck) {
deck = deck.sort((a,b) => a-b);
  return deck;
}

/**
 * Reorders the deck so that the top card ends up at the bottom.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} reordered deck
 */
export function reorder(deck) {
  return deck.reverse();
}
