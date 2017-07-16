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
# 块级作用域
## ES5出现的问题
> 场景一: 内层变量可能会覆盖外层变量

``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>块级作用域</title>
</head>
<body>
</body>
<script>
	var time = new Date();

	function fun() {
		console.log(time);
		if (false){
			var time = "Hello World!";  //会提前加载,将time赋值
		}
	}

	fun(); //输出undefined
</script>
</html>
```
![](http://i.imgur.com/tJgF4Pn.png)

> 场景二： 用来计数的循环变量泄露为全局变量

``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>块级作用域</title>
</head>
<body>
</body>
<script>
	var string = "Hello World!";
	for (var i = 0; i < string.length; i++){
		console.log(string[i]);
	};
	console.log("循环结束");
	console.log(i); // 输出12
</script>
</html>
```
![](http://i.imgur.com/9CugGml.png)

## 块级作用域
> ES6 解决场景一

``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>块级作用域</title>
</head>
<body>
</body>
<script>
    let time = new Date();

	function fun() {
		console.log(time);
		if (false){
			let time = "Hello World!";  //会提前加载,将time赋值
		}
	}

	fun(); //输出undefined
</script>
</html>
```
# const
> const也用来声明变量，但是声明的是常量。一旦声明，常量的值就不能改变。`const常量只在当前模块有效。`

## const 常量
``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>const</title>
</head>
<body>
</body>
<script>
	const PI = 3.14159;
	console.log(PI);
	console.log(5*PI);
	PI = 5; //错误
</script>
</html>
```
![](http://i.imgur.com/IdJIjjR.png)

## const 对象
``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>const</title>
</head>
<body>
</body>
<script>
    const person = {};
    person.name = "Gavin"; //后面重复赋值
    person.age = 20;  //后面重复赋值
    console.log(person.name); 
    console.log(person.age);
    console.log(person);
</script>
</html>
```
![](http://i.imgur.com/7VZUzIx.png)

## const 冻结对象
``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>const</title>
</head>
<body>
</body>
<script>
	const person = Object.freeze({
		name: "Gavin",
		age : 20
	});

	console.log(person.name);	//Gavin
	console.log(person.age);	//20
	console.log(person);		//Object

	person.name = "Gavin 1";  //不能改变
	console.log(person.name); //Gavin
</script>
</html>
```
![](http://i.imgur.com/Al5QO2L.png)

## const 跨模块常量
> module.js

``` javascript
export const intVariantName = 100;
export const FloatVariantName = 3.14159165;
export const charVariantName = "variantValue";
```
> use.js

``` javascript
import * as variant from './module';
console.log(variant.intVariantName);	//100
console.log(variant.FloatVariantName);	//3.14159165
console.log(variant.charVariantName);	//variantValue
```
> otherUse.js

``` javascript
import { FloatVariantName, charVariantName } as variant from './module';
	console.log(variant.FloatVariantName);	//3.14159165
	console.log(variant.charVariantName);	//variantValue
```
> OnlyInt.js

``` javascript
import intVariantName as variant from './module';
console.log(variant.intVariantName);	//100
```
# 全局变量属性
> 全局对象是最顶层的对象，在浏览器环境指的是window对象，在Node.js指的是global对象。在JavaScript语言中，所有全局变量都是全局对象的属性。（Node的情况比较特殊，这一条只对REPL环境适用，模块环境必须显式声明成global的属性。）<br>
> ES6规定，var命令和function命令声明的全局变量，属于全局对象的属性；let命令、const命令、class命令声明的全局变量，不属于全局对象的属性。

``` javascript
var varName = "varValue";
//	浏览器环境下
console.log(window.varName);	//varValue
//	Node.js环境下
console.log(global.varName);	//varValue
//	通用环境
console.log(this.varName);		//varValue


let letName = "letValue";
console.log(window.letName);	//undefined -- use strict
console.log(this.letName);		//undefined -- use strict
```
