require.config({
  baseUrl: ".",
  paths: {
      "polymer": "polymer/",
      "midi" : "midi"
  }
});
require(['polymer/webcomponent.js'], function () {
    // my_module.my_method();
})

// ++resource++midiplayer/bower_components/webcomponentsjs/webcomponents.js