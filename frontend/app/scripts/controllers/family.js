'use strict';

angular.module('Canfinder.clientApp')

    .controller('FamilyCtrl', function ($scope, Family) {

        $scope.families = Family.query();
  });
