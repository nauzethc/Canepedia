'use strict';

angular.module('canepediaClientApp')
    .controller('BreedFormCtrl', function ($scope, Breed, FCIGroup) {

        $scope.form = {};
        $scope.groups = FCIGroup.query();


        $scope.createBreed = function(form) {

            if (angular.isUndefined(form.name)   ||
                angular.isUndefined(form.origin) ||
                angular.isUndefined(form.group) ) {
                console.log("Incomplete");

            } else {
                Breed.save({}, form,
                    function(resource, status) {
                        console.log("Added!");
                        console.log(status);
                    },

                    function(status) {
                        console.log("Error!");
                        console.log(status);
                    }
                );
            }
        }

    });