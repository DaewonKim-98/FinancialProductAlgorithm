<template>
  <div class="container m-3">
    <h1 class="fw-bold">상품 상세</h1>

    <div v-if="store.nowType==='deposit' || store.nowType==='saving'" class="mt-3 card border border-warning">
      <div class="card-body">
        <h5 class="fw-bold border-bottom border-warning pb-3 card-title"><span class="me-3">[{{ product.kor_co_nm }}]</span> {{ product.fin_prdt_nm }}</h5>
        <p class="mt-5 card-text"><span class="fw-bold">가입제한 :</span> {{ joinDenyText }}</p>
        <p class="mt-5 card-text"><span class="fw-bold">가입 방법 :</span> {{ product.join_way }}</p>
        <p class="mt-5 card-text"><span class="fw-bold">우대조건 :</span> {{ product.spcl_cnd }}</p>
        <p class="mt-5 card-text"><span class="fw-bold">상세 설명 :</span> {{ product.etc_note }}</p>
      </div>
    </div>

    <div v-else class="card">
      <div class="card-body">
        <h5 class="fw-bold border-bottom border-warning pb-3 card-title"><span class="me-3">{{ product.kor_co_nm }}</span> {{ product.fin_prdt_nm }}</h5>
        <p class="mt-5 card-text"><span class="fw-bold">가입 방법 :</span> {{ product.join_way }}</p>
        <p class="mt-5 card-text"><span class="fw-bold">대출한도 :</span> {{ product.loan_lmt }}</p>
        <p class="mt-5 card-text"><span class="fw-bold">연체 이자율 :</span> {{ product.dly_rate }}</p>
        <p class="mt-5 card-text"><span class="fw-bold">중도상환 수수료 :</span> {{ product.erly_rpay_fee }}</p>
        <p class="mt-5 card-text"><span class="fw-bold">대출 부대비용 :</span> {{ product.loan_inci_expn }}</p>
      </div>
    </div>

    <button @click="addCart(product)" class="btn btn-warning mt-3">가입하기</button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const router = useRouter()
const route = useRoute()
const store = useUserStore()
const productCode = ref(route.params.id)

const product = ref(null)

if (store.nowType === 'deposit') {
  product.value = store.productList_deposit.filter(product => {
    return product.fin_prdt_cd === productCode.value
  })[0]
} else if (store.nowType === 'saving') {
  product.value = store.productList_saving.filter(product => {
    return product.fin_prdt_cd === productCode.value
  })[0]
} else if (store.nowType === 'loan') {
  product.value = store.corpersProducts.filter(product => {
    return product.fin_prdt_cd === productCode.value
  })[0]
}


const joinDenyText = computed(() => {
switch (product.value.join_deny) {
  case 1:
    return '제한없음'
  case 2:
    return '일부제한'
  case 3:
    return '서민전용'
  default:
    return '알 수 없음'
  }
})

const addCart = (product) => {
  store.getCartItems()
  const existingCartItem = store.cartItems.find(item => {
    return item.fin_prdt_cd === product.fin_prdt_cd && item.user === store.userPk
  });

  if (existingCartItem) {
    // If it exists, show a message and prevent adding to the cart
    window.alert('이미 가입된 상품입니다.');
  } else {
    axios({
      method: 'post',
      url: `${store.API_URL}/accounts/carts/`,
      data: {
        kor_co_nm: product.kor_co_nm,
        fin_prdt_nm: product.fin_prdt_nm,
        fin_prdt_cd: product.fin_prdt_cd,
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((res) => {
      console.log(res)
      router.push({ name: 'mypage' })
    })
    .catch((err) => {
      console.log(err)
      Object.keys(err.response.data).forEach((item) => {
        if (err.response.data[item] === 'Invalid token.') {
          window.alert('로그인 후 가입해주세요.')
          router.push({ name: 'login'})
        }
      })
    })
  }
}


</script>

<style scoped>

</style>