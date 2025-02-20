<template>
  <div class="detail-container">
    <div class="rowBC header">
      <div class="rowBC" style="max-width: 50%; flex-shrink: 0; min-width: 200px">
        <el-button icon="ArrowLeftBold" type="primary" plain circle size="large" @click="routerBack()"/>
        <div class="columnSS" style="margin-left: 10px; width: 100%">
          <span style="font-weight: bold; font-size: 22px; margin-bottom: 5px">{{ $route.query.kb_name }}</span>
          <span style="font-size: 12px; color: #666666">{{ $t('knowledge.detail.dataCount') }}: {{ totalCount }}</span>
        </div>
      </div>
      <div class="rowEC" style="width: 100%; flex-shrink: 1;">
        <div v-if="activeIndex === 'dataset'" class="rowBC">
          <div class="rowBC">

            <el-tooltip
              effect="dark"
              placement="top"
            >
            <div class="upload-container" @click="onOpenUpdateDialog">
              <span>{{ $t('knowledge.import.json') }}</span>
              <el-icon style="margin-left: 10px; height: 20px;">
              <InfoFilled />
            </el-icon>
            </div>
              <template #content>
                Json文件请参考以下格式：
                <pre style="text-align: left; margin: 10px;">{{ jsonFormatExample }}</pre>
              </template>
            </el-tooltip>
          </div>
          <div class="upload-container" style="margin-left: 10px;" @click="showAddItemDialog">
            <span>{{ $t('knowledge.import.single') }}</span>
          </div>
        </div>
        <div v-else-if="activeIndex === 'search'" class="rowBC" style="width: 100%">
          <el-input
              v-model="searchValue" 
              :placeholder="$t('knowledge.import.search.placeholder')" 
              size="large"
              style="width: 100%; margin: 0 20px" />
          <el-button size="default" :loading="searching" type="primary" @click="onSearchClick">
            {{ $t('knowledge.import.search.button') }}
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
              <span>{{ $t('knowledge.detail.menu.dataset') }}</span>
            </div>
            <div :class="`rowSC menu-item ${activeIndex === 'search' ? ' active' : ''}`" @click="onMenuClick('search')">
              <el-icon>
                <Search/>
              </el-icon>
              <span>{{ $t('knowledge.detail.menu.search') }}</span>
            </div>
            <div :class="`rowSC menu-item ${activeIndex === 'setting' ? ' active' : ''}`"
                 @click="onMenuClick('setting')">
              <el-icon>
                <Setting/>
              </el-icon>
              <span>{{ $t('knowledge.detail.menu.setting') }}</span>
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
                    <span class="operator">{{ item.content?.keyword || item.content?.Operator }}</span>
                    <div class="header-right">
                      <el-tag 
                        :type="getStatusType(item.status)" 
                        size="small" 
                        class="status-tag"
                      >
                        {{ $t(`knowledge.detail.status.${item.status}`) }}
                      </el-tag>
                      <el-button 
                        type="primary"  
                        @click="toggleExpand(index)"
                      >
                        {{ expandedCards[index] ? '收起' : '展开' }}
                      </el-button>
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
                          {{ $t('knowledge.detail.button.retry') }}
                        </el-button>
                      </template>
                    </el-alert>
                  </div>

                  <div v-show="expandedCards[index]" class="card-body">
                    <div class="card-info">
                      <div class="info-right">
                        <el-tag size="small" type="info" class="time-tag">
                          {{ formatTime(item.created_at) }}
                        </el-tag>
                        <div v-if="item.status === 'completed' || item.status === 'failed'" class="actions">
                          <el-button type="danger" @click="handleDeleteItem(index)">
                            {{ $t('knowledge.detail.button.delete') }}
                          </el-button>
                        </div>
                      </div>
                    </div>

                    <div class="info-item">
                      <div class="label">Content:</div>
                      <div class="content-value">
                        <pre class="json-content">{{ JSON.stringify(item.content, null, 2) }}</pre>
                      </div>
                    </div>
                  </div>
                </div>
              </el-card>
            </div>

            <!-- 编辑对话框 -->
            <el-dialog
              v-model="editDialogVisible"
              :title="$t('knowledge.detail.dialog.edit.title')"
              width="80%"
              :close-on-click-modal="false"
            >
              <el-form v-if="currentEditItem" label-width="auto" label-position="right" class="edit-form">
                <el-form-item label="keyword">
                  <el-input v-model="currentEditItem.Operator" />
                </el-form-item>
                <el-form-item label="description">
                  <el-input
                    v-model="currentEditItem.Description"
                    type="textarea"
                    :rows="3"
                  />
                </el-form-item>
                <el-form-item :label="$t('knowledge.detail.form.link')">
                  <el-input v-model="currentEditItem.Link" />
                </el-form-item>
                <el-form-item :label="$t('knowledge.detail.form.tree')">
                  <el-input
                    v-model="currentEditItem.Tree"
                    type="textarea"
                    :rows="3"
                  />
                </el-form-item>
                <el-form-item :label="$t('knowledge.detail.form.detail')">
                  <el-input
                    v-model="currentEditItem.Detail"
                    type="textarea"
                    :rows="5"
                  />
                </el-form-item>
              </el-form>
              <template #footer>
                <div class="dialog-footer">
                  <el-button @click="editDialogVisible = false">
                    {{ $t('knowledge.detail.dialog.edit.cancel') }}
                  </el-button>
                  <el-button type="primary" @click="handleSaveEdit">
                    {{ $t('knowledge.detail.dialog.edit.confirm') }}
                  </el-button>
                </div>
              </template>
            </el-dialog>
          </div>
        </div>
        <div v-if="activeIndex === 'search'">
          <el-table :data="searchResult" :loading="searching" style="width: 100%; border-radius: 10px;" height="calc(100vh - 140px)">
            <el-table-column :label="$t('knowledge.detail.search.title')">
              <template #default="scope">
                <div class="search-result-item">
                  <div class="document-info rowSC">
                    <el-tag size="small" style="margin-right: 10px">
                      <span style="font-weight: bold; font-size: 16px">
                        {{ $t('knowledge.detail.search.result') }} {{ scope.$index + 1 }}
                      </span>
                      #
                      <span style="font-weight: bold; font-size: 16px">
                        {{ $t('knowledge.detail.search.score') }}{{ scope.row.score }}
                      </span>
                    </el-tag>
                    <span class="document-title">{{ scope.row.document?.title }}</span>
                  </div>
                  <div class="content">{{ scope.row.content }}</div>
                  <div v-if="scope.row.meta_info" class="meta-info">
                    <el-descriptions :column="2" size="small" border>
                      <el-descriptions-item v-for="(value, key) in scope.row.meta_info" :key="key" :label="key">
                        {{ value }}
                      </el-descriptions-item>
                      <el-descriptions-item :label="$t('knowledge.detail.search.docFormat')">
                        {{ scope.row.document?.type }}
                      </el-descriptions-item>
                      <el-descriptions-item :label="$t('knowledge.detail.search.splitIndex')">
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
              <span style="color: #000000; width: 160px; text-align: left; font-size: 16px; flex-shrink: 0">
                {{ $t('knowledge.detail.form.name') }}
              </span>
              <el-input size="large" v-model="editForm.kb_name" style="width: 200px;" />
            </div>

            <div class="rowSC" style="width: 100%; margin-top: 20px;">
              <span style="color: #000000; width: 160px; text-align: left; font-size: 16px; flex-shrink: 0">
                {{ $t('knowledge.detail.form.description') }}
              </span>
              <el-input size="large" v-model="editForm.kb_info" :rows="2" type="textarea"/>
            </div>

            <div class="rowSC" style="width: 100%; margin-top: 20px;">
              <span style="color: #000000; width: 160px; text-align: left; font-size: 16px; flex-shrink: 0">
                {{ $t('knowledge.detail.form.embeddingModel') }}
              </span>
              <el-input size="large" v-model="editForm.embedding_model_name" disabled style="width: 200px;" />
            </div>

            <div class="rowSC" style="width: 100%; margin-top: 20px;">
              <span style="color: #000000; width: 160px; text-align: left; font-size: 16px; flex-shrink: 0">
                {{ $t('knowledge.detail.form.databaseType') }}
              </span>
              <el-input size="large" v-model="editForm.db_type" disabled style="width: 200px;" />
            </div>

            <div class="rowSC" style="margin-top: 20px">
              <el-button :icon="Delete" size="small" @click="onHandleDeleteClick">
                {{ $t('knowledge.detail.button.delete') }}
              </el-button>
              <el-button size="medium" icon="Edit" type="primary" @click="onHandleSaveClick">
                {{ $t('knowledge.detail.button.save') }}
              </el-button>
            </div>
          </div>
        </div>
      </el-main>
    </el-container>
    <el-dialog
        v-model="chunksDialogVisible"
        :title="$t('knowledge.detail.chunks.title')"
        width="80%"
        top="3vh"
        style="height: 92vh"
        :destroy-on-close="true">
      <el-collapse v-if="currentChunks" v-loading="chunksLoading" style="height: calc(92vh - 80px); overflow-y: scroll">
        <el-collapse-item v-for="(chunk, index) in currentChunks" :key="index" title="">
          <template #title>
            <el-tag size="small" style="margin-right: 10px">
              {{ $t('knowledge.detail.chunks.block') }}: {{ chunk.content_info.content_index + 1 }}
            </el-tag>
            <span style="display: inline-block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100%;">
              {{ chunk.chunk_content }}
            </span>
          </template>
          <div class="chunk-content">
            <p>{{ chunk.content_info.content }}</p>
          </div>
        </el-collapse-item>
      </el-collapse>
    </el-dialog>
    <!-- 添加新知识对话框 -->
    <el-dialog
      v-model="addItemDialogVisible"
      :title="$t('knowledge.detail.dialog.add.title')"
      width="80%"
      :close-on-click-modal="false"
    >
      <div
        v-loading="addingItem"
        :element-loading-text="$t('knowledge.detail.dialog.add.loading')"
        element-loading-background="rgba(255, 255, 255, 0.7)"
      >
        <el-form 
          ref="newItemForm" 
          :model="newItem"
          :rules="newItemRules"
          v-if="newItem" 
          size="large" 
          label-width="auto" 
          label-position="right" 
          class="edit-form"
        >
          <el-form-item label="keyword" prop="keyword">
            <el-input v-model="newItem.keyword" />
          </el-form-item>
          <el-form-item label="type" prop="type">
            <el-select v-model="newItem.type" :placeholder="$t('knowledge.detail.dialog.add.typePlaceholder')">
              <el-option label="function" value="function" />
              <el-option label="keyword" value="keyword" />
              <el-option label="type" value="type" />
              <el-option label="operator" value="operator" />
            </el-select>
          </el-form-item>
          <el-form-item label="detail" prop="detail">
            <el-input
              v-model="newItem.detail"
              type="textarea"
              :rows="2"
            />
          </el-form-item>
          <el-form-item label="description" prop="description">
            <el-input
              v-model="newItem.description"
              type="textarea"
              :rows="2"
            />
          </el-form-item>
          <el-form-item label="tree" prop="tree">
            <el-input
              v-model="newItem.tree"
              type="textarea"
              :rows="3"
            />
          </el-form-item>
          <el-form-item label="link" prop="link">
            <el-input v-model="newItem.link" />
          </el-form-item>
          <el-form-item label="example" prop="example">
            <el-input
              v-model="newItem.example"
              type="textarea"
              :rows="5"
            />
          </el-form-item>
        </el-form>
      </div>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="addItemDialogVisible = false" :disabled="addingItem">
            {{ $t('knowledge.detail.dialog.add.cancel') }}
          </el-button>
          <el-button type="primary" @click="handleAddItem" :loading="addingItem">
            {{ $t('knowledge.detail.dialog.add.confirm') }}
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts" name="KnowledgeDetail">
import {knowledgeBaseDeleteReq, knowledgeBaseDetailReq, knowledgeBaseUpdateInfoReq, knowledgeSearchDocsReq, getKnowledgeBaseItemsReq, addKnowledgeBaseItemsReq, deleteKnowledgeBaseItemsReq, vectorizeKnowledgeBaseItemsReq} from "@/api/knowledge";
import {ElMessage, ElMessageBox} from 'element-plus'
import type {Ref} from 'vue'
import {onMounted, reactive, ref, watch} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import { useI18n } from '@/hooks/use-i18n'
import { FormInstance } from 'element-plus'
import { InfoFilled } from '@element-plus/icons-vue'
const i18n = useI18n()

