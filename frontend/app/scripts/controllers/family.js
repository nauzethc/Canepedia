'use strict';

angular.module('Canfinder.clientApp')
    .controller('FamilyListCtrl', function ($scope, Family) {
        $scope.families = Family.query();
    });