'use strict';

angular.module('canepediaClientApp')
    .controller('BreedFormCtrl', function ($scope, Breed, FCIGroup) {

        $scope.form = {};
        $scope.alert = {
            name : '',
            message : '',
            show : false
        }

        $scope.groups = FCIGroup.query();


        $scope.createBreed = function(form) {

            if (angular.isUndefined(form.name)   ||
                angular.isUndefined(form.origin) ||
                angular.isUndefined(form.group) ) {
                console.log("Incomplete");
                $scope.alert = {
                    name : 'alert-warning',
                    message: 'Some forms fields required',
                    show : true
                }

            } else {
                Breed.save({}, form,
                    function(resource, status) {
                        // Eimt event for new one added
                        $scope.$emit('BreedFormCtrl.newBreedAdded', resource);
                        // Clean form
                        $scope.breedForm.$setPristine();
                        $scope.form = {};
                        // Show alert
                        $scope.alert = {
                            name : 'alert-success',
                            message: 'Breed added!',
                            show : true
                        }
                    },

                    function(status) {
                        console.log("Error!");
                        console.log(status);
                        $scope.alert = {
                            name : 'alert-danger',
                            message: 'There was a problem!',
                            show : true
                        }
                    }
                );
            }
        }

    });