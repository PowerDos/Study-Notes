var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res, next) {
    res.json({ 'username': "Gavin", "sex": "male" });
});

router.get('/jsonp', function(req, res, next){
    res.jsonp({'username': "Gavin", "sex": "male"})
});

router.post('/', function(req, res, next){
    res.json({ 'username': "Gavin", "sex": "male" });
})
module.exports = router;
