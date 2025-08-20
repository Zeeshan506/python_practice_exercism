/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(remaniningTime = null) {
  if(remaniningTime === 0)
  {
    return "Lasagna is done."
  }
  else if(!remaniningTime)
  {
    return "You forgot to set the timer."
  }
  else if(remaniningTime)
  {
    return "Not done, please wait."
  }
}

export function preparationTime(layers, avgTime = 2) {
  return layers.length * avgTime
}

export function quantities(order) {
  let obj = {
    noodles: 0,
    sauce:0,
  }
  for (let item of order){
    if (item === "sauce"){
      obj[item] += 0.2;
    }
    if(item === "noodles"){
      obj[item]+= 50;
    }
  }
  return obj
}

export function addSecretIngredient(param1,param2) {
  let secret = param1[(param1.length-1)]
  param2.push(secret)
  
} 

export function scaleRecipe(recipe, scaler){
  let recipeChanged = {};
  scaler /= 2;
  for (let key in recipe){
    recipeChanged[key] = recipe[key] * scaler
  } 
  return recipeChanged
}