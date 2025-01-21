<template>
  <div class="detail-container">
    <div class="rowBC header">
      <div class="rowBC" style="max-width: 50%; flex-shrink: 0; min-width: 200px">
        <el-button icon="ArrowLeftBold" type="primary" plain circle size="large" @click="routerBack()"/>
        <div class="columnSS" style="margin-left: 10px; width: 100%">
          <span style="font-weight: bold; font-size: 22px; margin-bottom: 5px">{{ $route.query.kb_name }}</span>
          <span style="font-size: 12px; color: #666666">Data Count: {{ totalCount }}</span>
        </div>
      </div>
      <div class="rowEC" style="width: 100%; flex-shrink: 1;">
        <div v-if="activeIndex === 'dataset'" class="upload-container" @click="onOpenUpdateDialog">
          <span>添加新文件</span>
        </div>
        <div v-else-if="activeIndex === 'search'" class="rowBC" style="width: 100%">
          <el-input
              v-model="searchValue" placeholder="请输入搜索内容" size="large"
              style="width: 100%; margin: 0 20px" />
          <el-button size="default" :loading="searching" type="primary" @click="onSearchClick">
            搜索
          </el-button>
        </div>

      </div>
    </div>
    <el-container style="height: calc(100% - 100px)">
      <el-aside width="200px" style="border-right: 1px solid var(--border-color); height: 100%;">
        <div class="columnSS" style="width: 100%; padding: 10px;">
          <div class="columnSS" style="width: 100%; margin-top: 20px">
            <div :class="`rowSC menu-item ${activeIndex === 'dataset' ? ' active' : ''}`"
                 @click="onMenuClick('dataset')">
              <el-icon>
                <Document/>
              </el-icon>
              <span>数据集</span>
            </div>
            <div :class="`rowSC menu-item ${activeIndex === 'search' ? ' active' : ''}`" @click="onMenuClick('search')">
              <el-icon>
                <Search/>
              </el-icon>
              <span>搜索测试</span>
            </div>
            <div :class="`rowSC menu-item ${activeIndex === 'setting' ? ' active' : ''}`"
                 @click="onMenuClick('setting')">
              <el-icon>
                <Setting/>
              </el-icon>
              <span>配置</span>
            </div>
          </div>
        </div>
      </el-aside>
      <el-main style="overflow-y: hidden; width: 100%">
        <div v-if="activeIndex === 'dataset'" class="columnAE">
          <div class="file-list-container">
            <div class="cards-container">
              <el-card 
                v-for="(item, index) in itemList" 
                :key="index" 
                class="item-card"
                shadow="hover"
              >
                <div class="card-content">
                  <div class="card-header">
                    <span class="operator">{{ item.content?.Operator }}</span>
                    <div class="status-actions">
                      <el-tag 
                        :type="getStatusType(item.status)" 
                        size="small" 
                        class="status-tag"
                      >
                        {{ getStatusText(item.status) }}
                      </el-tag>
                      <div class="actions" v-if="item.status === 'completed'">
                        <el-button type="primary" link @click="handleEdit(index)">
                          编辑
                        </el-button>
                        <el-button type="danger" link @click="handleDeleteItem(index)">
                          删除
                        </el-button>
                      </div>
                    </div>
                  </div>

                  <!-- 错误信息展示 -->
                  <div v-if="item.error_msg" class="error-message">
                    <el-alert
                      :title="'处理失败：' + item.error_msg"
                      type="error"
                      :closable="false"
                      show-icon
                    >
                      <template #default>
                        <el-button 
                          type="primary" 
                          size="small" 
                          @click="handleRetry(item)"
                          class="retry-button"
                        >
                          重新处理
                        </el-button>
                      </template>
                    </el-alert>
                  </div>

                  <div class="card-info">
                    <el-tag size="small" type="info" class="time-tag">
                      {{ formatTime(item.created_at) }}
                    </el-tag>
                  </div>

                  <div class="card-body">
                    <div class="info-item">
                      <div class="label">描述：</div>
                      <div class="description">{{ item.content?.Description }}</div>
                    </div>
                    <div class="info-item">
                      <div class="label">语法树：</div>
                      <div class="tree">{{ item.content?.Tree }}</div>
                    </div>
                    <div class="info-item">
                      <div class="label">详细信息：</div>
                      <div class="detail">{{ item.content?.Detail }}</div>
                    </div>
                  </div>
                </div>
              </el-card>
            </div>

            <!-- 编辑对话框 -->
            <el-dialog
              v-model="editDialogVisible"
              title="编辑数据"
              width="80%"
              :close-on-click-modal="false"
            >
              <el-form v-if="currentEditItem" label-width="100px" class="edit-form">
                <el-form-item label="操作符">
                  <el-input v-model="currentEditItem.Operator" />
                </el-form-item>
                <el-form-item label="描述">
                  <el-input
                    v-model="currentEditItem.Description"
                    type="textarea"
                    :rows="3"
                  />
                </el-form-item>
                <el-form-item label="链接">
                  <el-input v-model="currentEditItem.Link" />
                </el-form-item>
                <el-form-item label="语法树">
                  <el-input
                    v-model="currentEditItem.Tree"
                    type="textarea"
                    :rows="3"
                  />
                </el-form-item>
                <el-form-item label="详细信息">
                  <el-input
                    v-model="currentEditItem.Detail"
                    type="textarea"
                    :rows="5"
                  />
                </el-form-item>
              </el-form>
              <template #footer>
                <div class="dialog-footer">
                  <el-button @click="editDialogVisible = false">取消</el-button>
                  <el-button type="primary" @click="handleSaveEdit">
                    确认
                  </el-button>
                </div>
              </template>
            </el-dialog>
          </div>
        </div>
        <div v-if="activeIndex === 'search'">
          <el-table :data="searchResult" :loading="searching" style="width: 100%; border-radius: 10px;" height="calc(100vh - 140px)">
            <el-table-column label="搜索结果展示（近似值评分为百分制，分数越高，相关性越高，100最高。）">
              <template #default="scope">
                <div class="search-result-item">
                  <div class="document-info rowSC">
                    <el-tag size="small" style="margin-right: 10px">
                      <span style="font-weight: bold; font-size: 16px">结果 {{ scope.$index + 1 }}</span>
                      #
                      <span style="font-weight: bold; font-size: 16px">评分：{{ scope.row.score }}</span>
                    </el-tag>
                    <span class="document-title">{{ scope.row.document?.title }}</span>
                  </div>
                  <div class="content">{{ scope.row.content }}</div>
                  <div v-if="scope.row.meta_info" class="meta-info">
                    <el-descriptions :column="2" size="small" border>
                      <el-descriptions-item v-for="(value, key) in scope.row.meta_info" :key="key" :label="key">
                        {{ value }}
                      </el-descriptions-item>
                      <el-descriptions-item label="文档格式">
                        {{ scope.row.document?.type }}
                      </el-descriptions-item>
                      <el-descriptions-item label="文本分割序号">
                        {{ scope.row.chunk_index + 1 }}
                      </el-descriptions-item>
                    </el-descriptions>
                  </div>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div v-if="activeIndex === 'setting'" style="width: 100%; height: 100%; background: white; padding: 20px; border-radius: 10px;">
          <div class="relative columnSS" style="width: 100%">
            <div class="rowSC" style="width: 100%;">
              <span style="color: #000000; width: 120px; text-align: left; font-size: 16px; flex-shrink: 0">名称</span>
              <span style="color: #333333;">{{ editForm.kb_name }}</span>
            </div>

            <div class="rowSC" style="width: 100%; margin-top: 20px;">
              <span style="color: #000000; width: 120px; text-align: left; font-size: 16px; flex-shrink: 0">介绍</span>
              <el-input v-model="editForm.kb_info" disabled :rows="2" type="textarea"/>
            </div>

            <div class="rowSC" style="width: 100%; margin-top: 20px;">
              <span style="color: #000000; width: 120px; text-align: left; font-size: 16px; flex-shrink: 0">向量模型</span>
              <span style="color: #333333;">{{ editForm.embedding_model_name }}</span>
            </div>

            <!-- 添加数据库类型显示 -->
            <div class="rowSC" style="width: 100%; margin-top: 20px;">
              <span style="color: #000000; width: 120px; text-align: left; font-size: 16px; flex-shrink: 0">数据库类型</span>
              <span style="color: #333333;">{{ editForm.db_type }}</span>
            </div>

            <div class="rowSC" style="margin-top: 20px">
              <!--              <el-button size="default" type="primary" @click="onHandleSaveClick">Save</el-button>-->
              <el-button :icon="Delete" size="small" @click="onHandleDeleteClick"> 删除</el-button>
            </div>
          </div>
        </div>
      </el-main>
    </el-container>
    <el-dialog
        v-model="chunksDialogVisible"
        :title="chunksDialogTitle"
        width="80%"
        top="3vh"
        style="height: 92vh"
        :destroy-on-close="true">
      <el-collapse v-if="currentChunks" v-loading="chunksLoading" style="height: calc(92vh - 80px); overflow-y: scroll">
        <el-collapse-item v-for="(chunk, index) in currentChunks" :key="index" title="">
          <template #title>
            <el-tag size="small" style="margin-right: 10px">分块: {{ chunk.content_info.content_index + 1 }}</el-tag>
            <span
                style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100%;">
              {{ chunk.chunk_content }}
            </span>
          </template>
          <div class="chunk-content">
            <p>{{ chunk.content_info.content }}</p>
          </div>
        </el-collapse-item>
      </el-collapse>
    </el-dialog>
  </div>
