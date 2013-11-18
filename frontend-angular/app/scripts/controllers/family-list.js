'use strict';

angular.module('canepediaClientApp')
    .controller('FamilyListCtrl', function ($scope, Family) {
        $scope.families = Family.query();
    });