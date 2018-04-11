<template>
  <div>
    <div>{{msg}}</div>
    <h3>子路由接收到的参数为： {{ $route.params.username }} - {{ $route.params.sex }}</h3>
  </div>
</template>

<script>
export default {
  name: 'RouterTransParamsChild',
  data () {
    return {
      msg: '我是子路由页面'
    }
  }
}
</script>

<style scoped>
h3 {
  color: #42b983;
}
</style>
