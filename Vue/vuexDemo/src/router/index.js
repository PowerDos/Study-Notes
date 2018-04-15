import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Count from '@/components/Count'
import GetStore1 from '@/components/GetStore1'
import GetStore2 from '@/components/GetStore2'
import GetStore3 from '@/components/GetStore3'
import Mutations from '@/components/Mutations'
import Getter from '@/components/Getter'
import Action from '@/components/Action'

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
    },
    {
      path: '/Mutations',
      name: 'Mutations',
      component: Mutations
    },
    {
      path: '/Getter',
      name: 'Getter',
      component: Getter
    },
    {
      path: '/Action',
      name: 'Action',
      component: Action
    }
  ]
})
