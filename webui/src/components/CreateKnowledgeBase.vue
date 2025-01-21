<!-- webui/src/components/CreateKnowledgeBase.vue -->
<template>
  <el-dialog
      v-model="dialogVisible"
      title="创建知识库"
      width="80%"
      @close="handleClose"
  >
    <el-form
        ref="formRef"
        size="default"
        :model="form"
        :rules="rules"
        label-width="160px"
        class="knowledge-form"
    >
      <el-form-item label="知识库名称" prop="kb_name">
        <el-input v-model="form.kb_name" placeholder="请输入知识库名称">
          <template #prefix>
            <el-icon><TakeawayBox /></el-icon>
          </template>
        </el-input>
      </el-form-item>

      <el-form-item label="知识库描述" prop="kb_info">
        <el-input
            v-model="form.kb_info"
            type="textarea"
            :rows="3"
            placeholder="请输入知识库描述"
        />
      </el-form-item>

      <el-form-item label="关联的数据库类型" prop="db_type">
        <el-radio-group v-model="form.db_type">
          <el-radio
              v-for="item in dbTypes"
              :key="item.value"
              :label="item.value"
              size="default"
              border
          >
          {{ item.name }}
          </el-radio>
        </el-radio-group>
      </el-form-item>

      <el-divider>
        <el-icon><Setting /></el-icon>
        <span class="ml-2">模型配置</span>
      </el-divider>

      <el-form-item label="向量模型" prop="embedding_model_name">
        <el-select
            v-model="form.embedding_model_name"
            placeholder="请选择向量模型"
            class="w-full"
        >
          <el-option
              v-for="model in embedModels"
              :key="model.name"
              :label="model.name"
              :value="model.name"
          >
            <div style="font-size: 14px;">
              {{ model.name }} / {{ model.dimension }} dim
            </div>
          </el-option>
        </el-select>
      </el-form-item>
    </el-form>

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleClose">取消</el-button>
        <el-button type="primary" @click="handleSubmit" :loading="loading">
          创建
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue'
import { ElMessage } from 'element-plus'
import {
  TakeawayBox,
  Setting,
  Connection
} from '@element-plus/icons-vue'
import { createKnowledgeBaseReq } from '@/api/knowledge'
import { embeddingModelsReq } from '@/api/models'
import { databaseTypesReq } from '@/api/database'
import type { DatabaseTypeOption } from '@/types/database'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:visible', 'created'])

const dialogVisible = computed({
  get: () => props.visible,
  set: (val) => emit('update:visible', val)
})

const formRef = ref()
const embedModels = ref([])
const loading = ref(false)
const dbTypes = ref<DatabaseTypeOption[]>([])

const form = reactive({
  kb_name: '',
  kb_info: '',
  embedding_model_name: '',
  db_type: ''
})

const rules = {
  kb_name: [
    { required: true, message: '请输入知识库名称', trigger: 'blur' },
    { min: 2, max: 50, message: '长度在 2 到 50 个字符', trigger: 'blur' }
  ],
  embedding_model_name: [
    { required: true, message: '请选择向量模型', trigger: 'change' }
  ],
  db_type: [
    { required: true, message: '请选择数据库类型', trigger: 'change' }
  ]
}

const handleClose = () => {
  dialogVisible.value = false
  formRef.value?.resetFields()
}

const handleSubmit = async () => {
  if (!formRef.value) return

  await formRef.value.validate(async (valid) => {
    if (valid) {
      loading.value = true
      try {
        await createKnowledgeBaseReq(form.kb_name, form.kb_info, form.embedding_model_name, form.db_type)
        ElMessage.success('创建成功')
        emit('created')
        handleClose()
      } catch (error) {
        ElMessage.error(error.message || '创建失败')
      } finally {
        loading.value = false
      }
    }
  })
}

const fetchModels = async () => {
  try {
    const res = await embeddingModelsReq()
    embedModels.value = res.data.items
  } catch (error) {
    ElMessage.error(error.message || '获取模型列表失败')
  }
}

const getDbTypes = async () => {
  try {
    const res = await databaseTypesReq()
    dbTypes.value = res.data.types
  } catch (error) {
    console.error('获取数据库类型失败:', error)
    ElMessage.error('获取数据库类型失败')
  }
}

onMounted(() => {
  fetchModels()
  getDbTypes()
})
</script>

<style scoped>
.knowledge-form {
  max-height: 60vh;
  overflow-y: auto;
  padding-right: 20px;
}

.el-select {
  width: 100%;
}

:deep(.el-select-dropdown__item) {
  padding: 8px 12px;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.ml-2 {
  margin-left: 8px;
}

.text-gray-400 {
  color: #9ca3af;
}

.text-sm {
  font-size: 14px;
}

.mt-1 {
  margin-top: 4px;
}

.w-full {
  width: 100%;
}

.rowSC {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

:deep(.el-radio-group) {
  display: flex;
  gap: 20px;
}

:deep(.el-radio.is-bordered) {
  padding: 8px 15px;
  margin-right: 0;
}
</style>