</template>

<script setup lang="ts" name="KnowledgeDetail">
import {knowledgeBaseDeleteReq, knowledgeBaseDetailReq, knowledgeBaseUpdateInfoReq, knowledgeSearchDocsReq, getKnowledgeBaseItemsReq, addKnowledgeBaseItemsReq, deleteKnowledgeBaseItemsReq} from "@/api/knowledge";
import {useBasicStore} from "@/store/basic";
import {Delete, Document, Search, Setting} from "@element-plus/icons-vue";
import {ElMessage, ElMessageBox} from 'element-plus'
import type {Ref} from 'vue'
import {onMounted, reactive, ref, watch} from 'vue'
import {useRoute, useRouter} from 'vue-router'

const basicStore = useBasicStore()
const router = useRouter()
const route = useRoute()
const activeIndex = ref('dataset')
const itemList: Ref<Array<any>> = ref([])
const currentPage = ref(1)
const pageSize = ref(20)
const totalCount = ref(0)
const loading = ref(false)
const showDetailIndex = ref(-1)
const reviewDrawer: Ref<boolean> = ref(false)
const reviewDrawerLoading: Ref<boolean> = ref(true)
const reviewDrawerTitle: Ref<string> = ref('')
const searchValue = ref('')
const searchResult = ref([])
const searching = ref(false)
const pollingTimer = ref<NodeJS.Timer | null>(null)
const expandLoading = ref<boolean>(false)

