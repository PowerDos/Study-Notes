const mongoose = require('mongoose');
const db = require('./conn_mongo');
var studentSchema = mongoose.Schema({
    name: { type: String },
    age: { type: Number },
    sex: { type: String }
});

// 查询静态方法， 静态方法在Model层就能使用
studentSchema.statics.findStudentByName = function(name, callback){
    this.model('student').find( {name: name}, callback );
}

// 修改的静态方法
studentSchema.statics.updateStudent = function(conditions, update, options, callback ){
    this.model("student").update(conditions, update, options, callback);
}

var studentModel = db.model('student', studentSchema);

module.exports = studentModel;
