<template>
  <div class="m-3">
    <h1 class="fw-bold">가입 상품</h1>
    <div v-if="cartItems.length">
      <div v-for="product in cartItems" class="card card-body border-warning m-3" :key="product.fin_prdt_cd">
        <p><span class="fw-bold">회사명 :</span> {{ product.kor_co_nm }}</p>
        <p><span class="fw-bold">상품명 :</span> {{ product.fin_prdt_nm }}</p>
        <p><span class="fw-bold">가입시기:</span> {{ product.created_at.slice(0, 10) }}</p>
        <button style="width: 160px;" class="light btn btn-warning mb-3" @click="goDetail(product)">상세페이지로 이동</button>
        <button style="width: 80x;" class="light btn btn-warning" @click="removeCart(product)">가입 취소</button>
      </div>
    </div>
    <div v-else class="mt-5">
      <strong class="fs-5">가입된 상품이 없습니다.</strong>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue"
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const router = useRouter()
const route = useRoute()

// 이부분도 유저에 연결된 db에서 가져오는거로 수정
const cartItems = ref([])

onMounted (() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/carts/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      cartItems.value = res.data.filter((item) => {
        return item.user === store.userPk
      })
    })
    .catch((err) => {
      console.log(err)
    })
})

const goDetail = (tmp) => {
  if (store.productList_deposit.filter(product => { return product.fin_prdt_cd === tmp.fin_prdt_cd })[0]) {
    store.nowType = 'deposit'
} else if (store.productList_saving.filter(product => { return product.fin_prdt_cd === tmp.fin_prdt_cd })[0]) {
  store.nowType = 'saving'
} else if (store.corpersProducts.filter(product => { return product.fin_prdt_cd === tmp.fin_prdt_cd })[0]) {
  store.nowType = 'loan'
}
  router.push({ name: 'productDetail', params: { id: tmp.fin_prdt_cd } })
}

const removeCart = (product) => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/accounts/carts/${product.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      // Remove the deleted product from the local cartItems array
      cartItems.value = cartItems.value.filter(item => item.id !== product.id);
    })
    .catch((err) => {
      console.log(err);
    });
}

</script>

<style scoped>
.card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s;
}

.card:hover {
  transform: scale(1.02);
}

.card-body {
  padding: 20px;
}

.btn-light {
  background-color: #1e88e5; /* 연한 파랑색으로 변경 */
  color: #fff;
}

.btn-light:hover {
  background-color: #005cbf; /* 버튼 호버 시 어두운 파랑색으로 변경 */
}
</style>