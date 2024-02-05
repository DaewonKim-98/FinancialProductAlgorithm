<!-- updateprofileview.vue -->

<template>
  <h1 class="m-3 fw-bold">개인 정보 수정</h1>
  <div class="d-flex flex-column align-items-center mx-auto" style="width: 500px;">
      <form @submit.prevent="updateProfile">
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">비밀번호 </span>
          <input v-model="newPassword" style="width: 500px;" type="password" class="rounded-3 form-control border border-warning" placeholder="PASSWORD">
        </div>
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">이름 </span>
          <input v-model="nickname" style="width: 500px;" type="text" class="rounded-3 form-control border border-warning" placeholder="USERNAME">
        </div>
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">성별 </span>
          <div>
          <div class="mb-3 form-check form-check-inline">
            <input v-model="gender" class="form-check-input border border-warning" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="남성">
            <label class="form-check-label" for="inlineRadio1">남성</label>
          </div>
          <div class="mb-3 form-check form-check-inline">
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
        <div class="d-grid gap-2 mt-5">
          <button class="btn btn-warning" type="submit">개인 정보 수정</button>
        </div>
      </form>
    </div>
</template>

<script setup>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { ref } from 'vue'

const store = useUserStore()
const nickname = ref(null)
const gender = ref(null)
const age = ref(null)
const newPassword = ref(null)
const masks = ref({
  modelValue: 'YYYY-MM-DD',
})

const updateProfile = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/accounts/update-profile/`,
    data: {
      nickname: nickname.value,
      gender: gender.value,
      age: age.value,
      newPassword: newPassword.value,
    },
    headers: {
        Authorization: `Token ${store.token}`
    }

  })
    .then((res) => {
      console.log(res);
      window.alert('수정이 완료되었습니다.')
      nickname.value = null
      gender.value = null
      age.value = null
      newPassword.value = null
      // Handle success, e.g., show a success message
    })
    .catch((error) => {
      console.log(error)
      window.alert('빈 칸을 모두 입력하세요.')

      // Handle error, e.g., show an error message
    });
}
</script>

<style scoped>
/* Add your styles here */
</style>
