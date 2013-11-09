'use strict';

describe('Service: Breed', function () {

  // load the service's module
  beforeEach(module('CanfinderClientApp'));

  // instantiate service
  var Breed;
  beforeEach(inject(function (_Breed_) {
    Breed = _Breed_;
  }));

  it('should do something', function () {
    expect(!!Breed).toBe(true);
  });

});
