'use strict';

describe('Controller: BreedFormCtrl', function () {

  // load the controller's module
  beforeEach(module('canepediaClientApp'));

  var BreedFormCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    BreedFormCtrl = $controller('BreedFormCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
