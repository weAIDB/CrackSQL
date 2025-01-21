<template>
  <div class="model-management">
    <div class="header-actions">
      <el-button v-if="activeTab === 'llm'" size="default" type="primary" @click="handleCreate">
        <el-icon>
          <Plus/>
        </el-icon>
        添加LLM模型
      </el-button>
      <el-button v-else size="default" type="primary" @click="handleCreate">
        <el-icon>
          <Plus/>
        </el-icon>
        添加Embedding模型
      </el-button>
    </div>
    <el-tabs v-model="activeTab" class="model-tabs">
      <el-tab-pane label="LLM模型" name="llm">
        <div class="models-container">
          <div v-for="model in llmModels" :key="model.id" class="model-card">
            <div class="model-header">
              <div class="model-title">
                <el-icon :size="20" :color="'var(--el-color-primary)'">
                  <component :is="model.deployment_type === 'cloud' ? 'Cloudy' : 'Monitor'"/>
                </el-icon>
                <el-tag :type="model.deployment_type === 'cloud' ? 'success' : 'warning'" size="small">
                  {{ model.deployment_type === 'cloud' ? '云端' : '本地' }}
                </el-tag>
                <span class="model-name">{{ model.name }}</span>
              </div>
              <el-tag :type="model.is_active ? 'success' : 'warning'" size="small">
                {{ model.is_active ? '启用中' : '已禁用' }}
              </el-tag>
            </div>

            <div class="model-info">
              <template v-if="model.deployment_type === 'cloud'">
                <div class="info-item">
                  <el-icon>
                    <Link/>
                  </el-icon>
                  <el-tooltip :content="model.api_base" placement="top" :disabled="!model.api_base">
                    <span class="info-text">{{ model.api_base || '未设置API地址' }}</span>
                  </el-tooltip>
                </div>
              </template>
              <template v-else>
                <div class="info-item">
                  <el-icon>
                    <FolderOpened/>
                  </el-icon>
                  <el-tooltip :content="model.path" placement="top" :disabled="!model.path">
                    <span class="info-text">{{ model.path || '未设置模型路径' }}</span>
                  </el-tooltip>
                </div>
              </template>
              <div class="info-item">
                <el-icon>
                  <TrendCharts/>
                </el-icon>
                <span class="info-text">温度: {{ model.temperature }}</span>
              </div>
              <div class="info-item">
                <el-icon>
                  <Tickets/>
                </el-icon>
                <span class="info-text">最大Token: {{ model.max_tokens || '未设置' }}</span>
              </div>
            </div>

            <div class="model-desc" :title="model.description">
              {{ model.description || '暂无描述' }}
            </div>

            <div class="model-footer">
              <el-tooltip content="编辑模型" placement="top">
                <el-button size="default" type="primary" plain @click="handleEdit(model)">
                  <el-icon>
                    <Edit/>
                  </el-icon>
                </el-button>
              </el-tooltip>
              <el-tooltip content="删除模型" placement="top">
                <el-button size="default" type="danger" plain @click="handleDelete(model)">
                  <el-icon>
                    <Delete/>
                  </el-icon>
                </el-button>
              </el-tooltip>
            </div>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane label="Embedding模型" name="embedding">
        <div class="models-container">
          <div v-for="model in embedModels" :key="model.id" class="model-card">
            <div class="model-header">
              <div class="model-title">
                <el-icon :size="20" :color="'var(--el-color-primary)'">
                  <component :is="model.deployment_type === 'cloud' ? 'Cloudy' : 'Monitor'"/>
                </el-icon>
                <el-tag :type="model.deployment_type === 'cloud' ? 'success' : 'warning'" size="small">
                  {{ model.deployment_type === 'cloud' ? '云端' : '本地' }}
                </el-tag>
                <span class="model-name">{{ model.name }}</span>
              </div>
              <el-tag :type="model.is_active ? 'success' : 'warning'" size="small">
                {{ model.is_active ? '启用中' : '已禁用' }}
              </el-tag>
            </div>

            <div class="model-info">
              <template v-if="model.deployment_type === 'cloud'">
                <div class="info-item">
                  <el-icon>
                    <Link/>
                  </el-icon>
                  <el-tooltip :content="model.api_base" placement="top" :disabled="!model.api_base">
                    <span class="info-text">{{ model.api_base || '未设置API地址' }}</span>
                  </el-tooltip>
                </div>
              </template>
              <template v-else>
                <div class="info-item">
                  <el-icon>
                    <FolderOpened/>
                  </el-icon>
                  <el-tooltip :content="model.path" placement="top" :disabled="!model.path">
                    <span class="info-text">{{ model.path || '未设置模型路径' }}</span>
                  </el-tooltip>
                </div>
              </template>
              <div class="info-item" v-if="model.dimension">
                <el-icon>
                  <Histogram/>
                </el-icon>
                <span class="info-text">向量维度: {{ model.dimension }}</span>
              </div>
            </div>

            <div class="model-desc" :title="model.description">
              {{ model.description || '暂无描述' }}
            </div>

            <div class="model-footer">
              <el-tooltip content="编辑模型" placement="top">
                <el-button size="default" type="primary" plain @click="handleEdit(model)">
                  <el-icon>
                    <Edit/>
                  </el-icon>
                </el-button>
              </el-tooltip>
              <el-tooltip content="删除模型" placement="top">
                <el-button size="default" type="danger" plain @click="handleDelete(model)">
                  <el-icon>
                    <Delete/>
                  </el-icon>
                </el-button>
              </el-tooltip>
            </div>
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
    <!-- LLM模型表单对话框 -->
    <el-dialog v-model="dialogVisible" :title="modelForm.id ? '编辑模型' : '添加模型'" width="600px">
      <el-form ref="formRef" size="default" :model="modelForm" :rules="modelRules" label-width="100px">
        <el-form-item label="模型名称" prop="name">
          <el-input v-model="modelForm.name" :disabled="modelForm.id" />
        </el-form-item>
        <el-form-item label="部署类型" prop="deployment_type">
          <el-radio-group v-model="modelForm.deployment_type" :disabled="modelForm.id">
            <el-radio label="cloud">云端模型</el-radio>
            <el-radio label="local">本地模型</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item v-if="modelForm.deployment_type === 'local'" label="模型路径" prop="path">
          <el-input v-model="modelForm.path"/>
        </el-form-item>
        <el-form-item v-if="modelForm.deployment_type === 'cloud'" label="API地址" prop="api_base">
          <el-input v-model="modelForm.api_base"/>
        </el-form-item>
        <el-form-item v-if="modelForm.deployment_type === 'cloud'" label="API密钥" prop="api_key">
          <el-input v-model="modelForm.api_key" type="password" show-password/>
        </el-form-item>
        <template v-if="activeTab === 'llm'">
          <el-form-item label="温度" prop="temperature">
            <el-slider v-model="modelForm.temperature" :min="0" :max="2" :step="0.1"/>
          </el-form-item>
          <el-form-item label="最大Token" prop="max_tokens">
            <el-input-number v-model="modelForm.max_tokens" :min="0" :step="100"/>
          </el-form-item>
        </template>
        <template v-else>
          <el-form-item label="向量维度" prop="dimension">
            <el-input-number v-model="modelForm.dimension" :min="1" :step="64" :disabled="modelForm.id"/>
          </el-form-item>
        </template>
        <el-form-item label="描述" prop="description">
          <el-input v-model="modelForm.description" type="textarea" :rows="3"/>
        </el-form-item>
        <el-form-item label="状态" prop="is_active">
          <el-switch v-model="modelForm.is_active"/>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit" :loading="formSubmitting">
          确定
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>


