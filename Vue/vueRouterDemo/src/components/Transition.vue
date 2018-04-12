<template>
  <div>
    <h3>{{ msg }}</h3>
    <p>css过渡类名：组件过渡过程中，会有四个CSS类名进行切换，这四个类名与transition的name属性有关，比如name="fade",会有如下四个CSS类名</p>
    <ul>
      <li>fade-enter:进入过渡的开始状态，元素被插入时生效，只应用一帧后立刻删除</li>
      <li>fade-enter-active:进入过渡的结束状态，元素被插入时就生效，在过渡过程完成后移除。</li>
      <li>fade-leave:离开过渡的开始状态，元素被删除时触发，只应用一帧后立刻删除。</li>
      <li>fade-leave-active:离开过渡的结束状态，元素被删除时生效，离开过渡完成后被删除。</li>
    </ul>
    <p>从上面四个类名可以看出，fade-enter-active和fade-leave-active在整个进入或离开过程中都有效，所以CSS的transition属性在这两个类下进行设置。</p>
    <p><strong>默认的mode模式in-out模式，这并不是我们想要的。下面我们学一下mode模式。</strong></p>
    <p><strong>过渡模式mode：</strong></p>
    <ul>
      <li>in-out:新元素先进入过渡，完成之后当前元素过渡离开。</li>
      <li>out-in:当前元素先进行过渡离开，离开完成后新元素过渡进入。</li>
    </ul>
    <hr>
    <div>
      <router-link to="/transition/tpage1">子页面一</router-link> |
      <router-link to="/transition/tpage2">子页面二</router-link>
    </div>
    <div>
        <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'transition',
  data () {
    return {
      msg: '路由的过渡动画'
    }
  }
}
</script>

<style scoped>
.fade-enter {
  opacity:0;
}
.fade-leave{
  opacity:1;
}
.fade-enter-active{
  transition:opacity .5s;
}
.fade-leave-active{
  opacity:0;
  transition:opacity .5s;
}
</style>
