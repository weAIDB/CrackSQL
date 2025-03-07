<template>
  <div :class="classObj" class="layout-wrapper">
    <!--left side-->
    <Sidebar v-if="settings.showLeftMenu" class="sidebar-container"/>
    <!--right container-->
    <div class="main-container">
      <AppMain/>
    </div>

    <!-- Website Tour -->
    <el-tour v-model="tourOpen">
      <el-tour-step
          placement="bottom"
          target="#welcome"
          title="🎉🎉🎉Welcome to SQL Dialect Rewrite🎉🎉🎉"
          description="This is a tool for converting SQL statements between different database dialects. It uses LLM to understand the intent of the SQL statement and convert it to the target dialect."
      />
      <el-tour-step
          placement="bottom"
          target="#github"
          title="🎉🎉🎉Welcome to SQL Dialect Rewrite🎉🎉🎉"
          description="Visit Github and give us a Star! Your encouragement drives us forward!"
      />
      <el-tour-step
          placement="right"
          target="#dashboard"
          title="🎉🎉🎉Welcome to SQL Dialect Rewrite🎉🎉🎉"
          description="Start your SQL dialect conversion journey here!"
      />
      <el-tour-step
          placement="right"
          target="#chat"
          title="Latest Rewrite"
          description="View the latest rewrite task here"
      />
      <el-tour-step
          placement="right"
          target="#history"
          title="Rewrite History"
          description="View all SQL rewrite records"
      />
      <el-tour-step
          placement="right"
          target="#knowledge"
          title="Knowledge Base Management"
          description="Manage knowledge base here"
      />
      <el-tour-step
          placement="right"
          target="#database"
          title="Database Configuration"
          description="Manage target database connection settings"
      />
      <el-tour-step
          placement="right"
          target="#modelmanagement"
          title="Model Management"
          description="Configure LLM and Embedding models here"
      />
      <el-tour-step
          placement="right"
          target="#source-db"
          title="Source Database"
          description="Please select the source database"
      />
      <el-tour-step
          placement="left"
          target="#target-db"
          title="Target Database"
          description="Please select the target database. To improve the accuracy of statement conversion, please add the connection information of the target database. During the conversion process, the execution plan will be obtained by accessing this database."
      />
      <el-tour-step
          placement="left"
          target="#sql-input"
          title="SQL Input"
          description="Please enter the SQL statement to be converted here"
      />
      <el-tour-step
          placement="left"
          target="#convert-btn"
          title="Start Conversion"
          description="Click the button to start statement rewriting"
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
