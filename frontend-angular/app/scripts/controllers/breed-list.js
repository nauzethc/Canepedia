'use strict';

angular.module('canepediaClientApp')
    .controller('BreedListCtrl', function ($scope, Breed) {

        $scope.breeds = Breed.query();
        $scope.formTemplate = 'views/breed-form.html';

        $scope.$on('BreedFormCtrl.newBreedAdded', function(event, breed) {
            console.log("Received!");
            $scope.breeds.push(breed);
        });

    });