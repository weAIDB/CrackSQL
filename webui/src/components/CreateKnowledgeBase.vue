<!-- webui/src/components/CreateKnowledgeBase.vue -->
<template>
  <el-dialog
      v-model="dialogVisible"
      :title="$t('knowledge.create.title')"
      width="80%"
      :close-on-click-modal="false"
      @close="handleClose"
  >
    <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        class="demo-ruleForm"
        status-icon
    >
      <el-form-item :label="$t('knowledge.create.form.name')" prop="kb_name">
        <el-input
            v-model="form.kb_name"
            :placeholder="$t('knowledge.create.form.namePlaceholder')"
        />
      </el-form-item>
      <el-form-item :label="$t('knowledge.create.form.description')" prop="kb_info">
        <el-input
            v-model="form.kb_info"
            type="textarea"
            :placeholder="$t('knowledge.create.form.descriptionPlaceholder')"
        />
      </el-form-item>
      <el-form-item :label="$t('knowledge.create.form.embeddingModel')" prop="embedding_model_name">
        <el-select
            v-model="form.embedding_model_name"
            class="m-2"
            :placeholder="$t('knowledge.create.form.embeddingModelPlaceholder')"
            style="width: 100%"
        >
          <el-option
              v-for="item in embeddingModelList"
              :key="item.name"
              :label="item.name"
              :value="item.name"
          >
            <div class="rowSC" style="width: 100%">
              <span>{{ item.name }}</span>
              <span style="color: #999999">{{ $t('knowledge.create.form.dimension') }}: {{ item.dimension }}</span>
            </div>
          </el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleClose">{{ $t('common.cancel') }}</el-button>
        <el-button type="primary" @click="onSubmit" :loading="loading">
          {{ $t('knowledge.create.submit') }}
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import {ref, watch} from 'vue'
import type {FormInstance, FormRules} from 'element-plus'
import {ElMessage} from 'element-plus'
import {embeddingModelsReq} from '@/api/models'
import {createKnowledgeBaseReq} from '@/api/knowledge'
import {useI18n} from '@/hooks/use-i18n'

const i18n = useI18n()

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:visible', 'created'])

const dialogVisible = ref(false)
const loading = ref(false)
const formRef = ref<FormInstance>()
const embeddingModelList = ref([])

const form = ref({
  kb_name: '',
  kb_info: '',
  embedding_model_name: ''
})

const rules = ref<FormRules>({
  kb_name: [
    {required: true, message: i18n.t('knowledge.create.rules.nameRequired'), trigger: 'blur'},
    {min: 2, max: 50, message: i18n.t('knowledge.create.rules.nameLength'), trigger: 'blur'}
  ],
  embedding_model_name: [
    {required: true, message: i18n.t('knowledge.create.rules.embeddingRequired'), trigger: 'change'}
  ]
})

watch(() => props.visible, (val) => {
  dialogVisible.value = val
})

watch(() => dialogVisible.value, (val) => {
  emit('update:visible', val)
})

const getEmbeddingModelList = async () => {
  try {
    const res = await embeddingModelsReq()
    embeddingModelList.value = res.data.items
  } catch (error) {
    ElMessage.error(i18n.t('knowledge.create.fetchError'))
  }
}

const handleClose = () => {
  dialogVisible.value = false
  formRef.value?.resetFields()
}

const onSubmit = async () => {
  if (!formRef.value) return
  await formRef.value.validate(async (valid) => {
    if (valid) {
      loading.value = true
      try {
        await createKnowledgeBaseReq(
          form.value.kb_name,
          form.value.kb_info,
          form.value.embedding_model_name
        )
        ElMessage.success(i18n.t('knowledge.create.success'))
        handleClose()
        emit('created')
      } catch (error) {
        ElMessage.error(i18n.t('knowledge.create.error'))
      } finally {
        loading.value = false
      }
    }
  })
}

getEmbeddingModelList()
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
