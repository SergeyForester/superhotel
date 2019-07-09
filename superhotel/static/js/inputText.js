var contentold = {};   //объявляем переменную для хранения неизменного текста
function savedata(elementidsave, contentsave) {   // функция для сохранения отредактированного текста с помощью ajax
    $.ajax({
        url: '/save/',                           // url который обрабатывает и сохраняет наш текст

        data: {
            content: contentsave,     //наш пост запрос
            id: elementidsave
        },
        success: function (data) {      //получили ответ от сервера - обрабатываем

            if (data.result === contentsave)   //сервер прислал нам отредактированый тексn, значит всё ок
            {
                $('#' + elementidsave).html(data.result);        //записываем присланные данные от сервера в элемент, который редактировался
                $('<div id="status">Данные успешно сохранены:' + data.result + '</div>')     //выводим сообщение об успешном ответе сервера
                    .insertAfter('#' + elementidsave)
                    .addClass("success")
                    .fadeIn('fast')
                    .delay(1000)
                    .fadeOut('slow', function () {
                        this.remove();
                    }); //уничтожаем элемент

            } else {
                $('<div id="status">Запрос завершился ошибкой:' + data + '</div>') // выводим данные про ошибку
                    .insertAfter('#' + elementidsave)
                    .addClass("error")
                    .fadeIn('fast')
                    .delay(3000)
                    .fadeOut('slow', function () {
                        this.remove();
                    });  //уничтожаем элемент
            }
        }
    });
}

$(document).ready(function () {
    $('.ForEdit')                 // редактируемый элемент
        .mousedown(function (e)                       //  обрабатываем событие нажатие мышки
        {
            $(this).attr('contenteditable', 'true');
            e.stopPropagation();
            elementid = this.id;
            contentold[elementid] = $(this).html();        // текст до редактирования
            $(this).bind('keydown', function (e) {         // обработчик нажатия Escape
                if (e.keyCode === 27) {
                    e.preventDefault();
                    $(this).html(contentold[elementid]);	// возвращаем текст до редактирования
                }
            });
            $("#save").show();                              // показываем кнопку "сохранить"
        })
        .blur(function (event)                   //  обрабатываем событие потери фокуса
        {
            $(this).removeAttr('contenteditable');
            var elementidsave = this.id;                       // id елемента потерявшего фокус
            var contentsave = $(this).html();           // текст для сохраненния
            event.stopImmediatePropagation();
            if (elementid === elementidsave)    // если id не совпадает с id элемента, потерявшего фокус,
            {
                $("#save").hide();
            }      // значит фокус  в редактируемом элементе, кнопку не прячем

            if (contentsave !== contentold[elementidsave])  // если текст изменился
            {
                savedata(elementidsave, contentsave);   // отправляем на сервер
            }

        });


});