import axiosReq from '@/utils/axios-req'


// 获取所有的embed模型
export const embeddingModelsReq = () => {
  return axiosReq({
    url: '/api/llm_model/llm_models',
    method: 'get',
    params: {
      category: 'embedding'
    },
    reqLoading: false
  })
}

// 获取所有的LLM模型
export const llmModelsReq = (params) => {
  return axiosReq({
    url: '/api/llm_model/llm_models',
    method: 'get',
    params: {
      category: 'llm',
      ...params
    },
    reqLoading: false
  })
}

// 创建LLM模型
export function createLLMModelReq(data) {
  return axiosReq({
    url: '/api/llm_model/create',
    method: 'post',
    data
  })
}

// 更新LLM模型
export function updateLLMModelReq(data) {
  return axiosReq({
    url: '/api/llm_model/update',
    method: 'post',
    data
  })
}

// 删除LLM模型
export function deleteLLMModelReq(id) {
  return axiosReq({
    url: '/api/llm_model/delete',
    method: 'post',
    data: { id }
  })
}


