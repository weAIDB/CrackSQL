<template>
  <template v-if="!item.hidden">
    <template v-if="showSidebarItem(item.children, item)">
      <Link v-if="onlyOneChild.meta" :to="resolvePath(onlyOneChild.path)">
        <el-tooltip
            class="box-item"
            effect="dark"
            :content="langTitle(onlyOneChild.meta?.tooltip)"
            placement="right"
        >
          <div
              :id="onlyOneChild.name?.toLowerCase()"
              :class="`sidebar-item ${isActived ? ' sidebar-item-active': ''}`"
          >
            <el-icon style="margin: 10px 0" :color="isActived ? 'var(--el-color-primary)' : '#333333' " size="28">
              <component :is="onlyOneChild.meta?.elSvgIcon"/>
            </el-icon>
          </div>
        </el-tooltip>
      </Link>
    </template>
  </template>
</template>

<script setup lang="ts">
import {langTitle} from '@/hooks/use-common'
import {isExternal} from '@/hooks/use-layout'
import {resolve} from 'path-browserify'
import {computed, ref} from 'vue'
import type {RouteRawConfig} from '~/basic'
import Link from './Link.vue'

const props = defineProps({
  //每一个router Item
  item: {
    type: Object,
    required: true
  },
  //用于判断是不是激活样式
  activePath: {
    type: String,
    default: ''
  },
  //基础路径，用于拼接
  basePath: {
    type: String,
    default: ''
  }
})

//显示sidebarItem 的情况
const onlyOneChild = ref()
const showSidebarItem = (children = [], parent) => {
  const showingChildren = children.filter((item: RouteRawConfig) => {
    if (item.hidden) {
      return false
    } else {
      return true
    }
  })
  if (showingChildren.length > 0 && !parent?.alwaysShow) {
    onlyOneChild.value = showingChildren[0]
    return true
  }
  if (showingChildren.length === 0) {
    onlyOneChild.value = {...parent, path: '', noChildren: true}
    return true
  }
  return false
}
const resolvePath = (routePath) => {
  if (isExternal(routePath)) {
    return routePath
  }
  if (isExternal(props.basePath)) {
    return props.basePath
  }
  return resolve(props.basePath, routePath)
}
const isActived = computed(() => {
  return props.activePath === resolvePath(onlyOneChild.value.path)
})
</script>

<style scoped lang="scss">
.sidebar-item {
  display: flex;
  align-items: center;
  cursor: pointer;
  flex-direction: column;
  transition: all 0.3s;
  margin-bottom: 20px;
  width: 60px;

  &:hover {
    background-color: white;
  }
}

.sidebar-item-active {
  background-color: white !important;

  span {
    color: var(--el-color-primary);
  }
}
</style>
