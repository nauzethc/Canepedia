'use strict';

angular.module('canepediaClientApp')
    .controller('BreedListCtrl', function ($scope, Breed) {

        $scope.breeds = Breed.query();
        $scope.formTemplate = 'views/breed-form.html';

    });