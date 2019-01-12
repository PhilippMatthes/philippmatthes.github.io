function load(url, targetId, height) {
    var o = "<object style='width: 100%; height: " + height + "px' class='border-2' type='text/html' data=" + url + "></object>";
    $(targetId).html(o);
}