<template>
  <h1 class="m-3 fw-bold">회원가입</h1>
    <div class="d-flex flex-column align-items-center mx-auto" style="width: 500px;">
      <form @submit.prevent="signup">
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">아이디 </span>
          <input v-model="username" type="text" style="width: 500px;" class="rounded-3 form-control border border-warning" placeholder="ID">
        </div>
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">비밀번호 </span>
          <input v-model="password1" style="width: 500px;" type="password" class="rounded-3 form-control border border-warning" placeholder="PASSWORD">
        </div>
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">비밀번호 확인 </span>
          <input v-model="password2" style="width: 500px;" type="password" class="rounded-3 form-control border border-warning" placeholder="CHECK PASSWORD">
        </div>
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">이름 </span>
          <input v-model="nickname" style="width: 500px;" type="text" class="rounded-3 form-control border border-warning" placeholder="USERNAME">
        </div>
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">성별 </span>
          <div>
          <div class="form-check form-check-inline">
            <input v-model="gender" class="form-check-input border border-warning" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="남성">
            <label class="form-check-label" for="inlineRadio1">남성</label>
          </div>
          <div class="form-check form-check-inline">
            <input v-model="gender" class="form-check-input border border-warning" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="여성">
            <label class="form-check-label" for="inlineRadio2">여성</label>
          </div>  
          </div>
        </div>
        <div class="input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">생년월일</span>
          {{ age ? age.slice(0, 10) : '' }}
          <v-date-picker class="border border-warning" v-model.string="age" :masks="masks" no-title color="orange"/>
        </div>
        <div class="mt-5 d-grid gap-2 mt-3">
          <button class="btn btn-warning" type="submit">회원가입</button>
        </div>
      </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const gender = ref(null)
const age = ref(null)
const masks = ref({
  modelValue: 'YYYY-MM-DD',
})

const signup = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    gender: gender.value,
    age: age.value,
  }
  store.signup(payload)
}
</script>

<style scoped>

</style>