function submit(){
    var form = $("form");
    var d = doSimpleXMLHttpRequest('/ajax/input/', form);
    d.addCallbacks(onSuccess, onFail);
}
onSuccess = function (data){
    var output = $("output");
    output.innerHTML = data.responseText;
    showElement(output);
}
onFail = function (data){
    alert(data);
}
function init() {
    var btn = $("submit");
    btn.onclick = submit;
    var output = $("output");
    hideElement(output);
}

addLoadEvent(init);