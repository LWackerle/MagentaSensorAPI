const { Service } = require("feathers-mongoose");

exports.Devices = class Devices extends Service {
  async create(data, params) {
    if (data && data.device_id) {
      const req = await super.find({ query: { device_id: data.device_id } });
      if (!req || !req.data || req.data.length === 0) {
        return super.create(data, params);
      } else {
        return super.patch(data.device_id, data);
      }
    }
  }
};
