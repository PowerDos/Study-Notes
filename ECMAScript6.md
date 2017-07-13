# ECMAScript6
## 简介
> ECMAScript 6（以下简称ES6）是JavaScript语言的下一代标准，已经在2015年6月正式发布了。Mozilla公司将在这个标准的基础上，推出JavaScript 2.0。<br>

## ECMAScript和JavaScript的关系
> ECMAScript是JavaScript语言的国际标准，JavaScript是ECMAScript的实现。

## ECMAScript 6 的兼容
[http://kangax.github.io/es5-compat-table/es6/](http://kangax.github.io/es5-compat-table/es6/)

## 环境兼容
> 检测浏览器支不支持ES6，不支持就自动转换为ES5<br>

### Traceur转码器
``` HTML
<!-- 加载Traceur编译器 -->
<script src="http://google.github.io/traceur-compiler/bin/traceur.js" type="text/javascript"></script>
<!-- 将Traceur编译器用于网页 -->
<script src="http://google.github.io/traceur-compiler/src/bootstrap.js" type="text/javascript"></script>
<!-- 打开实验选项，否则有些特性可能编译不成功 -->
<script>
        traceur.options.experimental = true;
</script>
<body>...</body>
<!-- ES6代码 -->
<script type="module">
        class Calc {
                constructor(){
                        console.log('Calc constructor');
                }
                add(a, b){
                        return a + b;
                }
        }
        var c = new Calc();
        console.log(c.add(4,5));
</script>
```
### 注意
> script标签的type属性的值是module(或者traceur)，而不是text/javascript。这是Traceur编译器识别ES6代码的标识，编译器会自动将所有type=module的代码编译为ES5，然后再交给浏览器执行。

## 测试环境
> Google Chrome

# let
## 与var的区别
> 它的用法类似于var，但是所声明的变量，只在let命令所在的代码块内有效。

``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>	
</head>
<body>
</body>
<script>
	{
		var a = 100;
		let b = 200;
	}
	console.log(a);
	console.log(b);
</script>
</html>
```
> 结果

![与var的区别](http://i.imgur.com/x5BDlWZ.png)

## 不存在变量提升
> let不像var那样，会发生“变量提升”现象。

``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
</body>
<script>
	console.log("ES5:");
	var a = [];
	for (var i = 0; i < 10; i++){
		var c = i;
		a[i] = function () {
			console.log(c);
		}
	}
	a[5](); //会输出9，因为var c 最后循环过后，c为9

	console.log("ES6:");
	var b = [];
	for (var i = 0; i < 10; i++){
		let d = i;
		a[i] = function(){
			console.log(d);
		}
	}
	a[5]();	 //会打印出5，因为let只会在区域内起作用
</script>
</html>
```
> 结果

![](http://i.imgur.com/yYAK2gR.png)

## 暂时性死区

> 只要块级作用域内存在let命令，它所声明的变量就“绑定”（binding）这个区域，不再受外部的影响。


```HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>let</title>
</head>
<body>
</body>
<script>	
	var a = 200;
	// ***********不受外界影响开始***********
	{	
		// **********暂时性死区开始**********
		console.log(a); //打印undefined
		// **********暂时性死区结束**********
		let a = 100;
		console.log(a);  //打印100
	}
	// ***********不受外界影响结束***********
</script>
</html>
```

## 不允许重复声明
> let不允许在相同作用域内，重复声明同一个变量。

``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>let</title>
</head>
<body>
</body>
<script>
	// 不允许重复声明
	{
		var a = 100;
		var a = 200;
	}
	// 下面三个会报错
	{
		var b = 100;
		let b = 200;
	}
	{
		let c = 100;
		var c = 200;
	}
	{
		let d = 100;
		let d = 200;
	}
</script>
</html>
```

``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>let</title>
</head>
<body>
</body>
<script>
	// 模块之间不影响，可以重复声明
	{
		var a = 100;
		var a = 200;
		console.log(a);
	}
	{
		let a = 300;
		console.log(a);
	}
	// 模块内部不允许用let命令重复声明
	{
		var a = 1;
		let a = 2;
	}
</script>
</html>
```