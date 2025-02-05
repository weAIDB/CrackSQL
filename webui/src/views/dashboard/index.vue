<template>
  <div class="dashboard-container">
    <!-- 顶部标题区域 -->
    <div class="header-section">
      <div class="header-content">
        <div class="title-area" id="welcome">
          <h1>{{ $t('dashboard.title') }}</h1>
          <p>{{ $t('dashboard.subtitle') }}</p>
        </div>
        <a id="github" href="https://github.com/your-repo" target="_blank" class="github-link">
          <el-icon>
            <Link/>
          </el-icon>
          {{ $t('dashboard.github') }}
        </a>
      </div>
    </div>

    <!-- 主要操作区域 -->
    <div class="main-section">
      <!-- 左侧功能介绍 -->
      <div class="features-panel">
        <div class="feature-card">
          <el-icon class="feature-icon">
            <Connection/>
          </el-icon>
          <h3>{{ $t('dashboard.features.database.title') }}</h3>
          <p>{{ $t('dashboard.features.database.desc') }}</p>
        </div>
        <div class="feature-card">
          <el-icon class="feature-icon">
            <Monitor/>
          </el-icon>
          <h3>{{ $t('dashboard.features.conversion.title') }}</h3>
          <p>{{ $t('dashboard.features.conversion.desc') }}</p>
        </div>
        <div class="feature-card">
          <el-icon class="feature-icon">
            <Document/>
          </el-icon>
          <h3>{{ $t('dashboard.features.validation.title') }}</h3>
          <p>{{ $t('dashboard.features.validation.desc') }}</p>
        </div>
      </div>

      <!-- 右侧操作面板 -->
      <div class="operation-panel">
        <!-- 数据库选择区域 -->
        <div class="database-selector">
          <div id="source-db" class="source-db" style="width: 30%!important;">
            <label>{{ $t('dashboard.operation.sourceDb.label') }}</label>
            <el-select
                v-model="originalDB"
                class="db-select"
                size="large"
                :placeholder="$t('dashboard.operation.sourceDb.placeholder')"
            >
              <el-option
                  v-for="item in databaseOptions"
                  :key="item"
                  :label="item"
                  :value="item"
              />
            </el-select>
          </div>

          <div id="target-db" class="target-db" style="width: 70%">
            <label>{{ $t('dashboard.operation.targetDb.label') }}</label>
            <el-select
                v-model="targetDB"
                class="db-select"
                size="large"
                :placeholder="$t('dashboard.operation.targetDb.placeholder')"
                popper-class="target-db-dropdown"
            >
              <template #header>
                <div class="db-select-header">
                  <el-input
                      v-model="searchKeyword"
                      :placeholder="$t('dashboard.operation.targetDb.search')"
                      :prefix-icon="Search"
                      size="default"
                      @keyup.enter="handleSearch"
                  />
                  <el-button
                      type="primary"
                      size="default"
                      @click="showAddDatabaseDialog"
                  >
                    {{ $t('dashboard.operation.targetDb.add') }}
                  </el-button>
                </div>
              </template>
              <el-option
                  v-for="item in targetDBList"
                  :key="item.id"
                  :label="`${item.db_type}-${item.username}@${item.host}:${item.port}/${item.database}`"
                  :value="item.id"
              >
                <div class="db-option">
                  <span class="db-type">{{ item.db_type }}</span>
                  <span class="db-info">{{ `${item.username}@${item.host}:${item.port}/${item.database}` }}</span>
                </div>
              </el-option>
            </el-select>
          </div>
        </div>

        <!-- SQL输入区域 -->
        <div class="sql-input">
          <el-input
              id="sql-input"
              v-model="userInput"
              type="textarea"
              rows="auto"
              :placeholder="$t('dashboard.operation.sql.placeholder')"
          />
          <el-button
              id="convert-btn"
              type="primary"
              size="large"
              :disabled="sendBtnDisabled"
              @click="onSendClick"
              style="margin: 20px 0"
          >
            {{ $t('dashboard.operation.convert') }}
          </el-button>
        </div>
      </div>
    </div>

    <!-- 添加数据库配置对话框 -->
    <el-dialog
        v-model="addDatabaseDialogVisible"
        :title="$t('dashboard.dialog.add.title')"
        width="800px"
        destroy-on-close
    >
      <DatabaseConfigForm ref="databaseConfigFormRef" :initial-data="editForm"/>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="addDatabaseDialogVisible = false">
            {{ $t('dashboard.dialog.add.cancel') }}
          </el-button>
          <el-button type="primary" @click="onSaveClick">
            {{ $t('dashboard.dialog.add.confirm') }}
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts" name="Index">
import {createDatabaseReq, databaseListReq} from '@/api/database'
import {createRewriteReq} from '@/api/rewrite.js'
import DatabaseConfigForm from '@/components/DatabaseConfigForm.vue';
import type {DatabaseConfig} from "@/types/database";
import {Connection, Document, Link, Monitor, Search} from '@element-plus/icons-vue'
import {ElMessage} from "element-plus";
import {computed, onMounted, reactive, ref} from 'vue'
import {useRouter} from 'vue-router'
import {useI18n} from 'vue-i18n'

const i18n = useI18n()

// 数据库类型选项
const databaseOptions = ["MySql", "PostgreSQL", "Oracle"]

const userInput = ref('')
const databaseConfigFormRef = ref()

const sendBtnDisabled = computed(() => {
  return userInput.value === '' || targetDB.value === '' || originalDB.value === ''
})

