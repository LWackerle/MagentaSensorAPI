const { Service } = require("feathers-mongoose");

exports.Devices = class Devices extends Service {
  async create(data, params) {
    const doc = super.get(data.service_id);
    if (doc) {
      return super.patch(data.service_id, data);
    } else {
      return super.create(data, params);
    }
  }
};
