'use strict';

angular.module('canepediaClientApp')
    .controller('BreedFormCtrl', function ($scope, $routeParams, Breed, FCIGroup) {

        $scope.form = {};

        if ($routeParams.slug) {
            var breed = Breed.get({ breedSlug: $routeParams.slug }, function(breed) {

                // Populate breed info to form
                $scope.form = {
                    name:      breed.name,
                    origin:    breed.origin,
                    wikipedia: breed.wikipedia,
                    group:     breed.group
                }
                $scope.form.related = new Array();
                for (var i=0, max=breed.related.length; i<max; i++) {
                    $scope.form.related.push(breed.related[i].id);
                }
                console.log($scope.form);

            });

            // Get breeds list to populate form
            $scope.breeds = Breed.query();
        }

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

        $scope.updateBreed = function(form) {

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
                breed.name = form.name;
                breed.origin = form.origin;
                breed.wikipedia = form.wikipedia;
                breed.group = form.group;
                breed.related = form.related;
                breed.$save();
            }
        }

    });