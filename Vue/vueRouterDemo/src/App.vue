<template>
  <div id="app">
    <div>
      <router-link to="/">HelloWorld</router-link> |
      <router-link to="/home">Home</router-link> |
      <router-link to="/father">子路由实例</router-link> |
      <router-link to="/transFather">父子组件传值</router-link> |
      <router-link to="/showMoreRouterView">多个RouterView</router-link>
      <br>
      <router-link to="/urlParams/60/Gavin">vue-router 利用url传递参数</router-link> |
      <router-link to="/RedirectTarget">redirect基本重定向</router-link> |
      <router-link to="/Gavin">alias别名的使用</router-link> |
      <router-link to="/transition">路由的过渡动画</router-link> |
      <router-link to="/unkownpath">404页面</router-link> |
      <router-link to="/routerHook">路由钩子</router-link>
    </div>
    <br>
    <hr>
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.fade-enter {
  opacity:0;
}
.fade-leave{
  opacity:.3;
}
.fade-enter-active{
  transition:opacity .2s;
}
.fade-leave-active{
  opacity:0;
  transition:opacity .2s;
}
</style>
