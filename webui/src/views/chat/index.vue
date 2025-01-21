<template>
  <div v-if="!historyDetail" class="empty-state">
    <el-empty description="暂无改写记录">
      <template #image>
        <el-icon :size="60" color="#909399"><ChatDotSquare /></el-icon>
      </template>
      <template #description>
        <p>还没有任何SQL改写记录</p>
        <p class="sub-text">前往首页开始您的第一次SQL改写</p>
      </template>
      <el-button type="primary" @click="router.push('/')">开始改写</el-button>
    </el-empty>
  </div>
  <div v-else class="relative columnSC detail-container">
    <!-- 头部信息 -->
    <div class="header">
      <div class="header-item rowBC" style="width: 100%; height: 35px">
        <div class="rowSC">
          <span style="margin-right: 10px; font-weight: bold; color: #333333">{{ historyDetail.source_db_type }}</span>
          <svg
              class="icon"
              viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20">
            <path
                d="M122.368 887.296c-15.872 0-32.256-6.144-44.544-18.432-24.576-24.576-24.576-64.512 0-89.088L280.064 527.36 77.824 274.944c-24.576-24.576-24.576-64.512 0-89.088 24.576-24.576 64.512-24.576 89.088 0l297.472 296.96c11.776 11.776 18.432 27.648 18.432 44.544 0 16.896-6.656 32.768-18.432 44.544l-297.472 296.96c-12.288 12.288-28.16 18.432-44.544 18.432z"
                fill="#6CA9E5"/>
            <path
                d="M375.296 887.296c-21.504 0-42.496-11.264-54.272-30.72-14.848-24.576-10.752-56.32 9.216-76.8L583.68 527.36 330.752 274.944c-20.48-20.48-24.576-52.224-9.216-76.8 14.848-24.576 44.544-36.352 72.192-27.648l524.288 296.96c26.624 8.192 44.544 32.256 44.544 59.904 0 27.648-17.92 52.224-44.544 59.904l-524.288 296.96c-6.144 2.048-12.288 3.072-18.432 3.072z"
                fill="#4C91E5"/>
          </svg>
          <span style="margin-left: 10px; font-weight: bold; color: #333333">{{ historyDetail.target_db_type }}</span>
        </div>
        <div class="rowSC">
          <el-tag :type="getStatusType(historyDetail.status)" style="margin-right: 20px">
            {{ historyDetail.status }}
          </el-tag>
          <div style="color: #666666; font-size: 14px;">
            {{ formatDate(historyDetail.created_at) }}
          </div>
        </div>
      </div>
    </div>

    <!-- 消息列表 -->
    <div ref="messagesScrollDiv" class="messages-container">
      <!-- 用户输入的SQL -->
      <chat-item
          :message="{
            role: 'user',
            content: formatUserMessage(historyDetail),
            time: historyDetail.created_at,
            loading: false
      }"/>

      <!-- 改写过程 -->
      <chat-item
          v-for="process in historyDetail.processes"
          :key="process.id"
          :message="{
                  role: process.role || 'assistant',
                  content: process.step_content,
                  time: process.created_at,
                  loading: false
                }"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import {rewriteLatestReq} from '@/api/rewrite.js'
import ChatItem from '@/components/ChatItem.vue'
import type {RewriteHistory} from '@/types/database'
import {onMounted, ref} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import {formatDate, formatUserMessage, getStatusType} from '@/utils/rewrite'

const route = useRoute()
const router = useRouter()

const historyDetail = ref<RewriteHistory | null>(null)
const messagesScrollDiv = ref<HTMLElement | null>(null)

// 获取改写详情
const getRewriteDetail = async () => {
  try {
    const res = await rewriteLatestReq()
    historyDetail.value = res.data
  } catch (error) {
    console.error('获取改写详情失败:', error)
  }
}

onMounted(() => {
  getRewriteDetail()
})
</script>

<style lang="scss" scoped>
.detail-container {
  height: calc(100vh - 40px);
  overflow: hidden;

  .header {
    width: 100%;
    border-bottom: 1px solid #eeeeee;
    padding: 10px 20px;
  }

  .messages-container {
    flex: 1;
    width: 100%;
    overflow-y: auto;
    padding: 20px;
  }
}

.empty-state {
  height: 100%;
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
