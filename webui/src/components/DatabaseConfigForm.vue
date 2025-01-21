<template>
  <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      label-width="120px"
      size="large"
      inline
  >
    <el-form-item label="数据库类型" prop="db_type">
      <el-radio-group v-model="form.db_type">
        <el-radio
            v-for="item in dbTypeOptions"
            :key="item.value"
            :label="item.value"
            size="large"
            border
        >
          {{ item.name }}
        </el-radio>
      </el-radio-group>
    </el-form-item>

    <el-form-item label="主机地址" prop="host">
      <el-input
          v-model="form.host"
          style="width: 300px"
          size="large"
          placeholder="请输入主机地址"
      />
    </el-form-item>

    <el-form-item label="用户名" prop="username">
      <el-input
          v-model="form.username"
          style="width: 300px"
          size="large"
          placeholder="请输入用户名"
      />
    </el-form-item>

    <el-form-item label="密码" prop="password">
      <el-input
          v-model="form.password"
          style="width: 300px"
          size="large"
          type="password"
          show-password
          placeholder="请输入密码"
      />
    </el-form-item>

    <el-form-item
        :label="form.db_type === 'oracle' ? 'service' : '数据库名称'"
        prop="database"
    >
      <el-input
          v-model="form.database"
          style="width: 300px"
          size="large"
          :placeholder="form.db_type === 'oracle' ? '请输入service' : '请输入数据库名称'"
      />
    </el-form-item>

    <el-form-item label="端口" prop="port">
      <el-input
          v-model.number="form.port"
          style="width: 300px"
          size="large"
          placeholder="请输入端口号"
      />
    </el-form-item>

    <el-form-item label="描述" prop="description">
      <el-input
          type="textarea"
          :rows="3"
          v-model="form.description"
          style="width: 680px"
          size="large"
          placeholder="请输入配置描述"
      />
    </el-form-item>
  </el-form>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import type { FormInstance } from 'element-plus'
import type { DatabaseConfig, DatabaseTypeOption } from '@/types/database'
import { databaseTypesReq } from '@/api/database'

const props = defineProps<{
  initialData?: Partial<DatabaseConfig>
}>()

const formRef = ref<FormInstance>()
const dbTypeOptions = ref<DatabaseTypeOption[]>([])

// 表单数据
const form = reactive<DatabaseConfig>({
  host: '',
  port: '',
  database: '',
  username: '',
  password: '',
  db_type: '',
  description: ''
})

// 表单验证规则
const rules = {
  host: [
    { required: true, message: '请输入主机地址', trigger: 'blur' },
    { min: 1, max: 128, message: '长度在 1 到 128 个字符', trigger: 'blur' }
  ],
  port: [
    { required: true, message: '请输入端口号', trigger: 'blur' },
    { type: 'number', message: '端口必须为数字', trigger: 'blur' },
    {
      validator: (rule: any, value: number, callback: any) => {
        if (value < 1 || value > 65535) {
          callback(new Error('端口号必须在 1-65535 之间'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
  ],
  database: [
    { required: true, message: '请输入数据库名称', trigger: 'blur' },
    { min: 1, max: 64, message: '长度在 1 到 64 个字符', trigger: 'blur' }
  ],
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 1, max: 64, message: '长度在 1 到 64 个字符', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 1, max: 256, message: '长度在 1 到 256 个字符', trigger: 'blur' }
  ],
  db_type: [
    { required: true, message: '请选择数据库类型', trigger: 'change' }
  ],
  description: [
    { max: 256, message: '长度不能超过 256 个字符', trigger: 'blur' }
  ]
}

// 获取数据库类型选项
const getDbTypes = async () => {
  try {
    const res = await databaseTypesReq()
    dbTypeOptions.value = res.data.types
  } catch (error) {
    console.error('获取数据库类型失败:', error)
  }
}

// 表单验证方法
const validateForm = async (): Promise<DatabaseConfig> => {
  if (!formRef.value) throw new Error('表单实例不存在')
  const valid = await formRef.value.validate()
    .catch(() => false)
  
  if (!valid) {
    return Promise.reject('表单验证失败')
  }
  
  return { ...form }
}

// 暴露方法给父组件
defineExpose({
  validateForm
})

// 初始化表单数据
const initForm = () => {
  if (props.initialData) {
    Object.assign(form, props.initialData)
  }
}

onMounted(() => {
  getDbTypes()
  initForm()
})
</script>

<style lang="scss" scoped>
.el-form {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;

  .el-form-item {
    margin-bottom: 0;

    &:first-child, &:last-child {
      width: 100%;
    }
  }
}

:deep(.el-radio-group) {
  display: flex;
  gap: 20px;
}

:deep(.el-form-item__label) {
  font-weight: 500;
}
</style>
