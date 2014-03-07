'use strict';

angular.module('canepediaClientApp')
    .controller('BreedDetailCtrl', function ($scope, $routeParams, Breed, FCIGroup) {

        $scope.showRelated = false;

        $scope.breed = Breed.get({ breedSlug: $routeParams.slug },
            function(response) {
                if (response.related.length > 0) {
                    $scope.showRelated = true;
                }
            }
        );
    });