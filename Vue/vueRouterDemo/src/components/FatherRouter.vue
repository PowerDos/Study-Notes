<template>
  <div>
    <h3>{{msg}}</h3>
    <div>
      <router-link to="/father/page1">子页面一</router-link> |
      <router-link to="/father/page2">子页面二</router-link>
    </div>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'father-router',
  data () {
    return {
      msg: '子路由实例'
    }
  }
}
</script>

<style scoped>
h3 {
  color: #42b983;
}
</style>
