let fileFormBooking1 = document.getElementById('bookingPhotoForm1')
let fileFormBooking2 = document.getElementById('bookingPhotoForm2')
let fileFormBooking3 = document.getElementById('bookingPhotoForm3')

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

          document.getElementById('bookingPhoto1').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
      addClass();
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

          document.getElementById('bookingPhoto2').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
      addClass();
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

          document.getElementById('bookingPhoto3').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
      addClass();
    }
  }



function addClass(){
       document.getElementsByClassName('bookingPhotoContainer')[0].classList.add('height200px');

}

fileFormBooking1.addEventListener('change', handleFileSelect1, false);
fileFormBooking2.addEventListener('change', handleFileSelect2, false);
fileFormBooking3.addEventListener('change', handleFileSelect3, false);


