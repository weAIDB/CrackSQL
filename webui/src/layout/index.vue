<template>
  <div :class="classObj" class="layout-wrapper">
    <!--left side-->
    <Sidebar v-if="settings.showLeftMenu" class="sidebar-container"/>
    <!--right container-->
    <div class="main-container">
      <AppMain/>
    </div>

    <!-- 网站引导 -->
    <el-tour v-model="tourOpen">
      <el-tour-step
          placement="bottom"
          target="#welcome"
          title="🎉🎉🎉欢迎使用方言改写🎉🎉🎉"
          description="本项目专注于不同数据库之间的语句转换，旨在为开发者提供便捷的工具，帮助他们轻松应对因数据库差异而产生的语句适配难题。"
      />
      <el-tour-step
          placement="bottom"
          target="#github"
          title="可以在 GitHub 上 Star 并关注我们"
          description="本项目已开源并托管在 GitHub 平台，欢迎各位开发者前往查看源代码、参与贡献以及获取最新版本。"
      />
      <el-tour-step
          placement="right"
          target="#dashboard"
          title="创建新的改写"
          description="在这里可以创建新的SQL改写"
      />
      <el-tour-step
          placement="right"
          target="#chat"
          title="最近的一次改写"
          description="在这里可以查看最近的一次改写任务"
      />
      <el-tour-step
          placement="right"
          target="#history"
          title="改写历史"
          description="查看所有的SQL改写记录"
      />
      <el-tour-step
          placement="right"
          target="#database"
          title="数据库配置"
          description="管理目标数据库的连接配置"
      />
      <el-tour-step
          placement="right"
          target="#source-db"
          title="语句原始数据库"
          description="请选择语句原始数据库"
      />
      <el-tour-step
          placement="left"
          target="#target-db"
          title="目标数据库"
          description="请选择目标数据库，为了提高语句转换的正确率，请添加目标数据库的连接信息，转换过程中，会访问改数据库获取执行计划。"
      />
      <el-tour-step
          placement="left"
          target="#sql-input"
          title="语句输入"
          description="请在此处输入需要转换的SQL语句"
      />
      <el-tour-step
          placement="left"
          target="#convert-btn"
          title="开始转换"
          description="点击按钮开始进行语句改写"
      />
    </el-tour>
  </div>
</template>

<script setup lang="ts">
import {resizeHandler} from '@/hooks/use-layout'
import {useBasicStore} from '@/store/basic'
import {hasWebsiteBeenShownFirstTime, setWebsiteFirstShowStatus} from '@/utils/tour'
import {computed, onMounted, ref} from 'vue'
import AppMain from './app-main/index.vue'
import Sidebar from './sidebar/index.vue'

const {sidebar, settings} = useBasicStore()
const tourOpen = ref(false)

const classObj = computed(() => {
  return {
    closeSidebar: true,
    hideSidebar: !settings.showLeftMenu
  }
})

onMounted(() => {
  if (!hasWebsiteBeenShownFirstTime()) {
    tourOpen.value = true
    setWebsiteFirstShowStatus(true)
  }
})

resizeHandler()
</script>

<style>
.el-tour__body span {
  line-height: 1.6!important;
}
</style>

<style lang="scss" scoped>

.main-container {
  min-height: 100%;
  transition: margin-left var(--sideBar-switch-duration);
  margin-left: var(--side-bar-width);
  position: relative;
  border-radius: 15px;
  overflow: auto;
}

.sidebar-container {
  transition: width var(--sideBar-switch-duration);
  width: var(--side-bar-width) !important;
  background-color: var(--body-background) !important;
  height: 100%;
  position: fixed;
  font-size: 0;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 1001;
  overflow: hidden;
}

.closeSidebar {
  .sidebar-container {
    width: 60px !important;
    background-color: #ffffff !important;
    height: 80vh;
    margin-top: 10vh;
    margin-left: 10px !important;
    border-radius: 12px;
  }

  .main-container {
    margin-left: 80px !important;
    margin-top: var(--app-main-padding) !important;
    margin-bottom: var(--app-main-padding) !important;
    margin-right: var(--app-main-padding) !important;
  }
}

.hideSidebar {
  .sidebar-container {
    width: 0 !important;
  }

  .main-container {
    margin-left: 0;
  }
}
</style>
