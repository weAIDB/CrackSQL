import type { RewriteHistory } from '@/types/database'

// 用户消息模板
export const userTemplate = 
    '请将 ***[originalDB]*** 的query：\n```sql\n[sql]\n```\n转换成 ***[type]*** 的query。***[type]*** 的链接信息为 <u>[user]@[host]:[port]/[database]</u>'

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