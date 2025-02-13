<template>
  <div class="import-container">
    <!-- 顶部返回按钮和标题 -->
    <div class="header">
      <div class="columnSS" style="width: 100%;">
        <div v-if="currentStep === 1" class="rowSC">
          <el-button icon="ArrowLeftBold" type="primary" plain circle size="large" @click="router.back()" />
          <span style="font-weight: bold; font-size: 22px;">{{ route.query.kb_name }}</span>
        </div>
        <div v-else class="rowSC">
          <el-button icon="ArrowLeftBold" type="primary" plain size="default" @click="currentStep--">
            {{ $t('knowledge.import.prevStep') }}
          </el-button>
        </div>
      </div>
    </div>

    <!-- 步骤条 -->
    <el-steps :active="currentStep" finish-status="success" class="steps" align-center>
      <el-step :title="$t('knowledge.detail.steps.selectFile')" />
      <el-step :title="$t('knowledge.detail.steps.process')" />
      <el-step :title="$t('knowledge.detail.steps.addQueue')" />
    </el-steps>

    <!-- 文件上传区域 -->
    <div class="main-content">
      <!-- 第一步：选择文件 -->
      <div v-if="currentStep === 1">
        <el-upload
          ref="uploadRef"
          class="upload-drop"
          drag
          multiple
          :auto-upload="false"
          :show-file-list="false"
          :on-change="handleFileChange"
          :before-remove="handleFileRemove"
          :on-exceed="handleExceed"
          :limit="15"
          accept=".json"
        >
          <el-icon class="upload-icon">
            <Upload />
          </el-icon>
          <div class="upload-text">{{ $t('knowledge.import.upload.text') }}</div>
          <div class="upload-tip">
            {{ $t('knowledge.import.upload.tip') }}
            <br />
            {{ $t('knowledge.import.upload.limit') }}
          </div>
        </el-upload>

        <!-- 文件解析进度 -->
        <div v-if="fileList.length > 0" class="file-list">
          <div class="file-list-header">
            <div class="file-name">{{ $t('knowledge.import.fileList.name') }}</div>
            <div class="file-progress">{{ $t('knowledge.import.fileList.progress') }}</div>
            <div class="file-count">{{ $t('knowledge.import.fileList.count') }}</div>
            <div class="file-action">{{ $t('knowledge.import.fileList.action') }}</div>
          </div>
          <div v-for="(file, index) in fileList" :key="index" class="file-item">
            <div class="file-name">
              <el-icon>
                <Document />
              </el-icon>
              {{ file.name }}
            </div>
            <div class="file-progress">
              <el-progress :percentage="file.parseProgress || 0" :status="file.parseStatus" />
            </div>
            <div class="file-count">
              {{ file.itemCount || 0 }} {{ $t('knowledge.import.fileList.items') }}
            </div>
            <div class="file-action">
              <el-button type="danger" link @click="handleRemoveFile(index)">
                {{ $t('knowledge.import.fileList.delete') }}
              </el-button>
            </div>
          </div>
        </div>
      </div>

      <!-- 第二步：数据处理 -->
      <div v-if="currentStep === 2">
        <div v-if="jsonItems.length > 0" class="json-preview">
          <div class="preview-header">
            <span class="title">
              {{ $t('knowledge.import.preview.title') }} ({{ jsonItems.length }} {{ $t('knowledge.import.preview.count') }})
            </span>
          </div>

          <div class="cards-container">
            <el-card
              v-for="(item, index) in jsonItems"
              :key="index"
              class="item-card"
              shadow="hover"
            >
              <div class="card-content">
                <div class="card-header">
                  <span class="operator">{{ item.Operator }}</span>
                  <div class="actions">
                    <el-button type="primary" link @click="handleEdit(index)">
                      {{ $t('knowledge.import.card.edit') }}
                    </el-button>
                    <el-button type="danger" link @click="handleDeleteItem(index)">
                      {{ $t('knowledge.import.card.delete') }}
                    </el-button>
                  </div>
                </div>
                <div class="card-body">
                  <div class="info-item">
                    <div class="label">{{ $t('knowledge.import.card.description') }}</div>
                    <div class="description">{{ item.Description }}</div>
                  </div>
                  <div class="info-item">
                    <div class="label">{{ $t('knowledge.import.card.tree') }}</div>
                    <div class="tree">{{ item.Tree }}</div>
                  </div>
                  <div class="info-item">
                    <div class="label">{{ $t('knowledge.import.card.detail') }}</div>
                    <div class="detail">{{ item.Detail }}</div>
                  </div>
                </div>
              </div>
            </el-card>
          </div>
        </div>
      </div>

      <!-- 第三步：添加任务队列 -->
      <div v-if="currentStep === 3" class="process-container">
        <div class="process-content">
          <div class="rowCC" style="width: 100%">
            <el-icon style="font-size: 48px; color: var(--el-color-success); margin-right: 10px">
              <CircleCheckFilled />
            </el-icon>
            <span style="font-size: 16px">
              {{ $t('knowledge.import.message.addQueue', { countdown }) }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- 底部按钮 -->
    <div class="footer rowEC" style="width: 100%; margin-top: 20px;">
      <el-button
        type="primary"
        size="default"
        :disabled="!canProceed"
        @click="handleNextStep"
        :loading="uploading"
      >
        {{ getButtonText }}
      </el-button>
    </div>

    <!-- 编辑对话框 -->
    <el-dialog
      v-model="editDialogVisible"
      :title="$t('knowledge.import.dialog.edit.title')"
      width="80%"
      :close-on-click-modal="false"
    >
      <el-form v-if="currentEditItem" label-width="auto" label-position="right" class="edit-form">
        <el-form-item :label="$t('knowledge.import.dialog.edit.operator')">
          <el-input v-model="currentEditItem.Operator" />
        </el-form-item>
        <el-form-item :label="$t('knowledge.import.dialog.edit.description')">
          <el-input
            v-model="currentEditItem.Description"
            type="textarea"
            :rows="3"
          />
        </el-form-item>
        <el-form-item :label="$t('knowledge.import.dialog.edit.link')">
          <el-input v-model="currentEditItem.Link" />
        </el-form-item>
        <el-form-item :label="$t('knowledge.import.dialog.edit.tree')">
          <el-input
            v-model="currentEditItem.Tree"
            type="textarea"
            :rows="3"
          />
        </el-form-item>
        <el-form-item :label="$t('knowledge.import.dialog.edit.detail')">
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
            {{ $t('knowledge.import.dialog.edit.cancel') }}
          </el-button>
          <el-button type="primary" @click="handleSaveEdit">
            {{ $t('knowledge.import.dialog.edit.confirm') }}
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { Upload, CircleCheckFilled, Document } from '@element-plus/icons-vue'
import { addKnowledgeBaseItemsReq, vectorizeKnowledgeBaseItemsReq } from '@/api/knowledge'
import { useI18n } from '@/hooks/use-i18n'

const router = useRouter()
const route = useRoute()
const uploadRef = ref()
const i18n = useI18n()

interface JsonItem {
  Operator: string
  Description: string
  Link: string
  Tree: string
  Detail: string
}

// 添加el-upload的文件类型
interface UploadFile extends File {
  raw: File
}

// 修改 jsonItems 的类型声明
const jsonItems = ref<JsonItem[]>([])
const uploading = ref(false)
const currentStep = ref(1)
const countdown = ref(3)
const fileList = ref<any[]>([])

// 是否可以进行下一步
const canProceed = computed(() => {
  switch (currentStep.value) {
    case 1:
      return jsonItems.value.length > 0
    case 2:
      return jsonItems.value.length > 0
    case 3:
      return false
    default:
      return false
  }
})

// 按钮文字
const getButtonText = computed(() => {
  switch (currentStep.value) {
    case 1:
      return i18n.t('knowledge.import.button.next')
    case 2:
      return i18n.t('knowledge.import.button.upload')
    case 3:
      return i18n.t('knowledge.import.button.complete')
    default:
      return i18n.t('knowledge.import.button.next')
  }
})

// 处理文件数量超出限制
const handleExceed = () => {
  ElMessage.warning(i18n.t('knowledge.import.upload.exceed'))
}

// 处理文件移除前的操作
const handleFileRemove = (file: any) => {
  const index = fileList.value.indexOf(file)
  if (index !== -1) {
    // 从总数据中移除该文件的数据
    const removedFile = fileList.value[index]
    if (removedFile.items && removedFile.items.length > 0) {
      // 从jsonItems中移除该文件的所有数据
      jsonItems.value = jsonItems.value.filter(item => !removedFile.items.includes(item))
    }
    fileList.value.splice(index, 1)
  }
  return true
}

// 处理文件选择
const handleFileChange = async (file: UploadFile) => {
  if (!file) return

  // 检查文件类型
  if (!file.name.endsWith('.json')) {
    ElMessage.error('请上传JSON格式文件')
    return
  }

  // 添加文件到列表
  const fileItem = {
    name: file.name,
    raw: file.raw,
    parseProgress: 0,
    parseStatus: 'warning',
    itemCount: 0,
    items: [] as JsonItem[]
  }
  fileList.value.push(fileItem)

  // 读取文件内容
  const reader = new FileReader()
  reader.onload = (e) => {
    try {

      const content = JSON.parse(e.target?.result as string)
      if (!Array.isArray(content)) {
        fileItem.parseStatus = 'exception'
        ElMessage.error(`${file.name}: JSON文件内容必须是数组格式`)
        return
      }

      // 验证数组项格式
      const validItems = content.map(item => ({
        Operator: item.Operator || '',
        Description: item.Description || '',
        Link: item.Link || '',
        Tree: item.Tree || '',
        Detail: item.Detail || ''
      }))

      // 更新文件列表
      fileList.value = fileList.value.map(f => f.name === file.name ? { ...f, parseProgress: 100, parseStatus: 'success', itemCount: validItems.length, items: validItems } : f)

      // 合并到总的items中
      jsonItems.value = fileList.value.reduce((acc, file) => {
        if (file.items && Array.isArray(file.items)) {
          return [...acc, ...file.items]
        }
        return acc
      }, [])
    } catch (error) {
      fileList.value = fileList.value.map(f => f.name === file.name ? { ...f, parseProgress: 100, parseStatus: 'exception' } : f)
      ElMessage.error(`${file.name}: JSON文件解析失败`)
      console.error('JSON解析错误:', error)
    }
  }
  reader.readAsText(file.raw as Blob)
}

// 删除文件
const handleRemoveFile = (index: number) => {
  const removedFile = fileList.value[index]
  if (removedFile.items && removedFile.items.length > 0) {
    // 从jsonItems中移除该文件的所有数据
    jsonItems.value = jsonItems.value.filter(item => !removedFile.items.includes(item))
  }
  fileList.value.splice(index, 1)
}

// 删除某一项
const handleDeleteItem = (index: number) => {
  jsonItems.value.splice(index, 1)
}

// 处理下一步
const handleNextStep = async () => {
  if (currentStep.value === 2) {
    // 第二步点击上传
    await handleUpload()
  } else if (currentStep.value < 3) {
    currentStep.value++
  }
}

// 上传数据到知识库
const handleUpload = async () => {
  if (jsonItems.value.length === 0) {
    ElMessage.warning('请先选择要上传的数据')
    return
  }

  try {
    uploading.value = true
    const res = await addKnowledgeBaseItemsReq(route.query.kb_name as string, jsonItems.value)
    if (res.data.status === true) {
      const itemIds = res.data.data.success_ids || []
      const vectorizeRes = await vectorizeKnowledgeBaseItemsReq(route.query.kb_name as string, itemIds)
      if (vectorizeRes.data.status === true) {
        currentStep.value = 3
        // 倒计时后返回
        const timer = setInterval(() => {
          countdown.value--
          if (countdown.value <= 0) {
            clearInterval(timer)
            router.back()
          }
        }, 1000)
      } else {
        ElMessage.error(vectorizeRes.data.message || '向量化失败')
      }
    } else {
      ElMessage.error(res.data.message || '上传失败')
    }
  } catch (error: any) {
    ElMessage.error(error.message || '上传失败')
  } finally {
    uploading.value = false
  }
}

const editDialogVisible = ref(false)
const currentEditItem = ref<JsonItem | null>(null)
const currentEditIndex = ref(-1)

// 处理编辑
const handleEdit = (index: number) => {
  currentEditIndex.value = index
  currentEditItem.value = { ...jsonItems.value[index] }
  editDialogVisible.value = true
}

// 保存编辑
const handleSaveEdit = () => {
  if (currentEditItem.value && currentEditIndex.value !== -1) {
    jsonItems.value[currentEditIndex.value] = { ...currentEditItem.value }
  }
  editDialogVisible.value = false
}
</script>

<style scoped>
.import-container {
  padding: 20px;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: #f5f7fa;
}

.header {
  margin-bottom: 20px;
}

.main-content {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: white;
  border-radius: 8px;
  margin: 0 20px;
  flex: 1;
  overflow: hidden;
}

.upload-drop {
  width: 100%;
}

:deep(.el-upload-dragger) {
  width: 100%;
  height: 140px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 2px dashed #dcdfe6;
}

.upload-icon {
  font-size: 40px;
  color: var(--el-color-primary);
  margin-bottom: 10px;
}

.upload-text {
  font-size: 16px;
  color: #606266;
  margin-bottom: 10px;
}

.upload-tip {
  font-size: 14px;
  color: #909399;
  text-align: center;
  line-height: 1.5;
}

.json-preview {
  margin-top: 20px;
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.preview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.preview-header .title {
  font-size: 16px;
  font-weight: bold;
  color: #333;
}

.columnSS {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.rowSC {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  gap: 10px;
}

.steps {
  margin-bottom: 20px;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
}

.process-container {
  display: flex;
  justify-content: center;
  height: 100%;
  width: 100%;
}

.process-content {
  width: 100%;
  background: white;
  border-radius: 8px;
  padding: 40px;
  text-align: center;
}

.rowCC {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.file-list {
  margin-top: 20px;
  border: 1px solid #ebeef5;
  border-radius: 4px;
}

.file-list-header {
  display: grid;
  grid-template-columns: 2fr 2fr 1fr 100px;
  padding: 12px 20px;
  background-color: #f5f7fa;
  color: #909399;
  font-size: 14px;
  border-bottom: 1px solid #ebeef5;
}

.file-item {
  display: grid;
  grid-template-columns: 2fr 2fr 1fr 100px;
  padding: 12px 20px;
  align-items: center;
  border-bottom: 1px solid #ebeef5;
}

.file-name {
  display: flex;
  align-items: center;
  gap: 8px;
}

.file-progress {
  padding-right: 20px;
}

.file-count {
  color: var(--el-color-primary);
  font-weight: bold;
}

/* 编辑输入框样式 */
.edit-input {
  transition: all 0.3s ease;
}

.edit-input:deep(.el-input__inner) {
  font-size: 14px;
  padding: 8px 12px;
  transition: all 0.3s ease;
}

.edit-input:deep(.el-textarea__inner) {
  font-size: 14px;
  padding: 8px 12px;
  transition: all 0.3s ease;
  min-height: 60px;
}

/* 输入框焦点样式 */
.edit-input:deep(.el-input__inner:focus),
.edit-input:deep(.el-textarea__inner:focus) {
  transform: scale(1.02);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

/* 表格单元格样式 */
:deep(.el-table__cell) {
  padding: 12px !important;
}

:deep(.el-table__row) {
  transition: all 0.3s ease;
}

:deep(.el-table__row:hover) {
  background-color: var(--el-fill-color-light) !important;
  transform: translateY(-2px);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
  padding: 20px;
  overflow-y: auto;
  height: calc(100vh - 400px);
}

.item-card {
  transition: all 0.3s ease;
  height: 100%;
  min-height: 300px;
}

.item-card:hover {
  transform: translateY(-5px);
}

.card-content {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding-bottom: 16px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ebeef5;
  padding-bottom: 12px;
  flex-shrink: 0;
}

.operator {
  font-size: 20px;
  font-weight: bold;
  color: var(--el-color-primary);
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-top: 12px;
  flex: 1;
  justify-content: space-between;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-height: 0;
  flex-shrink: 1;
}

.info-item:last-child {
  margin-bottom: 8px;
}

.label {
  font-size: 13px;
  color: #909399;
  font-weight: 500;
}

.description {
  font-size: 14px;
  color: #606266;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.5;
}

.tree {
  font-size: 14px;
  color: #606266;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.5;
}

.detail {
  font-size: 14px;
  color: #606266;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.5;
}

.edit-form {
  max-height: 60vh;
  overflow-y: auto;
  padding: 20px;
}

:deep(.el-dialog__body) {
  padding: 0;
}
</style>
