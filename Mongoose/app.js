var student = require('./models/studentSchema');
var Gavin = new student({"name": "Gavin", "age": 20, "sex": "male"});
Gavin.save(function(){
    console.log('存储成功');
})