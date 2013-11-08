'use strict';

angular.module('Canfinder.clientApp')
    .controller('FamilyCtrl', function ($scope, FamilyCtrl) {

        $scope.families = FamilyCtrl.get();

  });
