var student = require('./models/studentSchema');
// 对象操作
// var Gavin = new student({"name": "Gavin2", "age": 20, "sex": "male"});
// Gavin.save(function(){
//     console.log('存储成功');
// })

// Model 操作
// 查询
// student.findStudentByName("Gavin",function(err, result){
//     if(err){
//         console.log(err);
//     }else{
//         console.log(result);
//     }
// });

// 更新
student.updateStudent({name: "Gavin"}, { $set: {age: 21} }, {}, function(err){
    if(err){
        console.log(err);
    }else{
        console.log("修改成功");
    }
});
