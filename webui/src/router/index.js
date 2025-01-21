import Layout from '@/layout/index.vue'
import {createRouter, createWebHistory} from 'vue-router'

export const constantRoutes = [
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
        meta: {title: 'Chat', elSvgIcon: 'ChatDotSquare', affix: true, tooltip: "查看最近一次改写"}
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
        meta: {title: 'History', elSvgIcon: 'Clock', tooltip: "查看改写历史"}
      },
      {
        path: ':id',
        name: 'HistoryDetail',
        component: () => import('@/views/history/detail.vue'),
        meta: {title: 'History', elSvgIcon: 'Collection', activeMenu: '/history'}
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
        meta: { title: 'Knowledge', elSvgIcon: 'Collection', tooltip: "查看知识库"}
      },
      {
        path: 'detail',
        name: 'KnowledgeDetail',
        component: () => import('@/views/knowledge/detail.vue'),
        meta: { title: 'Knowledge', elSvgIcon: 'Collection', activeMenu: '/knowledge'},
        hidden: true,
      },
      {
        path: 'detail/import',
        name: 'KnowledgeDetailImport',
        component: () => import('@/views/knowledge/import.vue'),
        meta: { title: 'Knowledge', elSvgIcon: 'Collection'},
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
        //using el svg icon, the elSvgIcon first when at the same time using elSvgIcon and icon
        meta: {title: 'Database', elSvgIcon: 'Coin', affix: true, tooltip: "进行数据库配置"}
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
        meta: { title: '模型管理', elSvgIcon: 'Connection', tooltip: "进行模型配置"}
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
