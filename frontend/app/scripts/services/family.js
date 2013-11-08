'use strict';

angular.module('Canfinder.clientApp')

    .factory('Family', ['$resource', function Family($resource) {

        return $resource('http://localhost:8000/db/families/:familyId', {

            'familyId': '@id'

        }, {

            query:   { method: 'GET' }

        });

    }]);
