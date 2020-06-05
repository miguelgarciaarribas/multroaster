function toggleResults() {
  var results = document.getElementsByClassName('result');
  for(i = 0; i < results.length; i++) {
    if (results[i].style.display === 'inline'){
     results[i].style.display = 'none';
    }  else {
     results[i].style.display = 'inline';
    }
  }
}
