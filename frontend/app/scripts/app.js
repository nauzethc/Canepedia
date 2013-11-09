'use strict';

angular.module('Canfinder.clientApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/breeds', {
        templateUrl: 'views/breed-list.html',
        controller: 'BreedListCtrl'
      })
      .when('/breeds/:id', {
        templateUrl: 'views/breed-detail.html',
        controller: 'BreedDetailCtrl'
      })
      .when('/families', {
        templateUrl: 'views/family-list.html',
        controller: 'FamilyCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .config(function ($httpProvider) {
    delete $httpProvider.defaults.headers.common["X-Requested-With"];
  });
