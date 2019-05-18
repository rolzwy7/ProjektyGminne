app.controller("ProjektViewCtrl", function($scope, $http, $timeout){
  $scope.data = {
    currency: "",
    button_text: "Zagłosuj",
    message_text: "",
    message_visible: false,
    message_class: "message",
    vote_temp_disabled: false,
    vote_class: "button is-success",
    vote_icon: "fas fa-vote-yea",
    vote_input_visible: false,
    vote_button_visible: true,
    vote_loading_visible: false,
    vote_num_visible: false,
    lock_vote_: false,
    pesel: "",
    after_vote_add: 0,
    regexp: "^[0-9]{11}$"
  };
  $scope.funcs = {
    vote_init: function(){
      if($scope.data.lock_vote_ != true) {
         $scope.data.vote_input_visible = true;
         $scope.data.vote_button_visible = false;
      }
    },
    lock_button: function(){
      $scope.data.vote_input_visible = false;
      $scope.data.vote_button_visible = false;
      $scope.data.vote_loading_visible = true;
    },
    unlock_button: function(){
      $scope.data.vote_input_visible = false;
      $scope.data.vote_button_visible = true;
      $scope.data.vote_loading_visible = false;
    },
    button_vote_success: function(){
      $scope.data.button_text = "Głos oddany";
      $scope.data.vote_icon = "fas fa-check";
      $scope.data.vote_class = "button is-info";
      $scope.data.lock_vote_ = true;
      $scope.data.vote_num_visible = true;
    },
    button_vote_failure: function(){
      $scope.data.button_text = "Wystąpił błąd. Spróbuj ponownie";
      $scope.data.vote_icon = "fas fa-times";
      $scope.data.vote_class = "button is-danger";
    },
    confirm_timeout: function(projekt_id, csrfmiddlewaretoken){
      console.log(projekt_id, csrfmiddlewaretoken);
      if($scope.data.pesel != "") {
        $http({
          method: 'POST',
          url: '/konkursy/vote',
          data: {
            "pesel": $scope.data.pesel,
            "project_id": projekt_id
          }
        }).then(function successCallback(response) {
          $scope.data.message_text = response.data.msg;
          if(response.data.voted_before) {
            $scope.data.vote_num_visible = true;
          }
          if(!response.data.success) {
            $scope.data.message_class = "message is-danger";
            $scope.funcs.button_vote_failure();
          } else {
            $scope.data.message_class = "message is-info";
            $scope.data.after_vote_add = 1;
            $scope.funcs.button_vote_success();
          }
          $scope.funcs.unlock_button();
          $scope.data.message_visible = true;
        }, function errorCallback(response) {
          $scope.funcs.unlock_button();
          $scope.funcs.button_vote_failure();
        });

      }
    },
    confirm: function(projekt_id, csrfmiddlewaretoken){
      if($scope.data.lock_vote_ == true) {
        console.log("vote locked");
      } else {
        $scope.funcs.lock_button();
        $timeout(function(){$scope.funcs.confirm_timeout(projekt_id, csrfmiddlewaretoken);}, 1000);
      }
    }
  };
});
