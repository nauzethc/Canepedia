'use strict';

angular.module('canepediaClientApp')
    .controller('BreedDetailCtrl', function ($scope, $routeParams, Breed) {

        $scope.showRelated = false;
        $scope.showFamily = false;

        $scope.breed = Breed.get({ breedId: $routeParams.id },
            function(response) {
                if (response.related.length > 0) {
                    $scope.showRelated = true;
                }
                if (response.family.length > 0) {
                    $scope.showFamily = true;
                }
            }
        );
    });