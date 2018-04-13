<template>
  <div>
    <h3>{{ msg }}</h3>
    <ul>
      <li>beforeRouteEnter：在路由进入前的钩子函数。</li>
      <li>beforeRouteLeave：在路由离开前的钩子函数。</li>
      <li>参数</li>
      <ol>
        <li>to:路由将要跳转的路径信息，信息是包含在对像里边的。</li>
        <li>from:路径跳转前的路径信息，也是一个对象的形式。</li>
        <li>next:路由的控制参数，常用的有next(true)和next(false)。</li>
      </ol>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'RouterHook',
  data () {
    return {
      msg: '钩子函数'
    }
  },
  beforeRouteEnter: (to, from, next) => {
    console.log('在模板配置中，进入路由之前')
    console.log(to)
    console.log(from)
    next()
  },
  beforeRouteLeave: (to, from, next) => {
    console.log('在模板配置中，离开路由之前')
    console.log(to)
    console.log(from)
    next()
  }
}
</script>