const editForm = reactive({
  kb_name: '',
  kb_info: '',
  embedding_model_name: '',
  db_type: ''
})

const chunksDialogVisible = ref(false)
const chunksDialogTitle = ref("文档分块详情")
const chunksLoading = ref(false)
const currentChunks = ref(null)

// 添加编辑相关的响应式变量
const editDialogVisible = ref(false)
const currentEditItem = ref<JsonItem | null>(null)
const currentEditIndex = ref(-1)

watch(() => activeIndex.value,
    (newValue, oldValue) => {
      console.log('activeIndex', newValue, oldValue)
      if (newValue === 'setting') {
        getKnowledgeBaseDetail()
      }
    },
    {immediate: true}
)

onMounted(async () => {
  activeIndex.value = (route.query.activeIndex as string) || 'dataset'
  getItems()
})

onUnmounted(() => {
  stopPolling()
})

const handleSizeChange = (val: number) => {
  getItems()
}
const handleCurrentChange = (val: number) => {
  getItems()
}

const getItems = () => {
  getKnowledgeBaseItemsReq(route.query.kb_name, currentPage.value, pageSize.value).then(res => {
    totalCount.value = res.data.total
    // 直接使用新数据替换当前页的数据
    itemList.value = res.data.items

    // 检查是否有文档正在处理中
    const hasProcessing = itemList.value.some(doc =>
        doc.status === 'processing'
    )
    if (hasProcessing) {
      startPolling()
    } else {
      stopPolling()
    }
  })
}

