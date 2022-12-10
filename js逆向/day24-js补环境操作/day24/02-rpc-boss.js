

(function () {
    var newElement = document.createElement("script");
    newElement.setAttribute("type", "text/javascript");
    newElement.setAttribute("src", "https://sekiro.virjar.com/sekiro-doc/assets/sekiro_web_client.js");
    document.body.appendChild(newElement);
    function guid() {
        function S4() {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
        }
        return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
    }
    function startSekiro() {
        var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=rpc-xl&clientId=" + guid());

        client.registerAction("des", function (request, resolve, reject) {
            // resolve(n);
            var _e = request['e']
            var _t = request['t']
            var _n = (new a).z(_e, parseInt(_t) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3)
            resolve(_n)
        })
    }
    setTimeout(startSekiro, 1000)
})();


