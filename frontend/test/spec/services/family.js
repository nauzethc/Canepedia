'use strict';

describe('Service: Family', function () {

  // load the service's module
  beforeEach(module('CanfinderClientApp'));

  // instantiate service
  var Family;
  beforeEach(inject(function (_Family_) {
    Family = _Family_;
  }));

  it('should do something', function () {
    expect(!!Family).toBe(true);
  });

});
