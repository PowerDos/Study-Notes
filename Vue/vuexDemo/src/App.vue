<template>
  <div id="app">
    <router-link to="/count">计数</router-link> |
    <router-link to="/getStore1">获取Store数据方式一 </router-link> |
    <router-link to="/getStore2">获取Store数据方式二 </router-link> |
    <router-link to="/getStore3">获取Store数据方式三 </router-link> |
    <router-link to="/Mutations">Mutations修改Store </router-link> |
    <router-link to="/Getter">Getter获取过滤过的参数 </router-link> |
    <router-link to="/Action">Action异步执行 </router-link> |
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