const router = useRouter()
const route = useRoute()
const activeIndex = ref('dataset')
const itemList: Ref<Array<any>> = ref([])
const currentPage = ref(1)
const pageSize = ref(20)
const totalCount = ref(0)
const searchValue = ref('')
const searchResult = ref([])
const searching = ref(false)
const newItemForm = ref<FormInstance | null>(null)
const pollingTimer = ref<NodeJS.Timer | null>(null)

const editForm = reactive({
  kb_id: '',
  kb_name: '',
  kb_info: '',
  embedding_model_name: '',
  db_type: ''
})

const newItemRules = {
  keyword: [
    { required: true, message: i18n.t('knowledge.detail.message.keywordRequired'), trigger: 'blur' }
  ],
  type: [
    { required: true, message: i18n.t('knowledge.detail.message.typeRequired'), trigger: 'blur' }
  ],
  detail: [
    { required: true, message: i18n.t('knowledge.detail.message.detailRequired'), trigger: 'blur' }
  ],
  description: [
    { required: true, message: i18n.t('knowledge.detail.message.descriptionRequired'), trigger: 'blur' }
  ],
  tree: [
    { required: true, message: i18n.t('knowledge.detail.message.treeRequired'), trigger: 'blur' }
  ]
}

const chunksDialogVisible = ref(false)
const chunksDialogTitle = ref("文档分块详情")
const chunksLoading = ref(false)
const currentChunks = ref(null)

