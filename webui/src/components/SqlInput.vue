<template>
  <div class="sql-input-container">
    <el-descriptions :column="2" border>

      <el-descriptions-item label="Connection Info" :span="4">
        <div class="connection-info">
          {{ message.target_db.username }}@{{ message.target_db.host }}:{{ message.target_db.port }}/{{ message.target_db.database }}
        </div>
      </el-descriptions-item>

      <el-descriptions-item label="Model" :span="4">
        {{ message.llm_model_name }}
      </el-descriptions-item>
      
      <el-descriptions-item label="Source Database">
        <div class="db-info">
          <span class="db-type">{{ message.source_db_type }}</span>
        </div>
      </el-descriptions-item>

      <el-descriptions-item label="Source Knowledge Base">
        <div class="db-info">
          <span class="db-type">{{ message.original_kb?.name }}</span>
        </div>
      </el-descriptions-item>

      <el-descriptions-item label="Target Database">
        <div class="db-info">
          <span class="db-type">{{ message.target_db.db_type }}</span>
        </div>
      </el-descriptions-item>

      <el-descriptions-item label="Target Knowledge Base">
        <div class="db-info">
          <span class="db-type">{{ message.target_kb?.name }}</span>
        </div>
      </el-descriptions-item>
      

      <el-descriptions-item label="Original SQL" :span="4">
        <div class="sql-section">
          {{ message.original_sql }}
        </div>
      </el-descriptions-item>

      <el-descriptions-item v-if="message.rewritten_sql" label="Rewrite SQL" :span="4">
        <div class="sql-section">
          {{ message.rewritten_sql }}
        </div>
      </el-descriptions-item>
    </el-descriptions>
  </div>
</template>

<script setup lang="ts">
import { ElDescriptions, ElDescriptionsItem } from 'element-plus'

interface TargetDB {
  db_type: string
  username: string
  host: string
  port: string
  database: string
}

interface KB {
  name: string
}

interface SqlMessage {
  source_db_type: string
  original_sql: string
  target_db: TargetDB
  created_at: string
  llm_model_name: string
  original_kb?: KB
  target_kb?: KB
}

const props = defineProps({
  message: {required:true, type: Object as () => SqlMessage, default: null }
})
</script>

<style scoped lang="scss">
.sql-input-container {
  margin: 5px 0;
  padding: 10px;
  background-color: RGBA(22, 23, 36, 1.00);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  gap: 15px;

  :deep(.el-descriptions) {
    --el-text-color-regular: #ffffff;
    --el-border-color: rgba(255, 255, 255, 0.1);
    --el-fill-color-blank: transparent;
    
    .el-descriptions__header {
      margin-bottom: 0;
      padding: 0 10px;
    }
    
    .el-descriptions__body {
      background-color: transparent;
      
      .el-descriptions__table {
        .el-descriptions__cell {
          padding: 12px 15px;
          background-color: rgba(0, 0, 0, 0.2);
        }
        
        .el-descriptions__label {
          color: rgba(255, 255, 255, 0.7);
          font-weight: 500;
          background-color: rgba(0, 0, 0, 0.3);
        }
        
        .el-descriptions__content {
          color: #ffffff;
          font-size: 15px;
          line-height: 1.4;
        }
      }
    }
  }
}

.db-info {
  display: flex;
  align-items: center;
  gap: 10px;

  .db-type {
    font-weight: 500;
  }

  .kb-name {
    color: rgba(255, 255, 255, 0.7);
    font-size: 14px;
  }
}

.connection-info {
  font-family: Monaco, Consolas, Courier New, monospace;
  color: rgba(255, 255, 255, 0.85);
  padding: 10px !important;
  background-color: rgba(111, 111, 111, 0.1)!important;
  border-radius: 4px;
  display: inline-block;
}

.sql-section {
  color: #ffffff;
  background-color: rgba(111, 111, 111, 0.1) !important;
  border-radius: 8px;
  overflow: hidden;
  padding: 10px !important;

  .sql-label {
    padding: 10px 15px;
    color: rgba(255, 255, 255, 0.7);
    font-weight: 500;
    background-color: rgba(0, 0, 0, 0.3);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  pre {
    margin: 0;
    padding: 15px;
    
    code {
      color: #ffffff;
      font-family: Monaco, Consolas, Courier New, monospace;
      font-size: 14px;
      line-height: 1.5;
    }
  }
}
</style> 