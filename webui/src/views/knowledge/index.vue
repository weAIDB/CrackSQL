<!-- webui/src/views/knowledge/index.vue -->
<template>
  <div class="columnSC" style="width: 100%">
    <div class="rowBC" style="padding: 20px; width: 100%">
      <div style="font-size: 24px; color: #333333">{{ $t('knowledge.title') }}</div>
      <el-button
          ref="addKnowledgeRef"
          size="default"
          plain
          type="primary"
          @click="onCreateKnowledgeClick"
      >
        <el-icon><Plus /></el-icon>
        {{ $t('knowledge.create.button') }}
      </el-button>
    </div>

    <div class="knowledge-grid">
      <div
          v-for="(item, index) in knowledgeList"
          :key="index"
          class="knowledge-card"
          @click="onKnowledgeClick(item)"
      >
        <div class="knowledge-header">
          <div class="knowledge-title">
            <el-icon size="20" color="var(--el-color-primary)">
              <TakeawayBox/>
            </el-icon>
            <span>{{ item.kb_name }}</span>
          </div>
          <el-tag size="small" type="info">
            {{ item.embedding_model_name }}
          </el-tag>
        </div>
        <div class="knowledge-content">
          {{ item.kb_info }}
        </div>
        <div class="knowledge-footer">
          <el-button text type="primary" size="small">
            查看详情 <el-icon><ArrowRight /></el-icon>
          </el-button>
        </div>
      </div>
    </div>

    <CreateKnowledgeBase
        :visible="dialogCreateFormVisible"
        @update:visible="dialogCreateFormVisible = $event"
        @created="getKnowledgeList"
    />

    <el-tour
        v-model="tourOpen"
        :mask="{ color: 'rgba(0, 0, 0, .3)' }"
    >
      <el-tour-step :target="addKnowledgeRef?.$el" :title="$t('knowledge.create.tour.title')">
        <div>{{ $t('knowledge.create.tour.desc') }}</div>
      </el-tour-step>
    </el-tour>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { Plus, TakeawayBox, ArrowRight } from '@element-plus/icons-vue'
import CreateKnowledgeBase from '@/components/CreateKnowledgeBase.vue'
import { knowledgeListReq } from '@/api/knowledge'
import { useI18n } from '@/hooks/use-i18n'

const i18n = useI18n()
const router = useRouter()
const knowledgeList = ref([])
const dialogCreateFormVisible = ref(false)
const addKnowledgeRef = ref()
const tourOpen = ref(false)

onMounted(() => {
  getKnowledgeList()
})

const getKnowledgeList = async () => {
  try {
    const res = await knowledgeListReq()
    knowledgeList.value = res.data
    tourOpen.value = knowledgeList.value.length === 0
  } catch (error) {
    console.error('获取知识库列表失败:', error)
  }
}

const onCreateKnowledgeClick = () => {
  dialogCreateFormVisible.value = true
}

const onKnowledgeClick = (item) => {
  router.push({
    path: '/knowledge/detail',
    query: { kb_name: item.kb_name }
  })
}
</script>

<style lang="scss" scoped>
.knowledge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
  width: 100%;
}

.knowledge-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.05);
  padding: 20px;
  transition: all 0.3s ease;
  border: 1px solid var(--el-border-color-light);
  display: flex;
  flex-direction: column;
  
  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    border-color: var(--el-color-primary-light-5);
  }

  .knowledge-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;

    .knowledge-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 16px;
      font-weight: 600;
      color: var(--el-text-color-primary);
    }
  }

  .knowledge-content {
    color: var(--el-text-color-regular);
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 16px;
    flex: 1;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
  }

  .knowledge-footer {
    display: flex;
    justify-content: flex-end;
    margin-top: auto;
  }
}

.knowledge-container,
.knowledges-container {
  display: none;
}
</style>
