const app = require('../../src/app');

describe('\'history\' service', () => {
  it('registered the service', () => {
    const service = app.service('history');
    expect(service).toBeTruthy();
  });
});
