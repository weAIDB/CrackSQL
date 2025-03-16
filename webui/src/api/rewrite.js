import axiosReq from '@/utils/axios-req'

// 获取改写列表
export const rewriteListReq = (pageSize = 20, page = 0, keyword = '') => {
  return axiosReq({
    url: 'api/rewrite/list',
    data: {
      page_size: pageSize,
      page,
      keyword
    },
    method: 'post'
  })
}

// 获取改写详情
export const rewriteDetailReq = (id) => {
  return axiosReq({
    url: `api/rewrite/detail`,
    data: { id },
    method: 'post'
  })
}

// 获取最近一次改写
export const rewriteLatestReq = () => {
  return axiosReq({
    url: 'api/rewrite/latest',
    method: 'get'
  })
}

// 创建改写历史
export const createRewriteReq = (data) => {
  return axiosReq({
    url: 'api/rewrite/create',
    method: 'post',
    data
  })
}

// 停止改写任务
export const stopRewriteReq = (data) => {
  return axiosReq({
    url: 'api/rewrite/stop',
    method: 'post',
    data
  })
}

// 删除改写历史
export const deleteRewriteReq = (id) => {
  return axiosReq({
    url: 'api/rewrite/delete',
    method: 'post',
    data: { id }
  })
}
