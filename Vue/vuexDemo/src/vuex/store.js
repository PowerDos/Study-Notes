import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count: 1
  },
  getters: {
    getCount (state) {
      return state.count + 1
    }
  },
  mutations: {
    add (state, num) {
      const n = num || 1
      state.count += n
    },
    reduce (state) {
      state.count--
    }
  },
  actions: {
    addAction (context) {
      context.commit('add', 8)
      setTimeout(() => { context.commit('reduce') }, 3000)
      console.log('异步执行')
    }
  }
})
