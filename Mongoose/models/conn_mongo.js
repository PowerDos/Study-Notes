const mongoose = require('mongoose');
var db = mongoose.createConnection('mongodb://localhost/School');
db.on('error', function(err){
    console.log("connect error: " + err);
});
db.once('open', function(callback){
    console.log('数据库连接成功');
});
module.exports = db;
