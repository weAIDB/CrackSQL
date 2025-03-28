<template>
  <div v-if="!historyDetail" v-loading="!historyDetail" class="rowCC" style="height: 100%; width: 100%;">
    {{ $t('history.list.loading') }}
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
          <span style="margin-left: 10px; font-weight: bold; color: #333333">{{ historyDetail.target_db.db_type }}</span>
        </div>
        <div class="rowSC">
          <el-tag :type="getStatusType(historyDetail.status)" style="margin-right: 20px">
            {{ $t(`history.status.${historyDetail.status.toLowerCase()}`) }}
          </el-tag>
          <div style="color: #666666; font-size: 14px;">
            {{ formatDate(historyDetail.created_at) }}
          </div>
          <div v-if="historyDetail.duration" class="rowSC" style="color: #666666; font-size: 14px; margin-left: 20px;">
            <el-icon><Timer /></el-icon>
            <span style="margin-left: 5px;">Duration: {{ historyDetail.duration }}</span>
          </div>
          <el-button style="margin-left: 20px;" v-if="historyDetail.status === 'processing'" type="danger" @click="stopRewrite">
            {{ $t('chat.operation.stop') }}
          </el-button>
        </div>
      </div>
    </div>

    <!-- 消息列表 -->
    <div ref="messagesScrollDiv" class="messages-container">
      <!-- 用户输入的SQL -->
      <sql-input
          :message="{
            source_db_type: historyDetail.source_db_type,
            original_sql: historyDetail.original_sql,
            target_db: historyDetail.target_db,
            created_at: historyDetail.created_at,
            llm_model_name: historyDetail.llm_model_name,
            original_kb: historyDetail.original_kb,
            target_kb: historyDetail.target_kb
          }"
      />

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
import {rewriteDetailReq, stopRewriteReq} from '@/api/rewrite.js'
import ChatItem from '@/components/ChatItem.vue'
import type {RewriteHistory} from '@/types/database'
import {onMounted, ref, onUnmounted} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import {formatDate, formatUserMessage, getStatusType} from '@/utils/rewrite'
import {useI18n} from '@/hooks/use-i18n'
import {Timer} from '@element-plus/icons-vue'
import SqlInput from '@/components/SqlInput.vue'
const route = useRoute()
const router = useRouter()
const i18n = useI18n()

const historyDetail = ref<RewriteHistory | null>(null)
const messagesScrollDiv = ref<HTMLElement | null>(null)
const pollTimer = ref<number | null>(null)

// 获取改写详情
const getRewriteDetail = async () => {
  try {
    const res = await rewriteDetailReq(Number(route.params.id))
    historyDetail.value = res.data
    
    if (historyDetail.value?.status === 'processing') {
      startPolling()
    } else {
      stopPolling()
    }
  } catch (error) {
    console.error('获取改写详情失败:', error)
    stopPolling()
  }
}

// 停止改写
const stopRewrite = async () => {
  try {
    await stopRewriteReq({id: historyDetail.value?.id})
    getRewriteDetail()
  } catch (error) {
    console.error('停止改写失败:', error)
  }
}

// 开始轮询
const startPolling = () => {
  if (!pollTimer.value) {
    pollTimer.value = window.setInterval(() => {
      getRewriteDetail()
    }, 3000)
  }
}

// 停止轮询
const stopPolling = () => {
  if (pollTimer.value) {
    clearInterval(pollTimer.value)
    pollTimer.value = null
  }
}

onMounted(() => {
  getRewriteDetail()
})

onUnmounted(() => {
  stopPolling()
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
    background-color: RGBA(22, 23, 36, 1.00);
  }
}
</style>
