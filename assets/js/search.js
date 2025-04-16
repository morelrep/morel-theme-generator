(function() {
  // Function to display search results
  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('search-results');

    if (results.length) { // Are there any results?
      var appendString = '';

      for (var i = 0; i < results.length; i++) {  // Iterate over the results
        var item = store[results[i].ref];
        
        // Construct the URL with the base path
        var basePath = '/morel-theme-generator'; // Replace with your actual base path
        var url = basePath + item.url; // Concatenate base path with item.url

        // Build the HTML string for each search result item
        appendString += '<li><a href="' + url + '"><h3>' + item.title + '</h3></a>';
        appendString += '<p>' + item.content.substring(0, 150) + '...</p></li>';
      }

      // Update the search results container with the generated HTML
      searchResults.innerHTML = appendString;
    } else {
      // Display a message if no results are found
searchResults.innerHTML = '<p>Aún esa obra o esa autora no están disponibles. <a href="/morel-theme-generator/add">Sugiere su incorporación</a></p>';
    }
  }

  // Function to get query variables from URL
  function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');

    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split('=');

      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      }
    }
  }

  // Get the search query from URL parameter
  var searchTerm = getQueryVariable('query');

  if (searchTerm) {
    // Set the search box value with the retrieved search term
    document.getElementById('search-box').setAttribute("value", searchTerm);

    // Initialize Lunr.js for search indexing
    var idx = lunr(function () {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('author');
      this.field('content');
    });

    // Add data to Lunr.js index from window.store
    for (var key in window.store) {
      idx.add({
        'id': key,
        'title': window.store[key].title,
        'author': window.store[key].author,
        'content': window.store[key].content
      });
    }

    // Perform search using Lunr.js
    var results = idx.search(searchTerm);
    
    // Display search results
    displaySearchResults(results, window.store);
  }
})();
