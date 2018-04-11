<template>
  <div id="app">
    <div>
      <router-link to="/">HelloWorld</router-link> |
      <router-link to="/home">Home</router-link> |
      <router-link to="/father">子路由实例</router-link> |
      <router-link to="/transFather">父子组件传值</router-link> |
      <router-link to="/showMoreRouterView">多个RouterView</router-link>
    </div>
    <router-view/>
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
</style>
