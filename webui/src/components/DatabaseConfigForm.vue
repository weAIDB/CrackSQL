<template>
  <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      size="large"
      label-width="120px"
      class="demo-ruleForm"
      status-icon
  >
    <el-form-item :label="$t('database.form.host')" prop="host">
      <el-input
          v-model="form.host"
          :placeholder="$t('database.form.hostPlaceholder')"
      />
    </el-form-item>
    <el-form-item :label="$t('database.form.username')" prop="username">
      <el-input
          v-model="form.username"
          :placeholder="$t('database.form.usernamePlaceholder')"
      />
    </el-form-item>
    <el-form-item :label="$t('database.form.password')" prop="password">
      <el-input
          v-model="form.password"
          type="password"
          show-password
          :placeholder="$t('database.form.passwordPlaceholder')"
      />
    </el-form-item>
    <el-form-item :label="$t('database.form.database')" prop="database">
      <el-input
          v-model="form.database"
          :placeholder="$t('database.form.databasePlaceholder')"
      />
    </el-form-item>
    <el-form-item :label="$t('database.form.port')" prop="port">
      <el-input
          v-model="form.port"
          :placeholder="$t('database.form.portPlaceholder')"
      />
    </el-form-item>
    <el-form-item :label="$t('database.form.type')" prop="db_type">
      <el-radio-group v-model="form.db_type">
        <el-radio v-for="item in dbTypes" :key="item.value" :label="item.value">
          {{ item.name }}
        </el-radio>
      </el-radio-group>
    </el-form-item>
    <el-form-item :label="$t('database.form.description')" prop="description">
      <el-input
          v-model="form.description"
          type="textarea"
          :placeholder="$t('database.form.descriptionPlaceholder')"
      />
    </el-form-item>
  </el-form>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue'
import type {FormInstance, FormRules} from 'element-plus'
import {useI18n} from '@/hooks/use-i18n'
import {supportDatabaseReq} from '@/api/database'

const i18n = useI18n()

const props = defineProps({
  initialData: {
    type: Object,
    default: () => ({})
  }
})

const formRef = ref<FormInstance>()
const form = ref({
  host: '',
  username: '',
  password: '',
  database: '',
  port: '',
  db_type: '',
  description: ''
})

const dbTypes = ref([])

const rules = ref<FormRules>({
  host: [{required: true, message: i18n.t('database.rules.host'), trigger: 'blur'}],
  username: [{required: true, message: i18n.t('database.rules.username'), trigger: 'blur'}],
  password: [{required: true, message: i18n.t('database.rules.password'), trigger: 'blur'}],
  database: [{required: true, message: i18n.t('database.rules.database'), trigger: 'blur'}],
  port: [{required: true, message: i18n.t('database.rules.port'), trigger: 'blur'}],
  db_type: [{required: true, message: i18n.t('database.rules.type'), trigger: 'change'}]
})

const validateForm = async () => {
  if (!formRef.value) return
  await formRef.value.validate()
  return form.value
}

defineExpose({
  validateForm
})

onMounted(() => {
  Object.assign(form.value, props.initialData)
  getSupportDatabaseOptions()
})

// 获取支持的数据库类型列表
const getSupportDatabaseOptions = async () => {
  const res = await supportDatabaseReq()
  dbTypes.value = res.data
}

</script>

<style scoped>
.demo-ruleForm {
  max-width: 460px;
}
</style>
