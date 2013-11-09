'use strict';

angular.module('Canfinder.clientApp')

    .factory('Breed', ['$resource',

        function ($resource) {
            return $resource('http://localhost\\:8000/db/breeds/:breedId', {}, {
                query: { method: 'GET', params: { breedId: ''}, isArray: true }
            });
        }

    ]);
