'use strict';

angular.module('Canfinder.clientApp')

    .factory('Family', ['$resource',

        function ($resource) {
            return $resource('http://localhost\\:8000/db/families/:familyId', {}, {
                query: { method: 'GET', params: { familyId: ''}, isArray: true }
            });
        }

    ]);
