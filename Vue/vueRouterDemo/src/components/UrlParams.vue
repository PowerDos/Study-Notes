<template>
  <div>
    <h3>{{ msg }}</h3>
    <div>
      <p>URL传入的参数</p>
      <p>id: {{ $route.params.id }}</p>
      <p>username: {{ $route.params.username }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UrlParams',
  data () {
    return {
      msg: 'vue-router 利用url传递参数'
    }
  }
}
</script>
