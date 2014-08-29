var app = angular.module('demo', []);

app.service('LightsService', ['$http',
  function ($http) {
    this.get = function () {

      /// Returns a promise that when resolved, has the data as the first argmuent.
      return $http({
        method: 'GET',
        url: '/api/v1/lights'
      });
    };
}]);

app.controller('LightsController', ['$scope', 'LightsService',
  function ($scope, LightsService) {
    $scope.package = {
      name: 'LightsController'
    };

    LightsService.get().
    success(function (data, status, headers, config) {
      // this callback will be called asynchronously
      // when the response is available
      $scope.data = data;
    }).
    error(function (data, status, headers, config) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
    });

}]);
