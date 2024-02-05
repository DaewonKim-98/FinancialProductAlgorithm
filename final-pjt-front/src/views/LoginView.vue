<template>
  <h1>Login</h1>
  <div class="d-flex flex-column align-items-center mx-auto" style="width: 500px;">
    <form @submit.prevent="login">
      <div class="mb-3 input-group flex-nowrap d-flex flex-column">
        <span class="mb-1">아이디 </span>
        <input v-model="username" type="text" style="width: 500px;" class="rounded-3 form-control border border-warning" placeholder="ID">
      </div>
      <div class="mb-3 input-group flex-nowrap d-flex flex-column">
        <span class="mb-1">비밀번호 </span>
        <input v-model="password" style="width: 500px;" type="password" class="rounded-3 form-control border border-warning" placeholder="PASSWORD">
      </div>
      <div class="d-grid gap-2 mt-3">
        <button class="btn btn-warning" type="submit">로그인</button>
      </div>
    </form>
    <RouterLink class="mt-3 fw-bold btn btn-outline-warning align-self-start" :to="{ name: 'signup' }">회원가입</RouterLink>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterView, RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const username = ref(null)
const password = ref(null)

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.login(payload)
}

</script>

<style  scoped>

</style>