'use strict';

angular.module('Canfinder.clientApp')
    .controller('BreedListCtrl', function ($scope, Breed) {
        $scope.breeds = Breed.query();
    });

angular.module('Canfinder.clientApp')
    .controller('BreedDetailCtrl', function ($scope, $routeParams, Breed) {
        $scope.showRelated = false;
        $scope.breed = Breed.get({ breedId: $routeParams.id },
            function(response) {
                if (response.related.length > 0) {
                    $scope.showRelated = true;
                }
            }
        );
    });