<template>
  <div>
    <h3>{{ msg }}</h3>
    <div>
      <router-link :to="toChildParams">子组件</router-link>
    </div>
    <br>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RouterTransParams',
  data () {
    return {
      msg: '父子组件传值',
      toChildParams: {
        name: 'child', // 路由名字
        params: { // 传给子路由的参数
          username: 'Gavin',
          sex: 'male'
        }
      }
    }
  }
}
</script>
