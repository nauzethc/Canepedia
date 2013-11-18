'use strict';

angular.module('canepediaClientApp')
    .controller('BreedListCtrl', function ($scope, Breed) {
        $scope.breeds = Breed.query();
    });