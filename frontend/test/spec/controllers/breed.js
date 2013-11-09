'use strict';

describe('Controller: BreedCtrl', function () {

  // load the controller's module
  beforeEach(module('Canfinder.clientApp'));

  var BreedCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    BreedCtrl = $controller('BreedCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
