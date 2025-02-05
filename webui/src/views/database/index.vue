<template>
  <div class="columnSC" style="width: 100%">
    <div class="rowBC" style="padding: 20px; width: 100%">
      <div class="rowSC" style="font-size: 24px; color: #333333">{{ $t('database.title') }}
        <el-input
            v-model="searchKeyword"
            :placeholder="$t('database.search.placeholder')"
            style="width: 260px; margin-left: 10px"
            size="default"
            @keyup.enter="handleSearch"
        >
          <template #append>
            <el-button size="default" style="color: var(--el-color-primary);" @click="handleSearch">
              <el-icon><Search /></el-icon>
            </el-button>
          </template>
        </el-input>
      </div>
      <el-button ref="addConfigRef" size="default" plain type="primary" @click="onCreateDatabaseClick">
        {{ $t('database.create.button') }}
      </el-button>
    </div>

    <div class="databases-container" style="padding: 10px 20px; width: 100%">
      <el-tooltip
          v-for="item in databaseList"
          :key="item.id"
          :content="item.description || '暂无描述'"
          placement="top"
          :show-after="200"
      >
        <div class="database-container">
          <div>
            <div class="rowBC">
              <span class="title">{{ item.host }}</span>
              <svg
                  v-if="item.db_type === 'oracle'"
                  fill="var(--el-color-primary)" t="1732264008857" class="icon" viewBox="0 0 1034 1024"
                  xmlns="http://www.w3.org/2000/svg"
                  width="36" height="36">
                <path
                    d="M459.69408 837.05856h60.28288l-31.87712-51.28192-58.50112 92.7232h-26.624l71.15776-111.38048c3.09248-4.5056 8.2432-7.2192 13.96736-7.2192 5.5296 0 10.69056 2.62144 13.69088 7.03488l71.43424 111.5648h-26.624l-12.55424-20.71552h-61.0304l-13.32224-20.72576z m276.5824 20.71552V761.0368h-22.59968v106.21952c0 2.90816 1.1264 5.72416 3.2768 7.8848 2.1504 2.1504 5.0688 3.36896 8.25344 3.36896h103.03488l13.312-20.71552H736.26624z m-373.8112-17.33632A39.69024 39.69024 0 0 0 402.2272 800.768a39.77216 39.77216 0 0 0-39.75168-39.75168h-98.84672V878.4896h22.58944v-96.75776h74.752c10.50624 0 18.944 8.54016 18.944 19.0464a18.96448 18.96448 0 0 1-18.944 19.02592l-63.6928-0.1024 67.45088 58.78784h32.80896l-45.3632-38.06208h10.30144z m-237.8752 38.06208a58.71616 58.71616 0 0 1-58.75712-58.68544c0-32.45056 26.3168-58.78784 58.74688-58.78784h68.28032a58.7776 58.7776 0 0 1 58.73664 58.7776 58.69568 58.69568 0 0 1-58.73664 58.69568h-68.28032z m66.7648-20.71552a37.96992 37.96992 0 0 0 38.02112-37.98016 38.05184 38.05184 0 0 0-38.03136-38.06208h-65.24928A38.06208 38.06208 0 0 0 88.064 819.8144a37.98016 37.98016 0 0 0 38.03136 37.96992h65.24928z m429.03552 20.71552a58.73664 58.73664 0 0 1-58.7776-58.68544 58.81856 58.81856 0 0 1 58.7776-58.78784h81.1008l-13.21984 20.71552H621.8752a38.0928 38.0928 0 0 0-38.06208 38.07232 38.01088 38.01088 0 0 0 38.06208 37.96992h81.47968l-13.312 20.71552h-69.66272z m276.29568-20.71552a37.96992 37.96992 0 0 1-36.5568-27.65824h96.5632l13.312-20.72576h-109.8752a38.07232 38.07232 0 0 1 36.5568-27.648h66.28352l13.4144-20.72576h-81.2032a58.81856 58.81856 0 0 0-58.7776 58.7776 58.73664 58.73664 0 0 0 58.7776 58.69568h69.66272l13.312-20.71552h-81.46944zM372.59264 666.6752c-141.9264 0-257.1264-114.8928-257.1264-256.8704 0-141.98784 115.2-257.28 257.1264-257.28h298.8544c141.96736 0 257.0752 115.3024 257.0752 257.28S813.42464 666.6752 671.4368 666.6752H372.59264z m292.20864-90.68544c91.9552 0 166.44096-74.27072 166.44096-166.1952 0-91.904-74.48576-166.58432-166.44096-166.58432h-285.5936c-91.92448 0-166.44096 74.68032-166.44096 166.6048 0 91.904 74.51648 166.17472 166.44096 166.17472h285.5936z"
                />
              </svg>
              <svg
                  v-else-if="item.db_type === 'mysql'"
                  class="icon" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"
                  width="36"
                  height="36">
                <path
                    d="M699.946667 242.176c-4.906667 0-8.234667 0.597333-11.690667 1.408v0.554667h0.597333c2.304 4.437333 6.229333 7.68 9.130667 11.648 2.304 4.565333 4.266667 9.130667 6.570667 13.653333l0.597333-0.64c4.010667-2.816 5.973333-7.338667 5.973333-14.208-1.706667-2.005333-1.962667-4.010667-3.413333-5.973333-1.706667-2.858667-5.376-4.266667-7.68-6.528zM246.186667 805.12h-39.552a2169.770667 2169.770667 0 0 0-11.52-188.16h-0.341334l-60.16 188.16H104.533333l-59.733333-188.16h-0.426667a3110.058667 3110.058667 0 0 0-8.32 188.16H0c2.346667-83.882667 8.192-162.56 17.493333-235.946667h49.066667l56.96 173.397334h0.341333L181.333333 569.173333h46.72c10.325333 85.973333 16.384 164.693333 18.261334 235.946667z m171.392-174.08c-16.128 87.253333-37.376 150.741333-63.658667 190.293333-20.565333 30.549333-43.093333 45.781333-67.541333 45.781334-6.528 0-14.506667-1.962667-24.149334-5.888v-21.077334c4.693333 0.725333 10.24 1.109333 16.469334 1.109334 11.434667 0 20.608-3.2 27.605333-9.472 8.405333-7.68 12.586667-16.298667 12.586667-25.813334 0-6.613333-3.285333-20.053333-9.813334-40.277333L265.813333 631.04h38.826667l31.018667 100.693333c6.997333 22.869333 9.941333 38.826667 8.746666 47.914667 17.066667-45.397333 28.928-95.018667 35.626667-148.608h37.546667z m525.866666 174.08h-112.213333v-235.946667h37.76v206.933334h74.453333z m-141.653333 5.76l-43.349333-21.333333c3.84-3.242667 7.552-6.741333 10.88-10.666667 18.474667-21.589333 27.648-53.674667 27.648-96.128 0-78.08-30.634667-117.162667-91.946667-117.162667-30.037333 0-53.504 9.898667-70.4 29.738667-18.346667 21.674667-27.562667 53.589333-27.562667 95.786667 0 41.472 8.106667 71.936 24.490667 91.306666 14.933333 17.493333 37.418667 26.24 67.541333 26.24 11.264 0 21.589333-1.408 30.933334-4.181333l56.533333 32.938667 15.36-26.538667zM661.333333 757.888c-9.6-15.36-14.378667-40.106667-14.378666-74.069333 0-59.434667 18.090667-89.173333 54.186666-89.173334 18.901333 0 32.853333 7.125333 41.685334 21.333334 9.557333 15.445333 14.336 39.936 14.336 73.514666 0 59.904-18.090667 89.941333-54.186667 89.941334-18.986667 0-32.853333-7.125333-41.728-21.333334z m-70.741333-18.133333c0 20.053333-7.338667 36.522667-22.016 49.322666s-34.261333 19.2-59.050667 19.2c-23.168 0-45.397333-7.338667-67.114666-21.973333l10.112-20.309333c18.688 9.386667 35.541333 13.994667 50.773333 13.994666 14.165333 0 25.301333-3.114667 33.408-9.386666a32.170667 32.170667 0 0 0 12.8-26.24c0-14.08-9.813333-26.026667-27.648-36.053334-16.554667-9.088-49.621333-28.032-49.621333-28.032-18.005333-13.098667-26.965333-27.136-26.965334-50.218666 0-19.2 6.698667-34.56 20.053334-46.293334 13.44-11.861333 30.72-17.706667 52.053333-17.706666 21.845333 0 41.813333 5.802667 59.733333 17.493333l-9.088 20.309333a116.309333 116.309333 0 0 0-45.397333-9.813333c-12.074667 0-21.418667 2.901333-27.904 8.789333a29.226667 29.226667 0 0 0-10.581333 22.357334c0 13.994667 9.984 26.026667 28.416 36.266666 16.768 9.173333 50.645333 28.586667 50.645333 28.586667 18.474667 13.013333 27.648 26.88 27.648 49.834667z"
                    fill="var(--el-color-primary)"/>
                <path
                    d="M990.890667 490.069333c-22.826667-0.597333-40.533333 1.706667-55.338667 8.021334-4.266667 1.706667-11.093333 1.706667-11.690667 7.125333 2.346667 2.261333 2.688 5.973333 4.693334 9.130667 3.413333 5.717333 9.301333 13.354667 14.762666 17.365333 5.973333 4.693333 11.946667 9.216 18.773333 13.226667 6.186667 4.010667 4.010667 12.8 9.088 18.773333 13.354667 3.114667 2.133333 5.12 5.973333 9.130667 7.338666v-0.853333c-1.962667-2.56-2.56-6.272-4.48-9.130667-2.858667-2.858667-5.717333-5.418667-8.533333-8.234666a137.514667 137.514667 0 0 0-29.653334-28.8c-9.130667-6.229333-29.098667-14.933333-32.853333-25.386667l-0.554667-0.597333c6.229333-0.554667 13.653333-2.816 19.626667-4.522667 9.685333-2.56 18.56-2.005333 28.586667-4.522667 4.522667-1.152 9.088-2.56 13.653333-4.010666v-2.56c-5.12-5.12-8.96-12.074667-14.250667-16.853334a378.325333 378.325333 0 0 0-47.104-35.114666c-8.96-5.717333-20.309333-9.386667-29.738666-14.250667-3.413333-1.706667-9.130667-2.56-11.093334-5.418667-5.12-6.229333-8.106667-14.506667-11.733333-21.930666a754.773333 754.773333 0 0 1-23.338667-49.621334c-5.12-11.178667-8.234667-22.314667-14.506666-32.554666-29.44-48.512-61.312-77.909333-110.336-106.666667-10.538667-5.973333-23.168-8.533333-36.522667-11.690667-7.125333-0.341333-14.250667-0.853333-21.333333-1.152-4.693333-2.005333-9.216-7.424-13.226667-10.026666-16.213333-10.24-58.197333-32.426667-70.144-3.072-7.68 18.517333 11.392 36.778667 18.005333 46.165333 4.906667 6.528 11.093333 13.994667 14.506667 21.333333 2.005333 4.949333 2.56 10.026667 4.565333 15.189334 4.522667 12.544 8.832 26.538667 14.805334 38.272 3.114667 5.973333 6.528 12.245333 10.538666 17.621333 2.304 3.114667 6.229333 4.565333 7.125334 9.685333-4.010667 5.802667-4.266667 14.250667-6.570667 21.333334-10.24 32.298667-6.229333 72.234667 8.277333 96 4.565333 7.082667 15.445333 22.784 29.994667 16.768 12.8-5.12 9.984-21.333333 13.653333-35.626667 0.853333-3.413333 0.298667-5.674667 2.048-7.978667v0.64c4.010667 8.021333 8.021333 15.658667 11.690667 23.68 8.789333 13.994667 24.149333 28.501333 36.992 38.186667 6.826667 5.12 12.245333 13.994667 20.778667 17.152v-0.853333h-0.64c-1.834667-2.474667-4.266667-3.669333-6.570667-5.674667a146.986667 146.986667 0 0 1-14.933333-17.066667 373.76 373.76 0 0 1-31.872-51.968c-4.693333-8.96-8.618667-18.602667-12.373334-27.434666-1.706667-3.413333-1.706667-8.533333-4.565333-10.24-4.266667 6.229333-10.538667 11.648-13.653333 19.328-5.418667 12.288-5.973333 27.392-8.021334 43.093333-1.152 0.298667-0.597333 0-1.152 0.597333-9.130667-2.218667-12.245333-11.690667-15.658666-19.626666-8.533333-20.266667-9.941333-52.821333-2.56-76.16 2.005333-5.973333 10.538667-24.832 7.125333-30.549334-1.792-5.418667-7.424-8.533333-10.538667-12.928a105.728 105.728 0 0 1-10.24-18.218666c-6.826667-15.957333-10.24-33.621333-17.664-49.578667-3.413333-7.381333-9.386667-15.104-14.250666-21.888-5.418667-7.68-11.392-13.098667-15.701334-22.186667-1.408-3.114667-3.413333-8.277333-1.152-11.690666 0.597333-2.304 1.792-3.2 4.010667-3.84 3.754667-3.072 14.293333 0.938667 18.005333 2.645333 10.538667 4.266667 19.413333 8.277333 28.245334 14.250667 4.010667 2.816 8.32 8.234667 13.44 9.642666h5.973333c9.130667 2.005333 19.413333 0.597333 27.946667 3.114667 15.146667 4.864 28.8 11.946667 41.045333 19.626667a253.994667 253.994667 0 0 1 88.96 97.536c3.413333 6.570667 4.906667 12.586667 8.021333 19.413333 5.973333 14.08 13.354667 28.288 19.413334 41.898667 5.973333 13.44 11.733333 27.136 20.309333 38.272 4.266667 5.973333 21.418667 9.088 29.098667 12.202666 5.674667 2.56 14.506667 4.906667 19.626666 8.021334 9.813333 5.973333 19.370667 12.8 28.586667 19.370666 4.693333 3.242667 18.901333 10.368 19.754667 16.128z"
                    fill="var(--el-color-primary)"/>
              </svg>
            </div>
            <div class="rowSC wrap" style="width: calc(100% - 20px); font-size: 16px; color: #666666; gap: 10px">
              <div class="database-item">{{ $t('database.info.username') }}：
                <el-tag size="default">{{ item.username }}</el-tag>
              </div>
              <div class="database-item">{{ $t('database.info.port') }}：
                <el-tag size="default">{{ item.port }}</el-tag>
              </div>
              <div class="database-item">{{ item.db_type === 'Oracle' ? $t('database.info.service') : $t('database.info.database') }}：
                <el-tag size="default">{{ item.database }}</el-tag>
              </div>
            </div>
          </div>

          <!-- 操作按钮 -->
          <div class="rowEC" style="margin-top: 10px">
            <el-button type="primary" link @click="handleEdit(item)">{{ $t('database.action.edit') }}</el-button>
            <el-button type="danger" link @click="handleDelete(item)">{{ $t('database.action.delete') }}</el-button>
          </div>
        </div>
      </el-tooltip>
    </div>

    <!-- 分页 -->
    <div class="pagination-container" style="margin-top: auto; padding: 20px;">
      <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :total="total"
          :page-sizes="[10, 20, 50]"
          layout="total, sizes, prev, pager, next"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
      />
    </div>

    <el-dialog 
        v-model="dialogVisible" 
        :title="isEdit ? $t('database.create.edit') : $t('database.create.title')" 
        width="800" 
        destroy-on-close
    >
      <DatabaseConfigForm ref="databaseConfigFormRef" :initial-data="editForm"/>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogVisible = false">{{ $t('database.action.cancel') }}</el-button>
          <el-button type="primary" @click="handleSave">{{ $t('database.action.save') }}</el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import {createDatabaseReq, databaseListReq, deleteDatabaseReq, updateDatabaseReq} from '@/api/database'
