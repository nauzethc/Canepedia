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
      .when('/families', {
        templateUrl: 'views/families.html',
        controller: 'FamilyCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
