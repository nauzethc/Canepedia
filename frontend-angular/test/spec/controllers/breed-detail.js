'use strict';

describe('Controller: BreedDetailCtrl', function () {

  // load the controller's module
  beforeEach(module('canepediaClientApp'));

  var BreedDetailCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    BreedDetailCtrl = $controller('BreedDetailCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
