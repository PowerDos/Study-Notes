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