<script setup>
import {createLLMModelReq, deleteLLMModelReq, llmModelsReq, updateLLMModelReq} from '@/api/models'
import {Plus} from '@element-plus/icons-vue'
import {ElMessage, ElMessageBox} from 'element-plus'
import {onMounted, reactive, ref} from 'vue'

// 状态变量
const activeTab = ref('llm')
const llmLoading = ref(false)
const embeddingLoading = ref(false)
const llmModels = ref([])
const embedModels = ref([])
const dialogVisible = ref(false)
const formSubmitting = ref(false)
const formRef = ref()

// 统一的表单数据结构
const modelForm = reactive({
  id: null,
  name: '',
  deployment_type: 'cloud',  // 默认云端模型
  category: 'llm',  // 默认LLM类型
  path: '',
  api_base: '',
  api_key: '',
  temperature: 0.7,
  max_tokens: 2000,
  dimension: 768,  // embedding模型需要
  description: '',
  is_active: true
})

// 统一的表单验证规则
const modelRules = {
  name: [
    {required: true, message: '请输入模型名称', trigger: 'blur'},
    {min: 2, max: 100, message: '长度在 2 到 100 个字符', trigger: 'blur'}
  ],
  deployment_type: [
    {required: true, message: '请选择部署类型', trigger: 'change'}
  ],
  path: [
    {required: true, message: '请输入模型路径', trigger: 'blur'}
  ],
  api_base: [
    {required: true, message: '请输入API地址', trigger: 'blur'}
  ],
  dimension: [
    {
      required: true,
      message: '请输入向量维度',
      trigger: 'blur',
      type: 'number'
    }
  ]
}

