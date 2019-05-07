app.controller("HomepageModalCtrl", function($rootScope, $scope, $http, $timeout, $q){
  $scope.modal_data = {
    modal_class: "modal",
    projekt_data: {},
    konkurs_data: {}
  };

  $scope.modal_funcs = {
    closeModal: function(){
      $scope.modal_data.modal_class = "modal";
    },
    load_projects: function() {
        $http({
          method: 'GET',
          url: '/kfp/' + $scope.modal_data.konkurs_data.id
        }).then(function successCallback(response) {
          $scope.modal_data.projekt_data = response.data;
        }, function errorCallback(response) {
          console.log(response);
        });
    }
  };

  $rootScope.$on('ShowListOfProjects', function(event, konkurs_data) {
    console.log(konkurs_data);
    $scope.modal_data.modal_class = "modal is-active";
    $scope.modal_data.konkurs_data = konkurs_data;
    $scope.modal_funcs.load_projects();
  });


});


app.controller("KonkursyListingCtrl", function($rootScope, $scope, $http, $timeout, $q){
  $scope.data = {
    "odk_array": [],
    "ozk_array": []
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
    },
    replace_jinja_href: function(jinja_href, my_pk) {
      return jinja_href.replace('123', my_pk);
    },
    project_list_emit: function(konkurs_data) {
      $rootScope.$broadcast("ShowListOfProjects", konkurs_data);
    }
  };
  $http({
    method: 'GET',
    url: '/api/q/aktywne_konkursy/?format=json&ordering=-date_start'
  }).then(function successCallback(response) {
    $scope.data.odk_array = response.data.results;
  }, function errorCallback(response) {
    console.log(response);
  });
  $http({
    method: 'GET',
    url: '/api/q/zakonczone_konkursy/?format=json&ordering=-date_finish'
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
    $http({
      method: 'GET',
      url: '/api/q/projekt/?format=json'
    }).then(function successCallback(response) {
      $scope.data.opublikowanych_projektow.count = response.data.count;
      $scope.data.opublikowanych_projektow.loading = false;
    }, function errorCallback(response) {
      console.log(response);
    });
  }, 300);


});
