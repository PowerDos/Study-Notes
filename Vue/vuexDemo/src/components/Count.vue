<template>
  <div>
    <h3>{{ msg }}</h3>
    <hr>
    <h3>{{ $store.state.count }}</h3>
    <button @click="$store.commit('add')">+</button>
    <button @click="$store.commit('reduce')">-</button>
  </div>
</template>

<script>
import store from '@/vuex/store'
export default {
  name: 'Count',
  data () {
    return {
      msg: 'Vuex 计数器'
    }
  },
  store
}
</script>