import type {DatabaseConfig} from '@/types/database'
import {Search} from '@element-plus/icons-vue'
import {ElMessage, ElMessageBox} from 'element-plus'
import {onMounted, reactive, ref} from 'vue'
import DatabaseConfigForm from "@/components/DatabaseConfigForm.vue"
import {useI18n} from '@/hooks/use-i18n'

const i18n = useI18n()

const databaseList = ref<DatabaseConfig[]>([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(20)
const searchKeyword = ref('')
const dialogVisible = ref(false)
const isEdit = ref(false)
const databaseConfigFormRef = ref()

const editForm = reactive<DatabaseConfig>({
  host: '',
  username: '',
  password: '',
  database: '',
  port: '',
  db_type: '',
  description: ''
})

// 获取数据库列表
const getDatabaseList = async () => {
  try {
    const res = await databaseListReq(pageSize.value, currentPage.value - 1, searchKeyword.value)
    databaseList.value = res.data.data
    total.value = res.data.total
  } catch (error) {
    console.error('获取数据库列表失败:', error)
    ElMessage.error('获取数据库列表失败')
  }
}

// 搜索
const handleSearch = () => {
  currentPage.value = 1
  getDatabaseList()
}

// 分页大小改变
const handleSizeChange = (val: number) => {
  pageSize.value = val
  getDatabaseList()
}

// 当前页改变
const handleCurrentChange = (val: number) => {
  currentPage.value = val
  getDatabaseList()
}

// 创建数据库配置
const onCreateDatabaseClick = () => {
  isEdit.value = false
  Object.assign(editForm, {
    host: '',
    username: '',
    password: '',
    database: '',
    port: '',
    db_type: '',
    description: ''
  })
  dialogVisible.value = true
}

// 编辑数据库配置
const handleEdit = (item: DatabaseConfig) => {
  isEdit.value = true
  Object.assign(editForm, item)
  dialogVisible.value = true
}

// 删除数据库配置
const handleDelete = (item: DatabaseConfig) => {
  ElMessageBox.confirm(
      i18n.t('database.message.deleteConfirm'),
      i18n.t('database.message.warning'),
      {
        confirmButtonText: i18n.t('database.action.confirm'),
        cancelButtonText: i18n.t('database.action.cancel'),
        type: 'warning',
      }
  ).then(async () => {
    try {
      await deleteDatabaseReq(item.id!)
      ElMessage.success(i18n.t('database.message.deleteSuccess'))
      getDatabaseList()
    } catch (error) {
      console.error('删除失败:', error)
      ElMessage.error(i18n.t('database.message.deleteError'))
    }
  })
}

// 保存配置
const handleSave = async () => {
  try {
    if (!databaseConfigFormRef.value) return
    const formData = await databaseConfigFormRef.value.validateForm()
    const saveReq = isEdit.value ? updateDatabaseReq : createDatabaseReq
    await saveReq(formData)
    ElMessage.success(i18n.t(isEdit.value ? 'database.message.updateSuccess' : 'database.message.saveSuccess'))
    dialogVisible.value = false
    getDatabaseList()
  } catch (error) {
    console.error('保存失败:', error)
    if (error !== '表单验证失败') {
      ElMessage.error(i18n.t('database.message.saveError'))
    }
  }
}

onMounted(() => {
  getDatabaseList()
})
</script>

<style lang="scss">

.database-container:hover {
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.04);
  border-color: var(--el-color-primary);
}

.databases-container {
  height: calc(100vh - 180px); /* 减去顶部导航(60px)、标题区域(60px)和分页区域(60px)的高度 */
  overflow-y: auto; /* 内容超出时显示滚动条 */
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.pagination-container {
  display: flex;
  justify-content: flex-start;
  width: 100%;
  border-top: 1px solid #f0f0f0;
  height: 60px; /* 固定分页器高度 */
}
</style>

<style lang="scss">
.database-container {
  border: 1.5px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  background: white;
  min-width: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px;
  width: calc(25% - 10px);
  margin: 0 10px 10px 0;
  transition: all 0.3s ease;

  .title {
    font-size: 16px;
    color: #333333;
  }

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-color: var(--el-color-primary-light-3);
  }
}


</style>
