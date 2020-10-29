const { Service } = require("feathers-mongoose");

exports.Devices = class Devices extends Service {
  async create(data, params) {
    if (data && data.device_id) {
      const docs = super.find({ query: { device_id: data.device_id } });
      if (!docs || docs.length === 0) {
        return super.create(data, params);
      } else {
        return super.patch(data.service_id, data);
      }
    }
  }
};
