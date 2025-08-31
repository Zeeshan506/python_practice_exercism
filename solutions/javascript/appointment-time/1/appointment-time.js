// @ts-check

/**
 * Create an appointment
 *
 * @param {number} days
 * @param {number} [now] (ms since the epoch, or undefined)
 *
 * @returns {Date} the appointment
 */
export function createAppointment(days, now = undefined) {
  const current = now ? new Date(now) : new Date();
  const appointment = new Date(current.getTime() + days * 24 * 60 * 60 * 1000)
  return appointment
}
/**
 * Generate the appointment timestamp
 *
 * @param {Date} appointmentDate
 *
 * @returns {string} timestamp
 */
export const getAppointmentTimestamp = date => date.toISOString();

/**
 * Get details of an appointment
 *
 * @param {string} timestamp (ISO 8601)
 *
 * @returns {Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>} the appointment details
 */
export const getAppointmentDetails = ts => { const d = new Date(ts); return { year: d.getFullYear(), month: d.getMonth(), date: d.getDate(), hour: d.getHours(), minute: d.getMinutes() }; };

/**
 * Update an appointment with given options
 *
 * @param {string} timestamp (ISO 8601)
 * @param {Partial<Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>>} options
 *
 * @returns {Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>} the appointment details
 */
export const updateAppointment = (ts, opts) => {
  const d = new Date(ts);
  if ('year' in opts) d.setFullYear(opts.year);
  if ('month' in opts) d.setMonth(opts.month);
  if ('date' in opts) d.setDate(opts.date);
  if ('hour' in opts) d.setHours(opts.hour);
  if ('minute' in opts) d.setMinutes(opts.minute);
  return getAppointmentDetails(d.toISOString());
};
/**
 * Get available time in seconds (rounded) between two appointments
 *
 * @param {string} timestampA (ISO 8601)
 * @param {string} timestampB (ISO 8601)
 *
 * @returns {number} amount of seconds (rounded)
 */
export function timeBetween(timestampA, timestampB) {
  const dateA = new Date(timestampA);
  const dateB = new Date(timestampB);

  const diffMs = Math.abs(dateA.getTime() - dateB.getTime());
  return Math.round(diffMs / 1000);
}

/**
 * Get available times between two appointment
 *
 * @param {string} appointmentTimestamp (ISO 8601)
 * @param {string} currentTimestamp (ISO 8601)
 *
 * @returns {boolean}
 */
export function isValid(appointmentTimestamp, currentTimestamp) {
  const appointment = new Date(appointmentTimestamp);
  const current = new Date(currentTimestamp);

  return appointment.getTime() > current.getTime();
}
