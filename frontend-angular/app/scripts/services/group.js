'use strict';

angular.module('canepediaClientApp')

    .factory('FCIGroup', ['$resource',

        function FCIGroup($resource) {

            return $resource('http://localhost\\:8000/db/groups/:groupId', {},
                {
                    query: { method: 'GET', params: { groupId: ''}, isArray: true }
                }
            );
        }
    ]);