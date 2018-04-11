<template>
  <div>
    <h3>{{ msg }}</h3>
  </div>
</template>

<script>
export default {
  name: 'RedirectTarget',
  data () {
    return {
      msg: '我是重定向后的页面'
    }
  }
}
</script>
