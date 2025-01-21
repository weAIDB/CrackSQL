<template>
  <div class="history-container">
    <!-- 标题区域 -->
    <div class="header-section">
      <h2>改写历史</h2>
      <el-input
          v-if="historyList.length > 0"
          v-model="searchKeyword"
          placeholder="搜索SQL语句"
          style="width: 300px"
          @keyup.enter="handleSearch"
      >
        <template #append>
          <el-button @click="handleSearch">
            <el-icon><Search /></el-icon>
          </el-button>
        </template>
      </el-input>
    </div>

    <!-- 历史记录列表 -->
    <div v-if="historyList.length === 0" class="empty-state">
      <el-empty description="暂无改写记录">
        <template #image>
          <el-icon :size="60" color="#909399"><Document /></el-icon>
        </template>
        <template #description>
          <p>还没有任何SQL改写记录</p>
          <template v-if="searchKeyword">
            <p class="sub-text">没有找到匹配的改写记录</p>
            <el-button @click="clearSearch">清除搜索</el-button>
          </template>
          <template v-else>
            <p class="sub-text">前往首页开始您的第一次SQL改写</p>
            <el-button type="primary" @click="router.push('/')">开始改写</el-button>
          </template>
        </template>
      </el-empty>
    </div>
    <div v-else class="history-list">
      <div v-for="item in historyList" :key="item.id" class="history-item">
        <div class="item-header">
          <div class="left-info">
            <span class="time">{{ formatDate(item.created_at) }}</span>
            <span class="db-type">{{ item.source_db_type }} → {{ item.target_db_type }}</span>
            <span class="target-info">
                 {{ `${item.target_db_user}@${item.target_db_host}:${item.target_db_port}/${item.target_db_database}` }}
               </span>
          </div>
          <div class="right-info">
            <el-tag :type="getStatusType(item.status)" class="status-tag">{{ item.status }}</el-tag>
            <el-button type="primary" link @click="showDetail(item)">详情</el-button>
          </div>
        </div>
        <div class="sql-preview">
          {{ item.original_sql.length > 100 ? item.original_sql.slice(0, 100) + '...' : item.original_sql }}
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

    <!-- 详情对话框 -->
    <el-dialog
        v-model="dialogVisible"
        title="改写详情"
        width="80%"
        destroy-on-close
    >
      <div v-if="currentHistory" class="detail-content">
        <!-- 详情内容 -->
      </div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import {rewriteListReq} from '@/api/rewrite.js'
import type {RewriteHistory} from '@/types/database'
import {Search, Document} from '@element-plus/icons-vue'
import {onMounted, ref} from 'vue'
import { useRouter } from 'vue-router'

const historyList = ref<RewriteHistory[]>([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)
const searchKeyword = ref('')
const dialogVisible = ref(false)
const currentHistory = ref<RewriteHistory | null>(null)
const router = useRouter()

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
          gap: 16px;

          .status-tag {
            min-width: 70px;
            text-align: center;
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
