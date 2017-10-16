angular.module('algoliaPlaces',['servoy']).directive('algoliaPlaces', function() {  
    return {
      restrict: 'E',
      scope: {
        model: '=svyModel',
        api: "=svyApi",
				handlers: "=svyHandlers",
				svyServoyapi: "="
      },
     controller: function($scope, $element, $attrs) {
        var outerElement = $element.children().first();
        var input = outerElement.children().first()[0];
        var placesAutocomplete = places({
          container: input,
          type: $scope.model.type,
          language: 'en'
        })

        placesAutocomplete.autocomplete[0].placeholder = $scope.model.placeholderText;
        placesAutocomplete.on('change', function(e) {
          $scope.model.dataProviderID = e.suggestion.value;
					$scope.svyServoyapi.apply('dataProviderID');
        });
      },
      templateUrl: 'algolia/places/places.html'
    };
  })