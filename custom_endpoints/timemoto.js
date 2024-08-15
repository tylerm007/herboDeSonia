var IOUtils = Java.type("org.apache.commons.io.IOUtils");
var StandardCharsets = Java.type("java.nio.charset.StandardCharsets");
var inputStream = request.getInputStream();

// get the payload

var result = IOUtils.toString(inputStream, StandardCharsets.UTF_8);
var json = JSON.parse(result);

// Accede a cada campo individualmente

var id = json.id;
var userFullName = json.data.userFullName;
var sequence = json.sequence;

// add additional code to process payload
//var result = IOUtils.toString(inputStream, StandardCharsets.UTF_8);
log.debug(' inputStream '+ result + ">>>>");
//log.debug(' result ' + result);

var res = {result: 'Hello', id :id, userFullName:userFullName};
return JSON.stringify(res);
