<template>
  <div class="history-container">
    <!-- 标题区域 -->
    <div class="header-section">
      <h2>{{ $t('history.title') }}</h2>
      <el-input
          v-if="historyList.length > 0"
          v-model="searchKeyword"
          :placeholder="$t('history.search.placeholder')" 
          size="medium"
          style="width: 300px"
          @keyup.enter="handleSearch"
      >
        <template #append>
          <el-button size="medium" @click="handleSearch">
            <el-icon><Search /></el-icon>
          </el-button>
        </template>
      </el-input>
    </div>

    <!-- 历史记录列表 -->
    <div v-if="historyList.length === 0" class="empty-state">
      <el-empty :description="$t('history.empty.title')">
        <template #image>
          <el-icon :size="60" color="#909399"><Document /></el-icon>
        </template>
        <template #description>
          <p>{{ $t('history.empty.description') }}</p>
          <template v-if="searchKeyword">
            <p class="sub-text">{{ $t('history.empty.noResults') }}</p>
            <el-button @click="clearSearch">{{ $t('history.search.clear') }}</el-button>
          </template>
          <template v-else>
            <p class="sub-text">{{ $t('history.empty.subText') }}</p>
            <el-button size="large" type="primary" @click="router.push('/')">
              {{ $t('history.empty.button') }}
            </el-button>
          </template>
        </template>
      </el-empty>
    </div>
    <div v-else class="history-list">
      <div v-for="item in historyList" :key="item.id" class="history-item">
        <div class="item-header">
          <div class="left-info">
            <el-tag :type="getStatusType(item.status)" class="status-tag">
              {{ $t(`history.status.${item.status.toLowerCase()}`) }}
            </el-tag>
            <span class="time">{{ formatDate(item.created_at) }}</span>
            <span class="duration rowSC" v-if="item.duration">
              <el-icon><Timer /></el-icon>
              <span style="margin-left: 5px;">{{ item.duration }}</span>
            </span>
            <span class="db-type">{{ item.source_db_type }} → {{ item.target_db.db_type }}</span>
            <span class="target-info">
              {{ `${item.target_db.username}@${item.target_db.host}:${item.target_db.port}/${item.target_db.database}` }}
            </span>
          </div>
          <div class="right-info">
            <el-popconfirm
              v-if="item.status !== 'processing'"
              width="300px"
              :title="$t('history.delete.confirm')"
              @confirm="confirmDelete(item)"
              :confirm-button-text="$t('common.confirm')"
              :cancel-button-text="$t('common.cancel')"
              confirm-button-type="danger"
            >
              <template #reference>
                <el-button 
                  type="danger" 
                  :title="$t('history.list.delete')"
                >
                  <el-icon><Delete /></el-icon>
                </el-button>
              </template>
            </el-popconfirm>
            <el-button type="success" @click="showDetail(item)">
              {{ $t('history.list.detail') }}
            </el-button>
            <el-button 
              type="primary" 
              link
              @click="toggleExpand(item.id)"
              :title="expandedItems.has(item.id) ? $t('history.list.collapse') : $t('history.list.expand')"
            >
              <el-icon>
                <component :is="expandedItems.has(item.id) ? ArrowUp : ArrowDown" />
              </el-icon>
            </el-button>
          </div>
        </div>
        <div class="sql-preview" v-if="!expandedItems.has(item.id)">
          {{ item.original_sql.length > 100 ? item.original_sql.slice(0, 100) + '...' : item.original_sql }}
        </div>
        <div v-else class="expanded-sql">
          <sql-input
            :message="{
              source_db_type: item.source_db_type,
              original_sql: item.original_sql,
              target_db: item.target_db,
              created_at: item.created_at,
              llm_model_name: item.llm_model_name,
              original_kb: item.original_kb,
              target_kb: item.target_kb
            }"
          />
        </div>
      </div>
    </div>

    <!-- 分页 -->
    <div v-if="historyList.length > 0" class="pagination-section">
      <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :page-sizes="[10, 20, 50]"
          :total="total"
          layout="total, sizes, prev, pager, next"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import {rewriteListReq, deleteRewriteReq} from '@/api/rewrite.js'
import type {RewriteHistory} from '@/types/database'
import {Search, Document, Delete, Timer, ArrowDown, ArrowUp} from '@element-plus/icons-vue'
import {onMounted, ref} from 'vue'
import {useRouter} from 'vue-router'
import {useI18n} from '@/hooks/use-i18n'
import { ElMessage } from 'element-plus'
import SqlInput from '@/components/SqlInput.vue'

