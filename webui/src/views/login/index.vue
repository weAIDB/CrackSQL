<template>
  <div class="login-container columnCC">
    <el-form ref="refLoginForm" class="login-form" label-width="auto" label-position="right" :model="subForm" :rules="formRules">
      <div class="title-container">
        <h3 class="title text-center">{{ settings.title }}</h3>
      </div>
      <el-form-item prop="username" :rules="formRules.isNotNull($t('login.rules.username'))">
        <div class="rowSC">
          <span class="svg-container">
            <svg-icon icon-class="user" />
          </span>
          <el-input 
              v-model="subForm.username" 
              :placeholder="$t('login.form.usernamePlaceholder')" 
          />
        </div>
      </el-form-item>
      <el-form-item prop="password" :rules="formRules.isNotNull($t('login.rules.password'))">
        <div class="rowSC flex-1">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
              :key="passwordType"
              ref="refPassword"
              v-model="subForm.password"
              :type="passwordType"
              name="password"
              :placeholder="$t('login.form.passwordPlaceholder')"
              @keyup.enter="handleLogin"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span>
        </div>
      </el-form-item>
      <div class="tip-message">{{ tipMessage }}</div>
      <el-button 
          :loading="subLoading" 
          type="primary" 
          class="login-btn" 
          size="default" 
          @click.prevent="handleLogin"
      >
        {{ $t('login.button') }}
      </el-button>
    </el-form>
  </div>
</template>

<script setup>
import { reactive, ref, watch, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useBasicStore } from '@/store/basic'
import { elMessage, useElement } from '@/hooks/use-element'
import { loginReq } from '@/api/user'
import { useI18n } from '@/hooks/use-i18n'

const i18n = useI18n()
const { settings } = useBasicStore()
const formRules = useElement().formRules

const subForm = reactive({
  username: '',
  password: ''
})

const state = reactive({
  otherQuery: {},
  redirect: undefined
})

const route = useRoute()
const getOtherQuery = (query) => {
  return Object.keys(query).reduce((acc, cur) => {
    if (cur !== 'redirect') {
      acc[cur] = query[cur]
    }
    return acc
  }, {})
}

watch(
    () => route.query,
    (query) => {
      if (query) {
        state.redirect = query.redirect
        state.otherQuery = getOtherQuery(query)
      }
    },
    { immediate: true }
)

const subLoading = ref(false)
const tipMessage = ref('')
const refLoginForm = ref(null)
const handleLogin = () => {
  refLoginForm.value.validate((valid) => {
    subLoading.value = true
    if (valid) loginFunc()
  })
}

const router = useRouter()
const basicStore = useBasicStore()

const loginFunc = () => {
  loginReq(subForm)
      .then(({ data }) => {
        elMessage(i18n.t('login.success'))
        basicStore.setToken(data?.access_token)
        basicStore.setUserInfo({userInfo: {username: data?.username}})
        router.push('/')
      })
      .catch((err) => {
        tipMessage.value = err?.msg || i18n.t('login.error')
      })
      .finally(() => {
        subLoading.value = false
      })
}

const passwordType = ref('password')
const refPassword = ref(null)
const showPwd = () => {
  if (passwordType.value === 'password') {
    passwordType.value = ''
  } else {
    passwordType.value = 'password'
  }
  nextTick(() => {
    refPassword.value.focus()
  })
}
</script>

<style lang="scss" scoped>
$bg: #2d3a4b;
$dark_gray: #889aa4;
$light_gray: #eee;
.login-container {
  height: 100vh;
  width: 100%;
  background-color: #2d3a4b;
  .login-form {
    margin-bottom: 20vh;
    width: 360px;
  }
  .title-container {
    .title {
      font-size: 22px;
      color: #eee;
      margin: 0px auto 25px auto;
      text-align: center;
      font-weight: bold;
    }
  }
}

.svg-container {
  padding-left: 6px;
  color: $dark_gray;
  text-align: center;
  width: 30px;
}

//错误提示信息
.tip-message {
  color: #e4393c;
  height: 30px;
  margin-top: -12px;
  font-size: 12px;
}

//登录按钮
.login-btn {
  width: 100%;
  margin-bottom: 30px;
}
.show-pwd {
  width: 50px;
  font-size: 16px;
  color: $dark_gray;
  cursor: pointer;
  text-align: center;
}
</style>

<style lang="scss">
//css 样式重置 增加个前缀避免全局污染
.login-container {
  .el-input__wrapper {
    background-color: transparent;
    box-shadow: none;
  }
  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
  .el-input input {
    background: transparent;
    border: 0px;
    -webkit-appearance: none;
    border-radius: 0px;
    padding: 10px 5px 10px 15px;
    color: #fff;
    height: 42px; //此处调整item的高度
    caret-color: #fff;
  }
  //hiden the input border
  .el-input__inner {
    box-shadow: none !important;
  }
}
</style>
