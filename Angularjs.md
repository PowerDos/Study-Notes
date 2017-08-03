# Angularjs
### 目录
1. [Angularjs](#angularjs)
	- [简介](#简介)
2. [小实例](#小实例)
	- [simple demo](#simple-demo)
	- [MVC demo](#mvc-demo)
3. [表达式](#表达式)
	- [减乘除余等](#减乘除余等)
	- [加法和字符串连接](#加法和字符串连接)
	- [对象](#对象)
	- [数组](#数组)
4. [指令](#指令)
	- [ng-app](#ng-app)
	- [ng-init](#ng-init)
	- [ng-model](#ng-model)
	- [ng-repeat](#ng-repeat)
5. [模型](#模型)
	- [双向绑定](#双向绑定)
	- [验证用户输入](#验证用户输入)
	- [应用状态](#应用状态)
6. [Scope(作用域)](#scope作用域)
7. [Controller(控制器)](#controller控制器)
8. [过滤器](#过滤器)
	- [currency](#currency)
	- [lowercase](#lowercase)
	- [uppercase](#uppercase)
	- [filter](#filter)
	- [orderBy](#orderby)
9. [Service服务](#service服务)
	- [$location](#location)
	- [$http](#http)
	- [$timeout](#timeout)
	- [$interval](#interval)
	
## 简介
> AngularJS 是建立在轻量 jQuery 之上的一个结构化前端 MVVM 框架 , 它可通过`<script>`标签添加到 HTML 页面,通过 指令 扩展了 HTML，且通过 表达式 绑定数据到 HTML。相比较 Facebook 的 React，个人觉得 AngularJS 可能更适合企业用户，创建单页面的 CRUD 应用。例如对表格表单的处理，AngularJS 就能展现其强大快捷的一面。另外，AngularJS 非常结构化，大而全，坏处就是规定比较严格，好处是代码更一致，而且有一套很完善的测试流程支持。但是性能经常受人诟病。企业用户可能对性能没有那么敏感，反而喜欢这种写起来条理清晰，功能强大的框架。这有点像 Java，虽然臃肿，慢，但是成熟稳定，所以企业往往选择这样的框架

# 小实例
> Bootstrap + Angularjs

## simple demo
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>简单小实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="">
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例</h1>
		<form action="">
			<div class="form-group">
				<label for="">实时输入显示：</label>
				<input type="text" class="form-control" ng-model='msg'>
			</div>
		</form>
		<!-- 写法一 -->
		<!-- <div class="well"> Gavin: {{ msg }} </div> -->
		<!-- 写法二 -->
		<div class="well">Gavin: <span ng-bind="msg"></span></div>
	</div>
</body>
</html>
```
![](http://i.imgur.com/p6XNwni.png)

## MVC demo
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>简单小实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例</h1>
		<form action="">
			<div class="form-group">
				<label for="">实时输入显示：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='msg'>
			</div>
		</form>
		<!-- view -->
		<!-- 写法一 -->
		<!-- <div class="well"> Gavin: {{ msg }} </div> -->
		<!-- 写法二 -->
		<div class="well">Gavin: <span ng-bind="msg"></span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 控制器代码逻辑范围
		// 赋初值，因为Angular的双向绑定，所以其他地方也会同步显示
		$scope.msg = "Study Note"; 
	})
</script>
</html>
```
![](http://i.imgur.com/Fut3UJk.png)

# 表达式
## 减乘除余等
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="">
			<div class="form-group">
				<label for="">第一个数：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='num_1'>
				<label for="">第二个数：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='num_2'>
			</div>
		</form>
		<!-- view -->
		<!-- 写法一 -->
	<!--<div class="well">减: <span ng-bind="num_1 - num_2"></span></div>
		<div class="well">乘: <span ng-bind="num_1 * num_2"></span></div>
		<div class="well">除: <span ng-bind="num_1 / num_2"></span></div>
		<div class="well">余: <span ng-bind="num_1 % num_2"></span></div> -->
		<!-- 写法二 -->
		<div class="well">减: {{ num_1 - num_2 }}</span></div>
		<div class="well">乘: {{ num_1 * num_2 }}</span></div>
		<div class="well">除: {{ num_1 / num_2 }}</span></div>
		<div class="well">余: {{ num_1 % num_2 }}</span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {

	})
</script>
</html>
```
![](http://i.imgur.com/oRmxVM1.png)
## 加法和字符串连接
> 因为JavaScript ` + ` 号默认优先是字符串连接，所以单独提取出来做个小实例

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="">
			<div class="form-group">
				<label for="">第一个数：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='num_1'>
				<label for="">第二个数：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='num_2'>
			</div>
		</form>
		<!-- view -->
		<!-- 写法一 -->
	<!--<div class="well">加: <span ng-bind="tot()"></span></div>
		<div class="well">字符串连接: <span ng-bind="num_1 + num_2"></span></div> -->
		<!-- 写法二 -->
		<div class="well">加: {{ tot() }}</span></div>
		<div class="well">字符串连接: {{ num_1 + num_2 }}</span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		$scope.tot = function(){
			var total = parseInt($scope.num_1) + parseInt($scope.num_2);
			return total ? total : 0;
		}
	})
</script>
</html>
```
![](http://i.imgur.com/K8VbKdL.png)

## 对象
>可以用两种方式，一种是ng-init，一种是直接在controller初始化

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<!-- <body ng-app="myapp" ng-controller='myctl' ng-init="person={firstName:'Gavin',lastName:'Lin'}"> -->
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<div class="well">姓名: {{ person.firstName + " " + person.lastName }}</span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 可以用ng-init初始化数据，也可以用下面的直接初始化数据
		$scope.person = {
			firstName: "Gavin",
			lastName: "Lin"
		};
	})
</script>
</html>
```
![](http://i.imgur.com/4VQ4NGj.png)

## 数组
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<!-- <body ng-app="myapp" ng-controller='myctl' ng-init="arr = ['one', 'two', 'three']"> -->
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<div class="well">数组: {{ arr[0] + " " + arr[1] + " " + arr[2] }}</span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 可以用ng-init初始化数据，也可以用下面的直接初始化数据
		$scope.arr = ["one", "two", "three"];
	})
</script>
</html>
```
![](http://i.imgur.com/pbJIGCB.png)

# 指令
### ng-app
> ng-app 指令定义了 AngularJS 应用程序的 根元素。ng-app 指令在网页加载完毕时会自动引导（自动初始化）应用程序。

### ng-init
> ng-init 指令为 AngularJS 应用程序定义了 初始值。通常情况下，不使用 ng-init。您将使用一个控制器或模块来代替它。

### ng-model 
> ng-model 指令 绑定 HTML 元素 到应用程序数据。<br>
ng-model 指令也可以：
- 为应用程序数据提供类型验证（number、email、required）。
- 为应用程序数据提供状态（invalid、dirty、touched、error）。
- 为 HTML 元素提供 CSS 类。
- 绑定 HTML 元素到 HTML 表单。

### ng-repeat
> ng-repeat 指令对于集合中（数组中）的每个项会 克隆一次 HTML 元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
	<style>
		th{
			text-align: center;
		}
	</style>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<table class="table table-bordered table-hover">
			<tr>
				<th>序号</th>
				<th>账号</th>
				<th>用户名</th>
				<th>密码</th>
				<th>操作</th>
			</tr>
			<tr ng-repeat="user in users">
				<th>{{ $index }}</th>
				<th>{{ user.userid }}</th>
				<th>{{ user.username }}</th>
				<th>{{ user.password }}</th>
				<th><a href="">删除</a></th>
			</tr>
		</table>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		$scope.users = [
			{'userid': "1001", "username": "Gavin1", "password": "123"},
			{'userid': "1002", "username": "Gavin2", "password": "123"},
			{'userid': "1003", "username": "Gavin3", "password": "123"},
			{'userid': "1004", "username": "Gavin4", "password": "123"},
			{'userid': "1005", "username": "Gavin5", "password": "123"},
			{'userid': "1006", "username": "Gavin6", "password": "123"},
			{'userid': "1007", "username": "Gavin7", "password": "123"},
			{'userid': "1008", "username": "Gavin8", "password": "123"},
			{'userid': "1009", "username": "Gavin9", "password": "123"},
			{'userid': "1010", "username": "Gavin10", "password": "123"}
		];
	})
</script>
</html>
```
![](http://i.imgur.com/8lovPBt.png)
# 模型
> ng-model 指令可以将输入域的值与 AngularJS 创建的变量绑定。

## 双向绑定
> 双向绑定，在修改输入域的值时， AngularJS 属性的值也将修改,上面的例子也提及到，这里就不再重复

## 验证用户输入
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form ng-app="" name="myForm" action="">
			<div class="form-group">
				<label for="">Email:</label>
				<input type="email" name="myAddress" class="form-control" ng-model="mail">
				<label class="label label-danger" ng-show="myForm.myAddress.$error.email">不是一个合法的邮箱地址</label>
			</div>
		</form>
	</div>
</body>
</html>
```
![](http://i.imgur.com/8CUM3GC.png)
![](http://i.imgur.com/MhHOLuE.png)
## 应用状态
> ng-model 指令可以为应用数据提供状态值(invalid, dirty, touched, error):

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body>
	<div class="container" >
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="" ng-app="" name="myForm">
			<div class="form-group">
				<label for="">Email:</label>
				<input type="email" name="myAddress" class="form-control" ng-model="mail">
				<label class="label label-danger" ng-show="myForm.myAddress.$error.email">不是一个合法的邮箱地址</label>
			</div>
			<div class="well">Valid: {{myForm.myAddress.$valid}} (如果输入的值是合法的则为 true)</div>
			<div class="well">Dirty: {{myForm.myAddress.$dirty}} (如果值改变则为 true)</div>
			<div class="well">Touched: {{myForm.myAddress.$touched}} (如果通过触屏点击则为 true)</div>
		</form>
	</div>
</body>
</html>
```
![](http://i.imgur.com/dbpLOlg.png)

### ng-model 指令根据表单域的状态添加/移除以下类：
- ng-empty
- ng-not-empty
- ng-touched:布尔值属性，表示用户是否和控件进行过交互
- ng-untouched
- ng-valid:布尔型属性，它指示表单是否通过验证。如果表单当前通过验证，他将为true
- ng-invalid:未通过验证的表单
- ng-dirty:布尔值属性，表示用户是否修改了表单。如果为 ture，表示有修改过；false 表示修没有修改过
- ng-pending
- ng-pristine:布尔值属性，表示用户是否修改了表单。如果为ture，表示没有修改过；false表示修改过

# Scope(作用域)
> Scope(作用域) 是应用在 HTML (视图) 和 JavaScript (控制器)之间的纽带。Scope 是一个对象，有可用的方法和属性。Scope 可应用在视图和控制器上。由于上面很多例子都用了scope就不在这单独演示

# Controller(控制器)
> AngularJS 应用程序被控制器控制。ng-controller 指令定义了应用程序控制器。控制器是 JavaScript 对象，由标准的 JavaScript 对象的构造函数 创建。由于上面很多例子都用了ng-controller就不在这单独演示

# 过滤器
## currency
> 格式化数字为货币格式。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="">
			<div class="form-group">
				<label for="">格式化数字为货币格式：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='msg'>
			</div>
		</form>
		<div class="well">货币格式: <span ng-bind="msg|currency"></span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 控制器代码逻辑范围
	})
</script>
</html>
```
![](http://i.imgur.com/1ZonO5W.png)

## lowercase
> 格式化字符串为小写。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="">
			<div class="form-group">
				<label for="">格式化字符串为小写：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='msg'>
			</div>
		</form>
		<div class="well">小写: <span ng-bind="msg|lowercase"></span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 控制器代码逻辑范围
	})
</script>
</html>
```
![](http://i.imgur.com/R4HYt4w.png)

## uppercase
> 格式化字符串为大写。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="">
			<div class="form-group">
				<label for="">格式化字符串为大写：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='msg'>
			</div>
		</form>
		<div class="well">大写: <span ng-bind="msg|uppercase"></span></div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 控制器代码逻辑范围
	})
</script>
</html>
```
![](http://i.imgur.com/iarln7G.png)

## filter
> 从数组项中选择一个子集。

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="">
			<div class="form-group">
				<label for="">查找：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='msg'>
			</div>
		</form>
		<div class="list-group">
			<a href="" class="list-group-item" ng-repeat=" row in rows|filter:msg "> {{ row }}</a>
		</div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 控制器代码逻辑范围
		$scope.rows=["Banana", "Grape", "plum", "watermelon", "orange"];
	})
</script>
</html>
```
![](http://i.imgur.com/w8RxtP9.png)
![](http://i.imgur.com/BFUJ1W3.png)

## orderBy
> 根据某个表达式排列数组

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<form action="">
			<div class="form-group">
				<label for="">查找：</label>
				<!-- Model -->
				<input type="text" class="form-control" ng-model='msg'>
			</div>
		</form>
		<div class="list-group">
			<a href="" class="list-group-item" ng-repeat=" user in rows|filter:msg|orderBy:'age' "> {{ user.name }} 年龄为: {{ user.age }}</a>
		</div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope) {
		// 控制器代码逻辑范围
		$scope.rows=[
			{ name: "Gavin1", age: 28, sex: "male" },
			{ name: "Gavin2", age: 27, sex: "male" },
			{ name: "Gavin3", age: 26, sex: "male" },
			{ name: "Gavin4", age: 25, sex: "male" },
			{ name: "Gavin5", age: 23, sex: "male" },
			{ name: "Gavin6", age: 20, sex: "male" },
			{ name: "Gavin7", age: 30, sex: "male" },
			{ name: "Gavin8", age: 22, sex: "male" }
		];
	})
</script>
</html>
```
![](http://i.imgur.com/rAwciTP.png)
![](http://i.imgur.com/flUQwHS.png)

# Service(服务)
## $location
>  $location 服务，它可以返回当前页面的 URL 地址。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<div class="list-group">
			<a href="" class="list-group-item"> URL: {{ url }}</a>
		</div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope, $location) {
		// 控制器代码逻辑范围
		$scope.url = $location.absUrl();
	})
</script>
</html>
```
![](http://i.imgur.com/ZbcAJ4S.png)

## $http
> $http 是 AngularJS 应用中最常用的服务。 服务向服务器发送请求，应用响应服务器传送过来的数据。

```html
!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<div class="list-group">
			<a href="" class="list-group-item"> GET: {{ getinfo }} </a>
		</div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope, $http) {
		// 控制器代码逻辑范围
		$http.get("/get_demo.php?name=Gavin&age=20").then(function(res) {
			$scope.getinfo = res.data;
		});
	})
</script>
</html>
```
> get_demo.php

```php
<?php 
echo "获取到的Get数据：";
var_dump($_GET);
```
> 注意: 本例子是放在server服务器测试的结果，php的代码在php的目录里

![](http://i.imgur.com/QVRhcp9.png)

## $timeout
> 超时器，对应了 JS window.setTimeout 函数。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<div class="list-group">
			<a href="" class="list-group-item"> Time Out Demo: {{ data }}</a>
		</div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope, $timeout) {
		$scope.data = "loading....";
		// 控制器代码逻辑范围
		$timeout(function () {
			$scope.data = "Time Out!";
		}, 3000);
	})
</script>
</html>
```
![](http://i.imgur.com/Qroymxz.png)

## $interval
> 定时器， $interval 服务对应了 JS window.setInterval 函数。

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Angularjs 学习实例</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/angular.min.js"></script>
</head>
<body ng-app="myapp" ng-controller='myctl'>
	<div class="container">
		<h1 class="page-header">Angularjs 学习实例 <small> Gavin</small></h1>
		<div class="list-group">
			<a href="" class="list-group-item"> Interval Demo: <label class="label label-danger" ng-bind="num"></label></a>
		</div>
	</div>
</body>
<script>
	// controller
	app = angular.module('myapp', []);
	app.controller('myctl', function ($scope, $interval) {
		$scope.num = 0;
		// 控制器代码逻辑范围
		$interval(function () {
			$scope.num = $scope.num + 1;
		}, 100);
	})
</script>
</html>
```
![](http://i.imgur.com/CzMwpon.png)