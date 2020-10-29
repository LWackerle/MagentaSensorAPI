const { Service } = require("feathers-mongoose");

exports.Devices = class Devices extends Service {
  async create(data, params) {
    console.log(data);
    const docs = super.find({ device_id: data.service_id });
    if (!docs || docs.length === 0) {
      return super.create(data, params);
    } else {
      return super.patch(data.service_id, data);
    }
  }
};
