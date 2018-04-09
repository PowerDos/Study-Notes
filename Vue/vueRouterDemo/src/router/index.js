import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import FatherRouter from '@/components/FatherRouter'
import Page1 from '@/components/Page1'
import Page2 from '@/components/Page2'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/father',
      name: 'father',
      component: FatherRouter,
      children: [
        {
          path: '/',
          name: 'index',
          component: Page1
        },
        {
          path: 'page1',
          name: 'page1',
          component: Page1
        },
        {
          path: 'page2',
          name: 'page2',
          component: Page2
        }
      ]
    }
  ]
})