const sendBtnDisabledText = computed(() => {
  if (userInput.value === '') {
    return i18n.t('dashboard.operation.validation.noSql')
  }
  if (originalDB.value === '') {
    return i18n.t('dashboard.operation.validation.noSource')
  }
  if (targetDB.value === '') {
    return i18n.t('dashboard.operation.validation.noTarget')
  }
})

const router = useRouter()

const originalDB = ref("Oracle")
const targetDB = ref("")
const targetDBList = ref<DatabaseConfig[]>([])
const total = ref(0)

const editForm = reactive<DatabaseConfig>({
  host: '',
  username: '',
  password: '',
  database: '',
  port: '',
  db_type: '',
  description: ''
});

const addDatabaseDialogVisible = ref(false)

const showAddDatabaseDialog = () => {
  addDatabaseDialogVisible.value = true
}

const searchKeyword = ref('')

// 搜索处理
const handleSearch = () => {
  getDatabaseList()
}

// 修改获取数据库列表方法
const getDatabaseList = async () => {
  try {
    const res = await databaseListReq(100, 0, searchKeyword.value)  // 带搜索关键字获取配置
    targetDBList.value = res.data.data
    total.value = res.data.total
  } catch (error) {
    console.error('获取数据库列表失败:', error)
    ElMessage.error('获取数据库列表失败')
  }
}

onMounted(() => {
  // 获取数据库配置列表
  getDatabaseList()
});

const onSendClick = async () => {
  try {
    // 获取选中的目标数据库配置
    const targetConfig = targetDBList.value.find(item => item.id === Number.parseInt(targetDB.value))
    if (!targetDB.value) {
      ElMessage.error('请选择目标数据库')
      return
    }
    // 构造创建改写历史的参数
    const data = {
      source_db_type: originalDB.value,
      original_sql: userInput.value,
      target_db_type: targetConfig.db_type,
      target_db_user: targetConfig.username,
      target_db_host: targetConfig.host,
      target_db_port: targetConfig.port,
      target_db_password: targetConfig.password,
      target_db_database: targetConfig.database,
      target_db_id: targetConfig.id
    }

    // 创建改写历史
    await createRewriteReq(data)

    // 跳转到chat页面
    router.push('/chat')

  } catch (error) {
    console.error('创建改写历史失败:', error)
  }
}

// 保存数据库配置
const onSaveClick = async () => {
  try {
    if (!databaseConfigFormRef.value) return
    const formData = await databaseConfigFormRef.value.validateForm()
    await createDatabaseReq(formData)
    ElMessage.success('创建成功')
    getDatabaseList()  // 刷新列表
    addDatabaseDialogVisible.value = false  // 关闭对话框
  } catch (error) {
    console.error('保存失败:', error)
    if (error !== '表单验证失败') {
      ElMessage.error('保存失败')
    }
  }
}

</script>

<style lang="scss" scoped>
.dashboard-container {
  min-height: calc(100vh - 30px);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.1) 100%),
  linear-gradient(to right, #f6f7f9 0%, #eef1f5 100%);
  background-size: cover;
  padding: 40px;
  display: flex;
  flex-direction: column;
  gap: 40px;
  position: relative;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 400px;
    background: linear-gradient(135deg, var(--el-color-primary-light-8) 0%, var(--el-color-primary-light-5) 100%);
    opacity: 0.1;
    z-index: 0;
  }
}

.header-section {
  position: relative;
  z-index: 1;

  .header-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
  }

  .title-area {
    text-align: left;
  }

  h1 {
    font-size: 2.5em;
    color: var(--el-color-primary);
    margin-bottom: 16px;
    font-weight: 600;
  }

  p {
    font-size: 1.2em;
    color: #666;
  }

  .github-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 24px;
    border-radius: 6px;
    background: #24292e;
    color: white;
    text-decoration: none;
    font-size: 0.9em;
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
  }
}

.main-section {
  display: flex;
  gap: 40px;
  flex: 1;
}

.features-panel {
  width: 30%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  position: relative;
  z-index: 1;

  .feature-card {
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
    transition: transform 0.3s ease;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }

    .feature-icon {
      font-size: 24px;
      color: var(--el-color-primary);
      margin-bottom: 16px;
    }

    h3 {
      font-size: 1.1em;
      margin-bottom: 12px;
      color: #333;
    }

    p {
      font-size: 1em;
      color: #666;
      line-height: 1.6;
    }
  }
}

.operation-panel {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.database-selector {
  display: flex;
  align-items: center;
  gap: 24px;

  .source-db,
  .target-db {
    label {
      display: block;
      margin-bottom: 8px;
      color: #333;
      font-weight: 500;
    }

    .db-select {
      width: 100%;
    }
  }
}

.sql-input {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 100%;

  .el-textarea {
    flex: 1;
    display: flex;
  }

  :deep(.el-textarea__inner) {
    flex: 1;
    border: 1px solid #e4e7ed;
    border-radius: 8px;
    padding: 16px;
    font-family: 'Monaco', monospace;

    &:focus {
      border-color: var(--el-color-primary);
    }
  }

  .el-button {
    align-self: flex-end;
    padding: 12px 40px;
    margin-top: 20px;
  }
}

.db-select-header {
  padding: 16px;
  display: flex;
  gap: 12px;
  border-bottom: 1px solid #e4e7ed;
}

.db-option {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;

  .db-type {
    font-weight: bold;
  }

  .db-info {
    font-weight: lighter;
  }
}
</style>
