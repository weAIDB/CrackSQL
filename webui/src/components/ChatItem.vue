<template>
  <div class="chat-item-container">
    <div :class="'rowSC ' + roleClass">
      <img v-if="isUser" src="@/assets/chat-user.png" class="face"/>
      <img v-else src="@/assets/chat-robot.png" class="face" />
<!--      <span style="margin: 0 10px; color: red">abc</span>-->
<!--      <span style="color: #2c59cb">sdada</span>-->
    </div>
    <div :class="'rowSC ' + roleClass">
      <div v-if="!message.loading" style="max-width: 100%" class="content" v-html="htmlContent" />
      <div v-else>
        <div class="content rowBC" style="padding: 10px 20px">
          <el-icon class="is-loading" size="20" color="#333333">
            <Loading />
          </el-icon>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// 获取store和router
import marked from '../utils/markdownConfig.js'

const props = defineProps({
  message: {required:true, type: Object, default: null }
})

const isUser = computed(() => props.message.role === 'user')

const roleClass = computed(() => props.message.role === 'user' ? 'right' : 'left')

const htmlContent = computed(() => {
  return marked.parse(props.message.content)
})


</script>

<style>
code {
  border-radius: 4px;
}
</style>

<style scoped lang="scss">

.chat-item-container {
  margin: 5px 0;
  display: flex;
  flex-direction: column;
  width: 100%;
}

.face {
  width: 36px;
  height: 36px;
  border-radius: 36px;
}

.content {
  color: #333333;
  font-size: 15px;
  min-height: 20px;
  border-radius: 10px;
  padding: 10px 15px 0 15px;
  line-height: 1.4;
  word-break: break-all;
  word-wrap: break-word;
  position: relative;
  margin-top: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.06);;
}

.left {
  margin: 0 10px;
  .face {}
  .content {
    color: #333333;
    border: 1px solid #eeeeee;
    border-radius: 0 10px 10px 10px;
  }
}

.right {
  margin: 0 10px;
  flex-direction: row-reverse;
  .face {}
  .content {
    color: #41b584;
    background-color: #ecf8f3;
    border: 1px solid #41b584;
    border-radius: 10px 0 10px 10px;
  }
}

</style>
