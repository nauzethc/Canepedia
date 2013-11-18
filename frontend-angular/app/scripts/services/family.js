'use strict';

angular.module('canepediaClientApp')

    .factory('Family', ['$resource',

        function Family($resource) {

            return $resource('http://localhost\\:8000/db/families/:familyId', {},
                {
                    query: { method: 'GET', params: { familyId: ''}, isArray: true }
                }
            );
        }
    ]);