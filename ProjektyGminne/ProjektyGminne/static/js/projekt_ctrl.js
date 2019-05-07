app.controller("ProjektViewCtrl", function($scope, $http, $timeout){
  $scope.data = {
    wartosc_projektu: "{{object.wartosc_projektu}}",
    kwota_dofinansowania: "{{object.kwota_dofinansowania}}",
    currency: "",
    vote_temp_disabled: false,
    vote_class: "button is-success",
    vote_input_visible: false,
    vote_button_visible: true,
    vote_loading_visible: false,
    pesel: "12345678901",
    regexp: "^[0-9]{11}$"
  };
  $scope.funcs = {
    vote_init: function(){
      $scope.data.vote_input_visible = true;
      $scope.data.vote_button_visible = false;
    },
    confirm: function(projekt_id, csrfmiddlewaretoken){
      console.log(projekt_id, csrfmiddlewaretoken);
      if($scope.data.pesel != "") {
        $scope.data.vote_input_visible = false;
        $scope.data.vote_button_visible = false;
        $scope.data.vote_loading_visible = true;

        $http({
          method: 'GET',
          url: '/konkursy/vote?pesel='+$scope.data.pesel+"&pid=" + projekt_id
        }).then(function successCallback(response) {
          console.log(response);
        }, function errorCallback(response) {
          console.log(response);
        });

      }
    }
  };
});
