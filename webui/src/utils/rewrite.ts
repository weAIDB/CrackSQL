import type { RewriteHistory } from '@/types/database'

// 用户消息模板
export const userTemplate = 
    'Please convert the ***[originalDB]*** query:\n```sql\n[sql]\n```\nto a ***[type]*** query. The ***[type]*** connection info is <u>[user]@[host]:[port]/[database]</u>'

// 格式化用户消息
export const formatUserMessage = (history: RewriteHistory) => {
  return userTemplate
      .replace('[originalDB]', history.source_db_type)
      .replace('[sql]', history.original_sql)
      .replace('[type]', history.target_db.db_type)
      .replace('[user]', history.target_db.username)
      .replace('[host]', history.target_db.host)
      .replace('[port]', history.target_db.port)
      .replace('[database]', history.target_db.database)
      .replace('[type]', history.target_db.db_type)
}

// 获取状态标签类型
export const getStatusType = (status: string) => {
  const types = {
    success: 'success',
    failed: 'danger',
    processing: 'warning'
  }
  return types[status as keyof typeof types]
}

// 格式化日期
export const formatDate = (date: string) => {
  return new Date(date).toLocaleString()
}

// 计算持续时间
export const calculateDuration = (createdAt: string, updatedAt: string) => {
  if (!createdAt || !updatedAt) return '未知'
  
  const start = new Date(createdAt).getTime()
  const end = new Date(updatedAt).getTime()
  
  // 计算时间差（毫秒）
  const diff = end - start
  
  // 如果时间差小于0或者无效，返回未知
  if (diff < 0 || isNaN(diff)) return '未知'
  
  // 转换为秒
  const seconds = Math.floor(diff / 1000)
  
  // 如果小于1分钟
  if (seconds < 60) {
    return `${seconds}秒`
  }
  
  // 如果小于1小时
  if (seconds < 3600) {
    const minutes = Math.floor(seconds / 60)
    const remainingSeconds = seconds % 60
    return `${minutes}分${remainingSeconds}秒`
  }
  
  // 如果小于1天
  if (seconds < 86400) {
    const hours = Math.floor(seconds / 3600)
    const minutes = Math.floor((seconds % 3600) / 60)
    return `${hours}小时${minutes}分`
  }
  
  // 如果大于等于1天
  const days = Math.floor(seconds / 86400)
  const hours = Math.floor((seconds % 86400) / 3600)
  return `${days}天${hours}小时`
} 