// 添加编辑相关的响应式变量
const editDialogVisible = ref(false)
const currentEditItem = ref<JsonItem | null>(null)
const currentEditIndex = ref(-1)

// 添加新知识相关
const addItemDialogVisible = ref(false)
const addingItem = ref(false)
const newItem = ref({
  keyword: '',
  type: '',
  tree: '',
  detail: '',
  description: '',
  link: '',
  example: ''
})

// 添加 JSON 格式示例
const jsonFormatExample = ref(`[
  {
    "keyword": "关键词，必填",
    "type": "function, keyword, type, operator 四个中选择一个。必填",
    "tree": "语法树，必填",
    "detail": "详细信息，必填",
    "description": "简要描述，必填",
    "link": "相关链接",
    "example": "使用示例"
  }
]`)

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
        doc.status === 'pending'
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
  // 设置轮询间隔
  pollingTimer.value = setInterval(() => {
    getItems()
  }, 5000) // 每5秒轮询一次
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
      editForm.kb_id = res.data.id
      editForm.kb_name = res.data.kb_name
      editForm.kb_info = res.data.kb_info
      editForm.embedding_model_name = res.data.embedding_model ? res.data.embedding_model.name : ''
      editForm.db_type = res.data.db_type
    } else {
      ElMessage.error(res.msg || i18n.t('knowledge.detail.error.getDetail'))
    }
  }).catch(err => {
    ElMessage.error(err.message || i18n.t('knowledge.detail.error.getDetail'))
  })
}

