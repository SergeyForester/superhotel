let fileForm1 = document.getElementById('photoDescription1')
let fileForm2 = document.getElementById('photoDescription2')
let fileForm3 = document.getElementById('photoDescription3')
let fileForm4 = document.getElementById('photoDescription4')

function handleFileSelect1(evt) {
    var files = evt.target.files;

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }

      var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML =
          [
            '<img src="',
            e.target.result,
            '" title="', escape(theFile.name),
            '"/>'
          ].join('');

          document.getElementById('descrPhoto1').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
    }
  }

function handleFileSelect2(evt) {
    var files = evt.target.files;

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }

      var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML =
          [
            '<img src="',
            e.target.result,
            '" title="', escape(theFile.name),
            '"/>'
          ].join('');

          document.getElementById('descrPhoto2').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
    }
  }

function handleFileSelect3(evt) {
    var files = evt.target.files;

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }

      var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML =
          [
            '<img src="',
            e.target.result,
            '" title="', escape(theFile.name),
            '"/>'
          ].join('');

          document.getElementById('descrPhoto3').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
    }
  }

function handleFileSelect4(evt) {
    var files = evt.target.files;

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }

      var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML =
          [
            '<img src="',
            e.target.result,
            '" title="', escape(theFile.name),
            '"/>'
          ].join('');

          document.getElementById('descrPhoto4').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
    }
  }

  fileForm1.addEventListener('change', handleFileSelect1, false);
  fileForm2.addEventListener('change', handleFileSelect2, false);
  fileForm3.addEventListener('change', handleFileSelect3, false);
  fileForm4.addEventListener('change', handleFileSelect4, false);

