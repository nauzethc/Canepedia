'use strict';

angular.module('canepediaClientApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
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
        controller: 'FamilyListCtrl'
      })
      .when('/families/:id', {
        templateUrl: 'views/family-detail.html',
        controller: 'FamilyDetailCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .config(function ($httpProvider) {
    //$sceDelegateProvider.resourceUrlWhitelist([
    //  'self',
    //  'http://127.0.0.1:8000/**',
    //]);
    //$httpProvider.defaults.useXDomain = true;
    //$httpProvider.defaults.headers.post['X-CSRFToken'] = $cookiesProvider.csrftoken;
    //$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  });
