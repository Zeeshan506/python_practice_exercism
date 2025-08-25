/// <reference path="./global.d.ts" />
//
// @ts-check

/**
 * Determine the price of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(pizza, ...extras) {
  let basePrice = 0;
  switch(pizza){
    case "Margherita":
      basePrice = 7;
      break;
    case "Caprese":
      basePrice = 9;
      break;
    case "Formaggio":
      basePrice = 10;
      break;
    default:
      basePrice = 0;
  }

  function extraPrice(extraList){
    if (extraList.length === 0){
      return 0;
    }
    let price = 0;
    const [first, ...rest] = extraList;
    if (first === "ExtraSauce") price = 1; 
    if (first === "ExtraToppings") price = 2;
    return price + extraPrice(rest);
  }
  return basePrice + extraPrice(extras);
}

/**
 * Calculate the price of the total order, given individual orders
 *
 * (HINT: For this exercise, you can take a look at the supplied "global.d.ts" file
 * for a more info about the type definitions used)
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */
export function orderPrice(pizzaOrders) {
  let price = 0;
  for (let i = 0; i < pizzaOrders.length; i++) {
    const {pizza, extras} = pizzaOrders[i];
    console.log(pizza)
    console.log(extras)
    price += pizzaPrice(pizza, ...extras);
  }
  return price;
}