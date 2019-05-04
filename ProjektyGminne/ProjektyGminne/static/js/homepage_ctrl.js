app.controller("KonkursyListingCtrl", function($scope, $http, $timeout, $q){
  $scope.data = {
    "odk_array": [1, 2, 3],
    "ozk_array": [1, 2, 3, 4]
  };
  $scope.funcs = {
    date_diff_days_from_now: function(date_) {
      var ret = Math.floor((new Date() - new Date(date_)) / (1000*60*60*24))
      var postfix;
      if(ret == 1)
        postfix = "dzień";
      else
        postfix = "dni";
      return ret.toString() + " " + postfix + " temu"
    }
  };
  $http({
    method: 'GET',
    url: '/api/q/aktywne_konkursy/?format=json'
  }).then(function successCallback(response) {
    $scope.data.odk_array = response.data.results;
  }, function errorCallback(response) {
    console.log(response);
  });
  $http({
    method: 'GET',
    url: '/api/q/zakonczone_konkursy/?format=json'
  }).then(function successCallback(response) {
    console.log(response);
    $scope.data.ozk_array = response.data.results;
  }, function errorCallback(response) {
    console.log(response);
  });
});

app.controller("HomepageStatsCtrl", function($scope, $http, $timeout){
  $scope.data = {
    "aktywnych_konkursow": {
      "count": 0,
      "loading": true
    },
    "zakonczonych_konkursow": {
      "count": 0,
      "loading": true
    },
    "opublikowanych_projektow": {
      "count": 0,
      "loading": true
    },
    "oddanych_glosow": {
      "count": 0,
      "loading": true
    }
  };
  $timeout(function() {
    $http({
      method: 'GET',
      url: '/api/q/aktywne_konkursy/?format=json'
    }).then(function successCallback(response) {
      $scope.data.aktywnych_konkursow.count = response.data.count;
      $scope.data.aktywnych_konkursow.loading = false;
    }, function errorCallback(response) {
      console.log(response);
    });
    $http({
      method: 'GET',
      url: '/api/q/zakonczone_konkursy/?format=json'
    }).then(function successCallback(response) {
      $scope.data.zakonczonych_konkursow.count = response.data.count;
      $scope.data.zakonczonych_konkursow.loading = false;
    }, function errorCallback(response) {
      console.log(response);
    });
    $http({
      method: 'GET',
      url: '/api/q/glos/?format=json'
    }).then(function successCallback(response) {
      $scope.data.oddanych_glosow.count = response.data.count;
      $scope.data.oddanych_glosow.loading = false;
    }, function errorCallback(response) {
      console.log(response);
    });
  }, 300);


});
