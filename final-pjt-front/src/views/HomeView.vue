<template>
  <div class="d-flex flex-column" style="width: 100%;">
    <div class="d-flex align-center flex-column pt-5" style="width: 100%; background-color: #FFA500;">
      <div class="image-container" v-if="showing==='dj'">
        <img src="@/assets/images/DW.png" @click="changeShow('dw')" />
        <div class="d-flex flex-column align-items-center justify-content-center">
          <h1 class="text-effect">두 금융전문가와 함께합니다</h1>
          <img class="dj" src="@/assets/images/dj배경하양.png"/>
        </div>
        <img src="@/assets/images/JJ.png" @click="changeShow('jj')" />
      </div>
      <div class="image-container" v-else-if="showing==='dw'">
        <img src="@/assets/images/DW.png" @click="changeShow('dj')" />
        <div class="d-flex flex-column align-items-center justify-content-center">
          <h1 class="text-effect">최고의 금융전문가 김대원</h1>
          <h3 class="text-effect">나이 : 25세</h3>
          <h3 class="text-effect">경력 : 무경력</h3>
          <h3 class="text-effect">각오 한마디 : 고객님의 자산은 곧 나의 자산!</h3>
          <br>
          <button class="fw-bold btn btn-outline-light" @click="go_dw">후원하기</button>
        </div>
      </div>
      <div class="image-container" v-else-if="showing==='jj'">
        <img src="@/assets/images/JJ.png" @click="changeShow('dj')" />
        <div class="d-flex flex-column align-items-center justify-content-center">
          <h1 class="text-effect">최고의 금융전문가 이재종</h1>
          <h3 class="text-effect">나이 : 27세</h3>
          <h3 class="text-effect">경력 : 무경력</h3>
          <h3 class="text-effect">각오 한마디 : 어차피 남의 돈이라는 마인드!</h3>
          <br>
          <button class="fw-bold btn btn-outline-light" @click="go_dw">후원하기</button>
        </div>
      </div>
    </div>
    <div class="mt-4">
      <div class="d-flex flex-column align-items-center">
        <h3 class="fw-semibold mb-4">현재 가입 상품 순위</h3>
        <div class="col-md-8">
          <table class="table table-hover">
            <thead class="border-warning table-warning">
              <tr>
                <th scope="col">순위</th>
                <th scope="col">은행명</th>
                <th scope="col">상품명</th>
                <th scope="col">가입 인원</th>
              </tr>
            </thead>
            <tbody class="table-group-divider">
              <tr class="" v-for="(product, index) in ranking" :key="product.fin_prdt_cd">
                <td>{{ index + 1 }}위</td>
                <td>{{ product.kor_co_nm }}</td>
                <td>{{ product.fin_prdt_nm }}</td>
                <td>{{ product.frequency }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const router = useRouter()
const ranking = ref(null)
const showing = ref('dj')

const changeShow = function (conversionType) {
  if (conversionType === 'dj') {
    showing.value = 'dj'
  } else if (conversionType === 'dw') {
    showing.value = 'dw'
  } else if (conversionType === 'jj') {
    showing.value = 'jj'
  }
}

const go_dw = function () {
  router.push({ name: 'hidden'})
}

onMounted(() => {
  const store = useUserStore()
  const API_URL = 'http://127.0.0.1:8000'
  axios({
      method: 'get',
      url: `${API_URL}/recommends/apart/`,
    })
    .then((res) => {
      console.log('성공:', res.data.length)
      if (res.data.length === 0) {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/save-deposit-products/`,
        })
        .then((res) => {
          console.log('예금 데이터 세이브')
          console.log(res)
        })
        .then((res) => {
          store.pullProductList_deposit()
        })
        .catch((err) => {
          console.log(err)
        })

        axios({
          method: 'get',
          url: `${API_URL}/api/v1/save-saving-products/`,
        })
        .then((res) => {
          console.log('적금 데이터 세이브')
          console.log(res)
        })
        .then((res) => {
          store.pullProductList_saving()
          store.pullBankList()
        })
        .catch((err) => {
          console.log(err)
        })

        axios({
          method: 'get',
          url: `${API_URL}/api/v1/save-mortgage-loan-products/`,
        })
        .then((res) => {
          console.log('대출 데이터 세이브')
          console.log(res)
        })
        .then((res) => {
          store.pullProductList_loan()
          store.pullCorperList()
        })
        .catch((err) => {
          console.log(err)
        })

        axios({
          method: 'get',
          url: `${API_URL}/recommends/save-apart/`,
        })
        .then((res) => {
          console.log('아파트 데이터 세이브')
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })

        axios({
          method: 'get',
          url: `${API_URL}/exchanges/save-exchange-data/`,
        })
        .then((res) => {
          console.log('환율 데이터 세이브')
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        console.log('이미 아파트 데이터는 들어가있음')
      }
    })
    .catch((err) => {
      console.log('실패:', err)
    })
  axios({
        method: 'get',
        url: `${API_URL}/recommends/products-ranking/`,
      })
      .then((res) => {
        console.log('랭킹 반영')
        ranking.value = res.data
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })

})
</script>

<style scoped>
.dj {
  width: 300px;
  height: 300px;
}

img {
  width: 500px;
  height: 500px;
}
.image-container {
  display: flex;
  align-items: center;
  gap: 20px;
}

.text-effect {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  color: white;
}

</style>