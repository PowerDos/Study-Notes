<template>
  <div>
    <h3> {{ msg }} </h3>
    <p><strong>redirect和alias的区别</strong></p>
    <p><strong>redirect</strong>：仔细观察URL，redirect是直接改变了url的值，把url变成了真实的path路径。</p>
    <p><strong>alias</strong>：URL路径没有别改变，这种情况更友好，让用户知道自己访问的路径，只是改变了router-view中的内容。</p>
    <p><strong>别名请不要用在path为'/'中，如下代码的别名是不起作用的</strong></p>
  </div>
</template>

<script>
export default {
  name: 'alias',
  data () {
    return {
      msg: 'alias别名的使用'
    }
  }
}
</script>
