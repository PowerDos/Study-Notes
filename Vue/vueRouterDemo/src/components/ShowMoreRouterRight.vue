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
      msg: '右侧显示区'
    }
  }
}
</script>

<style scoped>
h3 {
  color: #fff;
}
</style>
