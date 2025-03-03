<template>
  <div class="chat-item-container">
    <div class="terminal-header">
      <span class="prompt">$</span>
      <span class="role">{{ message.role }}</span>
      <span class="time">{{ message.time }}</span>
    </div>
    <div class="terminal-content">
      <div v-if="!message.loading" v-html="htmlContent" />
      <div v-else class="loading">
        <el-icon class="is-loading" size="20">
          <Loading />
        </el-icon>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import marked from '../utils/markdownConfig.js'
import { Loading } from '@element-plus/icons-vue'

interface Message {
  loading: boolean
  content: string
  role: string
  time: string
}

const props = defineProps({
  message: {required:true, type: Object as () => Message, default: null }
})

const htmlContent = computed(() => {
  return marked.parse(props.message.content)
})
</script>

<style>
code {
  border-radius: 4px;
  background-color: rgba(0, 0, 0, 0.3);
  padding: 2px 4px;
  font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
  color: #98C379;
}

think {
  display: block;
  border-radius: 4px;
  color: #ABB2BF;
  padding: 15px;
  margin: 10px 0;
  position: relative;
  background-color: rgba(0, 0, 0, 0.3);
  border-left: 2px solid #61AFEF;
}

think:before {
  content: '💡';
  font-size: 24px;
  position: absolute;
  left: -13px;
  top: -16px;
}

think pre code {
  background: rgba(0, 0, 0, 0.2) !important;
  padding: 12px;
  border-radius: 4px;
  font-size: 14px;
  color: #98C379;
}
</style>

<style scoped lang="scss">
.chat-item-container {
  margin: 10px 0;
  background-color: #282C34;
  border-radius: 6px;
  overflow: hidden;
  font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
}

.terminal-header {
  background-color: #21252B;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1px solid #181A1F;

  .prompt {
    color: #98C379;
    font-weight: bold;
  }

  .role {
    color: #61AFEF;
    font-weight: 500;
  }

  .time {
    color: #5C6370;
    font-size: 12px;
    margin-left: auto;
  }
}

.terminal-content {
  padding: 15px;
  color: #ABB2BF;
  font-size: 14px;
  line-height: 1.6;

  :deep(p) {
    margin: 8px 0;
  }

  :deep(pre) {
    background-color: rgba(0, 0, 0, 0.3);
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
    margin: 10px 0;
  }

  :deep(ul), :deep(ol) {
    padding-left: 20px;
    margin: 8px 0;
  }

  :deep(li) {
    margin: 4px 0;
  }

  :deep(a) {
    color: #61AFEF;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }

  :deep(blockquote) {
    border-left: 2px solid #61AFEF;
    margin: 10px 0;
    padding-left: 15px;
    color: #5C6370;
  }

  .loading {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    color: #61AFEF;
  }
}
</style>
