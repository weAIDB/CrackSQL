import axiosReq from '@/utils/axios-req'

//获取知识库列表
export const knowledgeListReq = () => {
    return axiosReq({
        url: '/api/knowledge_base/list',
        params: {},
        method: 'get'
    })
}

// 搜索知识库内的文件
export const knowledgeSearchDocsReq = (kbName, query) => {
    return axiosReq({
        url: '/api/knowledge_base/search',
        data: { kb_name: kbName, query, top_k: 10 },
        method: 'post',
        reqLoading: false
    })
}


// 获取知识库详情
export const knowledgeBaseDetailReq = (knowledgeBaseName) => {
    return axiosReq({
        url: '/api/knowledge_base/detail',
        params: {kb_name: knowledgeBaseName},
        method: 'get'
    })
}

// 更新知识库
export const knowledgeBaseUpdateInfoReq = (knowledgeBaseName, info) => {
    return axiosReq({
        url: '/api/knowledge_base/update',
        data: {kb_name: knowledgeBaseName, kb_info: info},
        method: 'post'
    })
}

// 删除知识库
export const knowledgeBaseDeleteReq = (kbName) => {
    return axiosReq({
        url: '/api/knowledge_base/delete',
        data: { kb_name: kbName },
        method: 'post'
    })
}

// 创建知识库
export const createKnowledgeBaseReq = (knowledgeBaseName, info, embeddingModelName, dbType) => {
    return axiosReq({
        url: '/api/knowledge_base/create',
        data: {kb_name: knowledgeBaseName, kb_info: info, embedding_model_name: embeddingModelName, db_type: dbType},
        method: 'post',
        reqLoading: false
    })
}

export const getKnowledgeBaseItemsReq = (kbName, page, pageSize) => {
    return axiosReq({
        url: '/api/knowledge_base/items',
        params: {kb_name: kbName, page, page_size: pageSize},
        method: 'get'
    })
}

export const addKnowledgeBaseItemsReq = (kbName, items) => {
    return axiosReq({
        url: '/api/knowledge_base/add_items',
        data: {kb_name: kbName, items},
        method: 'post'
    })
}

export const deleteKnowledgeBaseItemsReq = (kbName, itemIds) => {
    return axiosReq({
        url: '/api/knowledge_base/delete_items',
        data: {kb_name: kbName, item_ids: itemIds},
        method: 'post'
    })
}
