const devices = require('./devices/devices.service.js');
const history = require('./history/history.service.js');
// eslint-disable-next-line no-unused-vars
module.exports = function (app) {
  app.configure(devices);
  app.configure(history);
};
