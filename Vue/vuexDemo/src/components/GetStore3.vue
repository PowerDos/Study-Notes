<template>
  <div>
    <h3>{{ msg }}</h3>
    <hr>
    <h3>{{ count }}</h3>
    <button @click="$store.commit('add')">+</button>
    <button @click="$store.commit('reduce')">-</button>
  </div>
</template>

<script>
import store from '@/vuex/store'
import { mapState } from 'vuex'
export default {
  name: 'Count',
  data () {
    return {
      msg: 'Vuex 获取store中的值 三'
    }
  },
  computed: mapState(['count']),
  store
}
</script>