const i18n = useI18n()
const historyList = ref<RewriteHistory[]>([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)
const searchKeyword = ref('')
const currentHistory = ref<RewriteHistory | null>(null)
const router = useRouter()
const expandedItems = ref<Set<string>>(new Set())

// 获取历史列表
const getHistoryList = async () => {
  try {
    const res = await rewriteListReq(pageSize.value, currentPage.value - 1, searchKeyword.value)
    historyList.value = res.data.data
    total.value = res.data.total
  } catch (error) {
    console.error('获取历史列表失败:', error)
  }
}

// 搜索
const handleSearch = () => {
  currentPage.value = 1
  getHistoryList()
}

// 分页处理
const handleSizeChange = (val: number) => {
  pageSize.value = val
  getHistoryList()
}

const handleCurrentChange = (val: number) => {
  currentPage.value = val
  getHistoryList()
}

// 格式化日期
const formatDate = (date: string) => {
  return new Date(date).toLocaleString()
}

// 获取状态标签类型
const getStatusType = (status: string) => {
  const types = {
    success: 'success',
    failed: 'danger',
    processing: 'warning'
  }
  return types[status as keyof typeof types]
}

// 显示详情
const showDetail = async (row: RewriteHistory) => {
  router.push(`/history/${row.id}`)
}

// 清除搜索
const clearSearch = () => {
  searchKeyword.value = ''
  getHistoryList()
}

// 确认删除
const confirmDelete = async (row: RewriteHistory) => {
  try {
    const res = await deleteRewriteReq(row.id)
    if (res.code === 0) {
      ElMessage.success(i18n.t('history.delete.success'))
      getHistoryList()
    } else {
      ElMessage.error(res.msg || i18n.t('history.delete.error'))
    }
  } catch (error) {
    console.error('删除历史记录失败:', error)
    ElMessage.error(i18n.t('history.delete.error'))
  }
}

// 处理展开/收起
const toggleExpand = (id: string) => {
  if (expandedItems.value.has(id)) {
    expandedItems.value.delete(id)
  } else {
    expandedItems.value.add(id)
  }
}

onMounted(() => {
  getHistoryList()
})
</script>

<style lang="scss" scoped>
.history-container {
  padding: 20px;
  overflow: hidden;
  height: calc(100vh - 30px);
  .header-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .history-list {
    overflow-y: scroll;
    height: calc(100% - 100px);
    .history-item {
      background: white;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 16px;
      box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.05);
      transition: all 0.3s ease;

      &:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px 0 rgba(0, 0, 0, 0.1);
      }

      .item-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;

        .left-info {
          display: flex;
          align-items: center;
          gap: 16px;
          color: #666;
          font-size: 14px;

          .time {
            color: #333;
            font-weight: 500;
          }

          .duration {
            display: flex;
            align-items: center;
            gap: 4px;
            color: #666;
            font-size: 13px;
            background-color: #f5f7fa;
            padding: 4px 8px;
            border-radius: 4px;
          }

          .db-type {
            color: var(--el-color-primary);
          }

          .target-info {
            color: #888;
            font-family: monospace;
          }
        }

        .right-info {
          display: flex;
          align-items: center;
          gap: 10px;

          .el-button.is-link {
            padding: 4px;
            height: 32px;
            width: 32px;
            border-radius: 4px;
            
            &:hover {
              background-color: var(--el-color-primary-light-9);
            }
            
            .el-icon {
              font-size: 16px;
            }
          }
        }
      }

      .sql-preview {
        font-family: monospace;
        background: #f8f9fa;
        padding: 12px;
        border-radius: 4px;
        color: #444;
        font-size: 14px;
        line-height: 1.5;
        white-space: pre-wrap;
      }

      .expanded-sql {
        margin-top: 12px;
        
        :deep(.sql-input-container) {
          background-color: #ffffff;
          margin: 0;
          
          .el-descriptions {
            --el-text-color-regular: #333333;
            --el-border-color: #e4e7ed;
            --el-fill-color-blank: #ffffff;
            
            .el-descriptions__body {
              .el-descriptions__table {
                .el-descriptions__cell {
                  background-color: #ffffff;
                }
                
                .el-descriptions__label {
                  color: #606266;
                  background-color: #f5f7fa;
                }
                
                .el-descriptions__content {
                  color: #333333;
                }
              }
            }
          }

          .connection-info {
            color: #333333;
            background-color: #f5f7fa;
          }

          .sql-section {
            background-color: #f5f7fa;
            border: 1px solid #e4e7ed;
            
            pre {
              code {
                color: #333333;
              }
            }
          }
        }
      }
    }
  }

  .pagination-section {
    display: flex;
    justify-content: flex-start;
    margin-top: 20px;
  }
}

.empty-state {
  height: calc(100vh - 200px);
  display: flex;
  align-items: center;
  justify-content: center;

  .sub-text {
    color: #909399;
    font-size: 14px;
    margin: 8px 0;
  }
}
</style>