// 开始轮询
const startPolling = () => {
  if (pollingTimer.value) return
  pollingTimer.value = setInterval(() => {
    getItems()
  }, 5000)
}

// 停止轮询
const stopPolling = () => {
  if (pollingTimer.value) {
    clearInterval(pollingTimer.value)
    pollingTimer.value = null
  }
}

const getKnowledgeBaseDetail = () => {
  knowledgeBaseDetailReq(route.query.kb_name).then(res => {
    if (res.code === 0 && res.data) {
      editForm.kb_name = res.data.kb_name
      editForm.kb_info = res.data.kb_info
      editForm.embedding_model_name = res.data.embedding_model ? res.data.embedding_model.name : ''
      editForm.db_type = res.data.db_type
    } else {
      ElMessage.error(res.msg || '获取知识库详情失败')
    }
  }).catch(err => {
    ElMessage.error(err.message || '获取知识库详情失败')
  })
}

const onHandleDetailContentClick = (index) => {
  if (showDetailIndex.value === index) {
    showDetailIndex.value = -1
  } else {
    showDetailIndex.value = index
  }
}

const onHandleSaveClick = () => {
  knowledgeBaseUpdateInfoReq(route.query.kb_name, editForm.kb_info).then(() => {
    ElMessage({
      type: 'success',
      message: 'Update completed',
    })
  })
}

const onSearchClick = () => {
  if (!searchValue.value) {
    return
  }
  searchResult.value = []
  searching.value = true
  knowledgeSearchDocsReq(route.query.kb_name, searchValue.value)
      .then(res => {
        if (res.code === 0) {
          searchResult.value = res.data
        } else {
          ElMessage.error(res.msg || '搜索失败')
        }
      })
      .catch(err => {
        ElMessage.error(err.message || '搜索失败')
      })
      .finally(() => {
        searching.value = false
      })
}

const onHandleDeleteClick = () => {
  ElMessageBox.confirm(
      '删除知识库将同时删除所有文档和向量数据，此操作不可恢复，是否继续？',
      '删除知识库',
      {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning',
      }
  )
      .then(() => {
        knowledgeBaseDeleteReq(route.query.kb_name).then(() => {
          ElMessage({
            type: 'success',
            message: 'Delete completed',
          })
          routerBack()
        })
      }).catch(() => {
  })
}

const onMenuClick = (index) => {
  activeIndex.value = index
}


const routerBack = () => {
  router.back()
}

