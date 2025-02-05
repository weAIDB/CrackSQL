import { useI18n as vueUseI18n } from 'vue-i18n'

// 创建一个缓存变量来存储i18n实例
let i18nInstance = null

export const useI18n = () => {
  if (!i18nInstance) {
    i18nInstance = vueUseI18n()
  }
  return i18nInstance
}

// 导出一个便捷的翻译方法
export const t = (key: string) => {
  const i18n = useI18n()
  return i18n.t(key)
} 