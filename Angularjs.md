# Angularjs
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