// 统一的处理方法
const handleCreate = () => {
  const category = activeTab.value
  Object.assign(modelForm, {
    id: null,
    name: '',
    deployment_type: 'cloud',
    category,
    path: '',
    api_base: '',
    api_key: '',
    temperature: category === 'llm' ? 0.7 : undefined,
    max_tokens: category === 'llm' ? 2000 : undefined,
    dimension: category === 'embedding' ? 768 : undefined,
    description: '',
    is_active: true
  })
  dialogVisible.value = true
}

const handleEdit = (row) => {
  Object.assign(modelForm, row)
  dialogVisible.value = true
}

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm('确定要删除该模型吗？', '提示', {
      type: 'warning'
    })
    await deleteLLMModelReq(row.id)
    await fetchModels()
    ElMessage.success('删除成功')
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error(error.message || '删除失败')
    }
  }
}

const handleStatusChange = async (row) => {
  try {
    await updateLLMModelReq({
      ...row,
      is_active: !row.is_active
    })
    await fetchModels()
  } catch (error) {
    ElMessage.error(error.message || '更新状态失败')
  }
}

const handleSubmit = async () => {
  if (!formRef.value) return

  await formRef.value.validate(async (valid) => {
    if (valid) {
      formSubmitting.value = true
      try {
        if (modelForm.id) {
          await updateLLMModelReq(modelForm)
          ElMessage.success('更新成功')
        } else {
          await createLLMModelReq(modelForm)
          ElMessage.success('创建成功')
        }
        dialogVisible.value = false
        await fetchModels()
      } catch (error) {
        ElMessage.error(error.message || (modelForm.id ? '更新失败' : '创建失败'))
      } finally {
        formSubmitting.value = false
      }
    }
  })
}

// 统一的数据获取方法
const fetchModels = async () => {
  const category = activeTab.value
  const loading = category === 'llm' ? llmLoading : embeddingLoading
  loading.value = true
  try {
    const res = await llmModelsReq({category})
    if (category === 'llm') {
      llmModels.value = res.data.items
    } else {
      embedModels.value = res.data.items
    }
  } catch (error) {
    ElMessage.error(error.message || `获取${category === 'llm' ? 'LLM' : 'Embedding'}模型列表失败`)
  } finally {
    loading.value = false
  }
}

// 监听标签页切换
watch(activeTab, () => {
  fetchModels()
})

// 生命周期钩子
onMounted(() => {
  fetchModels()
})
</script>


<style lang="scss" scoped>
.model-management {
  padding: 20px;
  height: 100%;
  position: relative;

  .header-actions {
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 1000;
  }

  .model-tabs {
    height: 100%;
  }

  .models-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 10px 0;
  }

  .model-card {
    flex: 1 1 350px;
    min-height: 200px;
    border: 1.5px solid var(--el-border-color);
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    background: white;
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      border-color: var(--el-color-primary);
    }

    .model-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;

      .model-title {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 16px;
        font-weight: 500;
      }
    }

    .model-info {
      margin-bottom: 16px;

      .info-item {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
        color: var(--el-text-color-regular);
        font-size: 14px;

        .el-icon {
          flex-shrink: 0;
          font-size: 16px;
          color: var(--el-color-primary);
        }

        span {
          overflow: hidden;
          text-overflow: ellipsis;
          line-height: 1.5;
          word-break: break-all;
        }
      }
    }

    .model-desc {
      flex-grow: 1;
      font-size: 14px;
      color: var(--el-text-color-secondary);
      margin-bottom: 16px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .model-footer {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      margin-top: auto;
    }
  }
}

:deep(.el-tabs__nav) {
  margin-bottom: 20px;
}
</style>
