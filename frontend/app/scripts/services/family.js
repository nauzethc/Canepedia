'use strict';

angular.module('Canfinder.clientApp')
    .factory('Family', ['$resource', function ($resource) {

        return $resource('/dogs/families/:familyId', { familyId:'@familyId' });

    }]);