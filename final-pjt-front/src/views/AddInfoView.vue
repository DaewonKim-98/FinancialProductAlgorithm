<template>
  <div class="m-3">
    <div class="d-flex justify-content-between">
      <div>
        <h1 class="fw-bold">추가 정보 입력</h1>
        <h5>해당 페이지는 첫 상품 추천시에만 노출됩니다</h5>
      </div>
      <button style="height: 50px;" class="fw-bold btn btn-outline-warning" @click="go_back">뒤로가기</button>
    </div>

    <div class="m-5 d-flex flex-column align-items-center mx-auto" style="width: 500px;">
      <form @submit.prevent="saveInfo">
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">현재 예금 가능액</span>
          <input v-model="depositMoney" style="width: 500px;" type="text" class="rounded-3 form-control border border-warning" placeholder="단위: 만원">
        </div>
        <div class="mb-3 input-group flex-nowrap d-flex flex-column">
          <span class="mb-1">매월 적금 가능액</span>
          <input v-model="savingMoney" style="width: 500px;" type="text" class="rounded-3 form-control border border-warning" placeholder="단위: 만원">
        </div>
        <div>
          <div class="mb-3 input-group flex-nowrap d-flex flex-column">
            <span class="mb-1">총 자산</span>
            <input v-model="totalMoney" style="width: 500px;" type="text" class="rounded-3 form-control border border-warning" placeholder="단위: 만원">
          </div>
          <div class="mb-3 input-group flex-nowrap d-flex flex-column">
            <span class="mb-1">목표 거주지</span>
            <div class="dropdown">
              <button class="btn border dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                {{ targetPlace }}
              </button>
              <ul class="dropdown-menu" style="max-height: 300px; overflow-y: auto;">
                <li v-for="apartment in apartments" :key="apartment.id">
                  <a class="dropdown-item" href="#" @click="selectApartment(apartment.sigu)">{{ apartment.sigu }}</a>
                </li>
              </ul>
            </div>
          </div>
          <div class="input-group flex-nowrap d-flex flex-column position-relative" style="height: 90px;">
            <span class="mb-1">목표 입주 시기</span>
            <month-picker-input class="z-3 position-absolute bottom-0" :min-date="new Date()" :default-month="12" lang="ko" @change="monthValue" :no-default="false">
            </month-picker-input>
          </div>

        </div>
        <div class="d-grid gap-2 mt-5">
          <button class="btn btn-warning" type="submit">확인</button>
        </div>
      </form>
    </div>
  </div>
  
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { MonthPickerInput } from 'vue-month-picker'

const store = useUserStore()
const router = useRouter()

const go_back = function () {
  router.push({ name: 'mypage' })
}

const depositMoney = ref(null)
const savingMoney = ref(null)
const totalMoney = ref(null)
const targetPlace = ref('시 / 군 / 구')
const moveTime = ref(null)

const monthValue = function(date) {
  moveTime.value = date.year + '-' + date.month.slice(0, -1)
}

store.apartments()
const apartments = store.apartmentsResult

const selectApartment = (sigu) => {
  targetPlace.value = sigu;
};

const saveInfo = function () {
  const payload = {
    depositMoney: depositMoney.value,
    savingMoney: savingMoney.value,
    totalMoney: totalMoney.value,
    targetPlace: targetPlace.value,
    moveTime: moveTime.value,
  }
  store.saveInfo(payload)
  router.push({ name: "mypage" })
}

</script>
<style scoped>
span {
  margin-top: 10px;
}
</style>