const onHandleSaveClick = () => {
  knowledgeBaseUpdateInfoReq(editForm.kb_name, editForm.kb_info, editForm.kb_id).then(() => {
    ElMessage({
      type: 'success',
      message: 'Update completed',
    })
    // 修改当前路由的query参数
    router.replace({
      query: {
        ...route.query,
        kb_name: editForm.kb_name
      }
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
        ElMessage.error(res.msg || i18n.t('knowledge.detail.error.search'))
      }
    })
    .catch(err => {
      ElMessage.error(err.message || i18n.t('knowledge.detail.error.search'))
    })
    .finally(() => {
      searching.value = false
    })
}

const onHandleDeleteClick = () => {
  ElMessageBox.confirm(
    i18n.t('knowledge.detail.message.deleteKbConfirm'),
    i18n.t('knowledge.detail.message.deleteKbTitle'),
    {
      confirmButtonText: i18n.t('common.confirm'),
      cancelButtonText: i18n.t('common.cancel'),
      type: 'warning',
    }
  )
  .then(() => {
    knowledgeBaseDeleteReq(route.query.kb_name).then(() => {
      ElMessage.success(i18n.t('knowledge.detail.message.deleteKbSuccess'))
      routerBack()
    })
  }).catch(() => {})
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
  getItems()
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
    await vectorizeKnowledgeBaseItemsReq(route.query.kb_name, [item.id])
    ElMessage.success(i18n.t('knowledge.detail.message.retrySuccess'))
    getItems()
  } catch (error) {
    ElMessage.error(i18n.t('knowledge.detail.message.retryError'))
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

// 在组件挂载时获取知识库详情
onMounted(() => {
  getKnowledgeBaseDetail()
})


interface JsonItem {
  keyword: string
  type: string
  tree: string
  detail: string
  description: string
  link: string
  example: string
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
      await updateKnowledgeBaseItemReq(currentEditItem.value)
      itemList.value[currentEditIndex.value] = { ...currentEditItem.value }
      ElMessage.success(i18n.t('knowledge.detail.message.updateSuccess'))
      editDialogVisible.value = false
    } catch (error) {
      ElMessage.error(i18n.t('knowledge.detail.message.updateError'))
    }
  }
}

