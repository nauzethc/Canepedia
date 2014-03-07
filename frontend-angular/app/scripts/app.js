'use strict';

angular.module('canepediaClientApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ngAnimate'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        nav: ''
      })
      .when('/breeds', {
        templateUrl: 'views/breed-list.html',
        controller: 'BreedListCtrl',
        nav: 'breeds'
      })
      .when('/breeds/:slug', {
        templateUrl: 'views/breed-detail.html',
        controller: 'BreedDetailCtrl',
        nav: 'breeds'
      })
      .when('/breeds/edit/:slug', {
        templateUrl: 'views/breed-edit.html',
        controller: 'BreedFormCtrl',
        nav: 'breeds'
      })
      .otherwise({
        redirectTo: '/',
        nav: ''
      });
  })
  .run(function ($rootScope) {
    $rootScope.$on('$routeChangeSuccess', function(ev, data) {
      if (data.$$route && data.$$route.nav) {
        $rootScope.nav = data.$$route.nav;
      }
    });
  })
  .config(function ($httpProvider, $cookiesProvider, $sceDelegateProvider) {
    $sceDelegateProvider.resourceUrlWhitelist([
      'self',
      'http://localhost:8000/**',
    ]);
    //$httpProvider.defaults.useXDomain = true;
    //$httpProvider.defaults.headers.post['X-CSRFToken'] = $cookiesProvider.csrftoken;
    //$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  })
  .directive('holderjs', function () {
    return {
        link: function (scope, element, attrs) {
            Holder.run({ images: element[0], nocss: true });
        }
    };
});
