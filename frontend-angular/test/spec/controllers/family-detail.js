'use strict';

describe('Controller: FamilyDetailCtrl', function () {

  // load the controller's module
  beforeEach(module('canepediaClientApp'));

  var FamilyDetailCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    FamilyDetailCtrl = $controller('FamilyDetailCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
