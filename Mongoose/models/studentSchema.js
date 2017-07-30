const mongoose = require('mongoose');
const db = require('./conn_mongo');
var studentSchema = mongoose.Schema({
    name: { type: String },
    age: { type: Number },
    sex: { type: String }
});

var studentModel = db.model('student', studentSchema);

module.exports = studentModel;
