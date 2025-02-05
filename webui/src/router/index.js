import Layout from '@/layout/index.vue'
import {createRouter, createWebHistory} from 'vue-router'

export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index.vue'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/error-page/404.vue'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/error-page/401.vue'),
    hidden: true
  },
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'Dashboard',
        component: () => import('@/views/dashboard/index.vue'),
        hidden: true
      }
    ]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/chat',
    children: [
      {
        path: '/chat',
        name: 'Chat',
        component: () => import('@/views/chat/index.vue'),
        meta: {
          title: 'menu.chat', 
          elSvgIcon: 'ChatDotSquare', 
          affix: true, 
          tooltip: 'menu.tooltip.chat'
        }
      }
    ]
  },
  {
    path: '/history',
    component: Layout,
    children: [
      {
        path: '',
        name: 'History',
        component: () => import('@/views/history/index.vue'),
        meta: {
          title: 'menu.history', 
          elSvgIcon: 'Clock', 
          tooltip: 'menu.tooltip.history'
        }
      },
      {
        path: ':id',
        name: 'HistoryDetail',
        component: () => import('@/views/history/detail.vue'),
        meta: {
          title: 'menu.history', 
          elSvgIcon: 'Collection', 
          activeMenu: '/history'
        }
      }
    ]
  },
  {
    path: '/knowledge',
    component: Layout,
    children: [
      {
        path: '',
        name: 'Knowledge',
        component: () => import('@/views/knowledge/index.vue'),
        meta: { 
          title: 'menu.knowledge', 
          elSvgIcon: 'Collection', 
          tooltip: 'menu.tooltip.knowledge'
        }
      },
      {
        path: 'detail',
        name: 'KnowledgeDetail',
        component: () => import('@/views/knowledge/detail.vue'),
        meta: { 
          title: 'menu.knowledge', 
          elSvgIcon: 'Collection', 
          activeMenu: '/knowledge'
        },
        hidden: true,
      },
      {
        path: 'detail/import',
        name: 'KnowledgeDetailImport',
        component: () => import('@/views/knowledge/import.vue'),
        meta: { 
          title: 'menu.knowledge', 
          elSvgIcon: 'Collection'
        },
        hidden: true,
      },
    ]
  },
  {
    path: '/database',
    component: Layout,
    children: [
      {
        path: '/database',
        name: 'Database',
        component: () => import('@/views/database/index.vue'),
        meta: {
          title: 'menu.database', 
          elSvgIcon: 'Coin', 
          affix: true, 
          tooltip: 'menu.tooltip.database'
        }
      }
    ]
  },
  {
    path: '/models',
    component: Layout,
    children: [
      {
        path: '',
        name: 'ModelManagement',
        component: () => import('@/views/models/index.vue'),
        meta: { 
          title: 'menu.models', 
          elSvgIcon: 'Connection', 
          tooltip: 'menu.tooltip.models'
        }
      }
    ]
  },
  {path: "/:pathMatch(.*)", redirect: "/404", hidden: true}
]

//角色和code数组动态路由
export const roleCodeRoutes = []
/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  // 404 page must be placed at the end !!!
  {path: "/:pathMatch(.*)", redirect: "/404", hidden: true},
]


const router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({top: 0}),
  routes: constantRoutes
})

export default router
