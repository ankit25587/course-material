var http = require('http');
var handleRequest = function(request, response) {
  response.writeHead(200);
  response.end("<h1> Hello World to Kubernetes v1.0 </h1>");
}
var www = http.createServer(handleRequest);
www.listen(8080);
