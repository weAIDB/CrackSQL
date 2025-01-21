import axiosReq from '@/utils/axios-req'

// 获取数据库配置列表
export const databaseListReq = (pageSize = 10, page = 0, keyword = '') => {
  return axiosReq({
    url: 'api/database_config/list',
    data: {
      page_size: pageSize,
      page,
      keyword
    },
    method: 'post'
  })
}

// 获取数据库类型列表
export const databaseTypesReq = () => {
  return axiosReq({
    url: 'api/database_config/types',
    method: 'get'
  })
}

// 创建数据库配置
export const createDatabaseReq = (config) => {
  return axiosReq({
    url: 'api/database_config/create',
    data: config,
    method: 'post'
  })
}

// 更新数据库配置
export const updateDatabaseReq = (config) => {
  return axiosReq({
    url: 'api/database_config/update',
    data: config,
    method: 'post'
  })
}

// 删除数据库配置
export const deleteDatabaseReq = (id) => {
  return axiosReq({
    url: 'api/database_config/delete',
    data: { id },
    method: 'post'
  })
}
