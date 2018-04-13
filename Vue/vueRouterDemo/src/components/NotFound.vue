<template>
  <div>
    <h3>{{ msg }}</h3>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  data () {
    return {
      msg: '404 此页面不存在'
    }
  }
}
</script>

<style scoped>
h3 {
  color: #42b983;
}
</style>
