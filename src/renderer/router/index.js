import Vue from 'vue'
import Router from 'vue-router'

import MainWindow from '@/components/MainWindow'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main-window',
      component: MainWindow
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
