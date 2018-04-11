<template>
  <div>
    <h3>{{ msg }}</h3>
  </div>
</template>

<script>
export default {
  name: 'ShowMoreRouterLeft',
  data () {
    return {
      msg: '左侧显示区'
    }
  }
}
</script>

<style scoped>
h3 {
  color: #2c2c2c;
}
</style>
