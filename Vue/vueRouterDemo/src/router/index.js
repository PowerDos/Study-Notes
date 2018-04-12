import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import FatherRouter from '@/components/FatherRouter'
import Page1 from '@/components/Page1'
import Page2 from '@/components/Page2'
import RouterTransParams from '@/components/RouterTransParams'
import RouterTransParamsChild from '@/components/RouterTransParamsChild'
import ShowMoreRouters from '@/components/ShowMoreRouters'
import ShowMoreRouterLeft from '@/components/ShowMoreRouterLeft'
import ShowMoreRouterRight from '@/components/ShowMoreRouterRight'
import UrlParams from '@/components/UrlParams'
import RedirectTarget from '@/components/RedirectTarget'
import alias from '@/components/alias'
import Transition from '@/components/Transition'

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
    },
    {
      path: '/transFather',
      component: RouterTransParams,
      children: [
        {
          path: 'child',
          name: 'child',
          component: RouterTransParamsChild
        }
      ]
    },
    {
      path: '/showMoreRouterView',
      component: ShowMoreRouters,
      children: [
        {
          path: '/',
          name: 'showMoreRouterView',
          components: {
            default: ShowMoreRouters,
            left: ShowMoreRouterLeft,
            right: ShowMoreRouterRight
          }
        }
      ]
    },
    {
      path: '/urlParams/:id/:username',
      name: 'UrlParams',
      component: UrlParams
    },
    {
      path: '/redirect',
      name: 'RedirectDemo',
      redirect: '/RedirectTarget'
    },
    {
      path: '/RedirectTarget',
      name: 'RedirectTarget',
      component: RedirectTarget
    },
    {
      path: '/alias',
      name: 'alias',
      component: alias,
      alias: '/Gavin'
    },
    {
      path: '/transition',
      component: Transition,
      children: [
        {
          path: 'tpage1',
          name: 'tpage1',
          component: Page1
        },
        {
          path: 'tpage2',
          name: 'tpage2',
          component: Page2
        }
      ]
    }
  ]
})