// 删除项目
const handleDeleteItem = async (index: number) => {
  try {
    await ElMessageBox.confirm(
      i18n.t('knowledge.detail.dialog.delete.confirmMessage'),
      i18n.t('knowledge.detail.dialog.delete.title'),
      {
        confirmButtonText: i18n.t('common.confirm'),
        cancelButtonText: i18n.t('common.cancel'),
        type: 'warning',
      }
    )
    
    await deleteKnowledgeBaseItemsReq(route.query.kb_name, [itemList.value[index].id])
    itemList.value.splice(index, 1)
    ElMessage.success(i18n.t('knowledge.detail.dialog.delete.success'))
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error(i18n.t('knowledge.detail.dialog.delete.error'))
    }
  }
}

// 显示添加对话框
const showAddItemDialog = () => {
  newItem.value = {
    keyword: '',
    type: '',
    tree: '',
    detail: '',
    description: '',
    link: '',
    example: ''
  }
  addItemDialogVisible.value = true
}

// 处理添加新知识
const handleAddItem = async () => {
  const formEl = newItemForm.value as FormInstance | undefined
  
  if (!formEl) return

  await formEl.validate((valid) => {
    if (valid) {
      addingItem.value = true
      addKnowledgeBaseItemsReq(route.query.kb_name, [newItem.value])
        .then((res) => {
          if (res.code === 0 && res.data.status) {
            addItemDialogVisible.value = false
            setTimeout(() => {
              getItems()
              addingItem.value = false
            }, 1000)
            ElMessage.success(i18n.t('knowledge.detail.message.addSuccess'))
          } else {
            addingItem.value = false  
            ElMessage.error(res.data.message || i18n.t('knowledge.detail.message.addError'))
          }
        })
        .catch(() => {
          addingItem.value = false
          ElMessage.error(i18n.t('knowledge.detail.message.addError'))
        })
    }
  })
}

const expandedCards = ref<{ [key: number]: boolean }>({})

const toggleExpand = (index: number) => {
  expandedCards.value[index] = !expandedCards.value[index]
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
  padding: 10px 15px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  &:hover {
    opacity: 0.9;
  }
}

.action-container {
  margin-top: 15px;
  display: flex;
  justify-content: flex-end;
  padding-right: 20px;
}

.cards-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 20px;
  overflow-y: auto;
  height: calc(100vh - 120px);
}

.item-card {
  transition: all 0.3s ease;
  width: 100%;
  margin-bottom: 0;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--el-border-color-lighter);

  .header-right {
    display: flex;
    align-items: center;
    gap: 12px;
  }
}

.operator {
  font-size: 16px;
  font-weight: bold;
  color: var(--el-color-primary);
}

.card-body {
  margin-top: 12px;
  padding: 16px;
  background-color: var(--el-fill-color-light);
  border-radius: 4px;
  transition: all 0.3s ease;
}

.card-content {
  display: flex;
  flex-direction: column;
}

.info-item {
  .label {
    font-size: 14px;
    font-weight: bold;
    color: var(--el-text-color-regular);
    margin-bottom: 4px;
  }

  .content-value {
    font-size: 14px;
    line-height: 1.3;
    color: var(--el-text-color-primary);
    margin-bottom: 8px;
    
    .json-content {
      white-space: pre-wrap;
      word-wrap: break-word;
      background-color: var(--el-fill-color-light);
      border-radius: 4px;
      padding: 8px;
      margin: 0;
      font-family: monospace;
      min-height: 100px;
      line-height: 1.6;
      font-size: 16px;
    }
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
  justify-content: flex-end;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--el-border-color-lighter);
  
  .info-right {
    display: flex;
    align-items: center;
    gap: 12px;
    
    .time-tag {
      font-size: 12px;
    }
    
    .actions {
      margin-left: 8px;
    }
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

/* 美化滚动条样式 */
.card-body::-webkit-scrollbar,
.json-content::-webkit-scrollbar {
  width: 6px;
}

.card-body::-webkit-scrollbar-thumb,
.json-content::-webkit-scrollbar-thumb {
  background-color: var(--el-border-color-lighter);
  border-radius: 3px;
}

.card-body::-webkit-scrollbar-track,
.json-content::-webkit-scrollbar-track {
  background-color: transparent;
}

</style>
