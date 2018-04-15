import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Count from '@/components/Count'
import GetStore1 from '@/components/GetStore1'
import GetStore2 from '@/components/GetStore2'
import GetStore3 from '@/components/GetStore3'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/count',
      name: 'Count',
      component: Count
    },
    {
      path: '/getStore1',
      name: 'getStore1',
      component: GetStore1
    },
    {
      path: '/getStore2',
      name: 'getStore2',
      component: GetStore2
    },
    {
      path: '/getStore3',
      name: 'getStore3',
      component: GetStore3
    }
  ]
})
