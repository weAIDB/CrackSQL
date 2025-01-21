<template>
  <div class="sidebar-logo-container">
    <transition name="sidebar-logo-fade">
      <img src="@/assets/avatar.jpg" />
    </transition>
  </div>
</template>

<script setup lang="ts">
import { reactive, toRefs } from 'vue'
import { useBasicStore } from '@/store/basic'
import SvgIcon from '@/icons/SvgIcon.vue'
const { settings } = useBasicStore()
defineProps({
  //是否折叠
  collapse: {
    type: Boolean,
    required: true
  }
})
const state = reactive({
  title: settings.title,
  //src/icons/common/sidebar-logo.svg
  logo: 'sidebar-logo'
})
//export to page for use
const { title, logo } = toRefs(state)
</script>

<style lang="scss">
//vue3.0 过度效果更改  enter-> enter-from   leave-> leave-from
.sidebar-logo-container {
  position: relative;
  width: 50px;
  height: 50px;
  overflow: hidden;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 2px solid white;
}
</style>
