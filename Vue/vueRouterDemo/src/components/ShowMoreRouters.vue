<template>
  <div>
    <h3>{{ msg }}</h3>
    <div class="container">
      <router-view></router-view>
      <router-view name="left" class="left"></router-view>
      <router-view name="right" class="right"></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShowMoreRouter',
  data () {
    return {
      msg: '多个路由显示区域'
    }
  }
}
</script>

<style scoped>
.container {
  width: 60%;
  margin: 0px auto;
}
.left{
  width: 50%;
  float: left;
  background-color: #ccc;
}
.right{
  width: 50%;
  float: left;
  background-color: #222;
}
</style>

