import router from '@/router'
import {progressClose, progressStart } from '@/hooks/use-permission'
import { useBasicStore } from '@/store/basic'
import { langTitle } from '@/hooks/use-common'

//路由进入前拦截
router.beforeEach(async (to) => {
  progressStart()
  document.title = langTitle(to.meta?.title) // i18 page title
  const basicStore = useBasicStore()
  basicStore.setFilterAsyncRoutes([])
  return true
})
//路由进入后拦截
router.afterEach(() => {
  progressClose()
})
