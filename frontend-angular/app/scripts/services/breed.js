'use strict';

angular.module('canepediaClientApp')

    .factory('Breed', ['$resource',

        function Breed($resource) {

            return $resource('http://localhost\\:8000/db/breeds/:breedSlug', {},
                {
                    query: { method: 'GET', params: { breedSlug: ''}, isArray: true }
                }
            );
        }
    ]);