// 添加文件大小格式化函数
const formatFileSize = (bytes: number): string => {
  if (bytes === 0 || !bytes) return '0 B'
  const k = 1024
  const sizes = ['B', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${Number.parseFloat((bytes / k ** i).toFixed(2))} ${sizes[i]}`
}

// 监听分页变化
const handlePageChange = (page: number) => {
  currentPage.value = page
  getDocuments()
}

// 获取状态类型
const getStatusType = (status: string): string => {
  const statusMap = {
    completed: 'success',
    pending: 'info',
    processing: 'warning',
    failed: 'danger'
  }
  return statusMap[status] || 'info'
}

// 获取状态文本
const getStatusText = (status: string): string => {
  const statusMap = {
    completed: '已完成',
    pending: '等待处理',
    processing: '处理中',
    failed: '处理失败'
  }
  return statusMap[status] || status
}

// 格式化时间
const formatTime = (time: string) => {
  return new Date(time).toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// 重试处理
const handleRetry = async (item: any) => {
  try {
    await retryProcessItemReq(item.id)
    ElMessage.success('已重新提交处理')
    getItems() // 刷新列表
  } catch (error) {
    ElMessage.error('重试失败')
  }
}

// 添加上传按钮点击处理函数
const onOpenUpdateDialog = () => {
  router.push({
    name: 'KnowledgeDetailImport',
    query: {
      kb_name: route.query.kb_name
    }
  })
}

const handleRetryDocument = async (row) => {
  const res = await vectorizeDocumentReq(
      row.id,
      row.process_type,
      row.chunk_size,
      row.separator,
      row.ai_summary,
      row.ai_qa,
      row.strengthen_model_name,
      row.splitter_model_name
  )
  if (res.code !== 0) {
    ElMessage.error(`处理文件失败: ${res.msg}`)
    return
  }
  getDocuments()
}

// 在组件挂载时获取知识库详情
onMounted(() => {
  getKnowledgeBaseDetail()
})

// 添加删除文档的处理函数
const handleDeleteDocument = (document) => {
  ElMessageBox.confirm(
      '此操作除删除文档外，也会删除文档对应的向量，不可恢复。',
      '确定要删除吗？',
      {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning',
      }
  ).then(async () => {
    try {
      const res = await deleteDocumentReq(document.id)
      if (res.code === 0) {
        ElMessage.success('文档删除成功')
        getDocuments() // 刷新文档列表
      } else {
        ElMessage.error(res.msg || '删除失败')
      }
    } catch (error) {
      console.error('删除文档失败:', error)
      ElMessage.error('删除文档失败')
    }
  }).catch(() => {
    // 用户取消删除
  })
}

interface JsonItem {
  Operator: string
  Description: string
  Link: string
  Tree: string
  Detail: string
}

// 处理编辑
const handleEdit = (index: number) => {
  currentEditIndex.value = index
  currentEditItem.value = { ...itemList.value[index] }
  editDialogVisible.value = true
}

// 保存编辑
const handleSaveEdit = async () => {
  if (currentEditItem.value && currentEditIndex.value !== -1) {
    try {
      // 这里需要添加更新知识库项目的API调用
      await updateKnowledgeBaseItemReq(currentEditItem.value)
      itemList.value[currentEditIndex.value] = { ...currentEditItem.value }
      ElMessage.success('更新成功')
      editDialogVisible.value = false
    } catch (error) {
      ElMessage.error('更新失败')
    }
  }
}

// 删除项目
const handleDeleteItem = async (index: number) => {
  try {
    await ElMessageBox.confirm(
      '确定要删除这条数据吗？',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    )
    
    // 这里需要添加删除知识库项目的API调用
    await deleteKnowledgeBaseItemReq(itemList.value[index].id)
    itemList.value.splice(index, 1)
    ElMessage.success('删除成功')
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

</script>

<style>
.dataset-detail-drawer {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}

.dataset-detail-drawer > .el-drawer__header {
  margin-bottom: 0 !important;
}

.el-descriptions__body {
  background-color: transparent !important;
}

.expand-container {
  padding: 0 10px;
}
</style>

<style scoped lang="scss">


.detail-container {
  padding: 20px;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: #f5f7fa;
}

.header {
  width: 100%;
}


:deep(.my-descriptions-item) {
  color: #0d5aa7;
}

.menu-item {
  width: 100%;
  margin-bottom: 10px;
  padding: 10px 10px;
  border-radius: 10px;
  cursor: pointer;
  border: 1px solid var(--el-color-primary);
  color: var(--el-color-primary);
  background: var(--el-color-primary-light-9);

  .el-icon {
    margin-right: 10px;
  }

  &:hover {
    background: var(--el-color-primary);
    color: white;
  }

  &.active {
    background: var(--el-color-primary);
    color: white;
  }
}

.file-list-container {
  width: 100%;
}

.demo-table-expand {
  padding: 20px;
}

.demo-table-expand .el-form-item {
  margin-bottom: 0;
  margin-right: 0;
  width: 100%;
}

.chunk-content {
  padding: 15px;
  background-color: var(--el-fill-color-light);
  border-radius: 4px;
  margin-bottom: 10px;
}

.chunk-content p {
  margin: 0;
  line-height: 1.5;
  white-space: pre-wrap;
}

.chunk-meta {
  margin-top: 10px;
}

.el-form-item {
  margin-bottom: 15px;
}

.margin-top {
  margin-top: 15px;
}

.chunk-content {
  padding: 15px;
  background-color: var(--el-fill-color-light);
  border-radius: 4px;
  margin-bottom: 10px;
}

.chunk-content p {
  margin: 0;
  line-height: 1.5;
  white-space: pre-wrap;
}

.chunk-meta {
  margin-top: 10px;
}

:deep(.el-descriptions__label) {
  width: 120px;
  justify-content: flex-end;
}

:deep(.el-descriptions__content) {
  padding: 12px 15px;
}

.search-result-item {
  padding: 10px;
}

.document-info {
  margin-bottom: 10px;
}

.document-title {
  font-weight: bold;
  color: var(--el-color-primary);
  font-size: 16px;
}

.content {
  white-space: pre-wrap;
  line-height: 1.5;
  color: #333;
  background: var(--el-fill-color-light);
  padding: 10px;
  border-radius: 4px;
  margin: 10px 0;
}

.meta-info {
  margin-top: 10px;
}

.document-content {
  padding: 20px;
}

.content-preview {
  margin-top: 20px;
  padding: 15px;
  background-color: #f5f7fa;
  border-radius: 4px;
  max-height: 500px;
  overflow-y: auto;
}

.content-preview pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  margin: 0;
  font-family: monospace;
  font-size: 14px;
  line-height: 1.5;
}

.settings-container {
  padding: 20px;
  max-width: 800px;
}

.danger-zone {
  margin-top: 20px;
  padding: 20px;
  background-color: #fff1f0;
  border: 1px solid #ffccc7;
  border-radius: 4px;
}

.warning-text {
  color: #ff4d4f;
  margin: 0;
  font-size: 14px;
}

.tabs-container {
  width: 100%;
}

.upload-container {
  padding: 8px;
  text-align: center;
  cursor: pointer;
  border: 1px solid var(--el-color-primary);
  background: var(--el-color-primary);
  color: white;
  border-radius: 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  width: 120px;
}

.action-container {
  margin-top: 15px;
  display: flex;
  justify-content: flex-end;
  padding-right: 20px;
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
  padding: 20px;
  overflow-y: auto;
  height: calc(100vh - 120px);
}

.item-card {
  transition: all 0.3s ease;
  height: 100%;
  min-height: 300px;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
}

.card-content {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--el-border-color-lighter);
}

.operator {
  font-size: 18px;
  font-weight: bold;
  color: var(--el-color-primary);
}

.card-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.info-item {
  .label {
    font-size: 14px;
    color: var(--el-text-color-regular);
    margin-bottom: 4px;
  }

  .description,
  .tree,
  .detail {
    font-size: 14px;
    line-height: 1.3;
    color: var(--el-text-color-primary);
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
  }
  .detail {
    margin-bottom: 20px;
  }
}

.edit-form {
  max-height: 60vh;
  overflow-y: auto;
  padding: 20px;
}

:deep(.el-dialog__body) {
  padding: 0;
}

.status-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.status-tag {
  flex-shrink: 0;
}

.error-message {
  margin: 12px 0;
  
  .retry-button {
    margin-top: 8px;
  }
}

.card-info {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 12px 0;
  
  .time-tag {
    font-size: 12px;
  }
}

.item-card {
  &.processing {
    opacity: 0.8;
    pointer-events: none;
  }

  &.failed {
    border: 1px solid var(--el-color-danger-light-5);
  }
}

</style>
