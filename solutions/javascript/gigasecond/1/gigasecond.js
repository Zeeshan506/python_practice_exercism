//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const gigasecond = (date) => {
  
  const giga_sec = 1000000000
  const input = new Date(date)
  const start = Math.floor(input/1000)
  const time1 = start + giga_sec
  const res = new Date(time1 * 1000)
  return res
};
