<template>
  <div>
    <h3>{{msg}}</h3>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'I am Home'
    }
  }
}
</script>

<style scoped>
h3 {
  color: #42b983;
}
</style>
