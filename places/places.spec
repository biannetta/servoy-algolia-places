{
	"name": "algolia-places",
	"displayName": "places",
	"version": 1,
	"definition": "algolia/places/places.js",
	"icon": "algolia/places/icon/algoliaPlaces.svg",
	"libraries": [
		{"name":"places.js", "version":"1.4.15", "url":"algolia/lib/places.min.js", "mimetype":"text/javascript"},
		{"name":"places.autocomplete.js", "version":"1.4.15", "url":"algolia/lib/placesAutocompleteDataset.min.js", "mimetype":"text/javascript"},
		{"name":"places.instasearch.js", "version":"1.4.15", "url":"algolia/lib/placesInstantsearchWidget.min.js", "mimetype":"text/javascript"}
	],
	"model": {
		"dataProviderID":{"type": "dataprovider","pushToServer":"allow","tags":{"scope":"design"},"ondatachange": { "onchange":"onDataChangeMethodID"}},
		"placeholderText":{"type":"tagstring"},
		"type":{"type" : "string", "values" : [{"DEFAULT":""},{"City":"city"},{"Country":"country"},{"Address":"address"},{"Bus Stop":"busStop"},{"Train Station":"trainStation"},{"Townhall":"townhall"},{"Airpot":"airport"}]}
	},
	"handlers": {
		"onDataChangeMethodID": {
			"returns": "boolean",
			"parameters": [
				{ "name": "oldValue", "type": "String" },
				{ "name": "newValue", "type": "String" },
 				{ "name": "event", "type": "JSEvent" }
			]
		}
	}
}