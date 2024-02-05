<template>
  <div>
    <div class="d-flex justify-content-between m-3">
    <h1 class="fw-bold">추천 상품</h1>
    <button @click.prevent="toggleInfoEdit" class="btn btn-outline-warning">
      {{ isInfoEdit ? '추가 정보 닫기' : '내 추가 정보 수정' }}
    </button>
    </div>
    <!-- 추가 정보 수정용 페이지 -->
    <div v-if="isInfoEdit">
      <div class="d-flex flex-column align-items-center mx-auto" style="width: 500px;">
      <form @submit.prevent="updateInfo">
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
              <button class="btn border dropdown-toggle border border-warning" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                {{ targetPlace }}
              </button>
              <ul class="dropdown-menu border border-warning" style="max-height: 300px; overflow-y: auto;">
                <li v-for="apartment in apartments" :key="apartment.id">
                  <a class="dropdown-item" href="#" @click="selectApartment(apartment.sigu)">{{ apartment.sigu }}</a>
                </li>
              </ul>
            </div>
          </div>
          <div class="input-group flex-nowrap d-flex flex-column position-relative" style="height: 90px;">
            <span class="">목표 입주 시기</span>
            <month-picker-input class="z-3 position-absolute bottom-0" :min-date="new Date()" :default-month="12" lang="ko" v-model.string="moveTime" :no-default="false" :input-pre-filled='false'>
            </month-picker-input>
          </div>
          </div>
          <div class="d-grid gap-2 mt-5">
            <button class="btn btn-warning" type="submit">수정</button>
          </div>
        </form>
      </div>
    </div>

    <!-- 추천된 상품 리스트 -->
    <!-- 내 정보, 해당 거주지 아파트 실거래가, 실거래가 금액 대비 내 자산 -->
    <div class="m-3 border border-warning p-3" style="width: 90%;">
      <p><span class="fw-bold">내 현재 자산 :</span> {{ formatTotalMoney }}</p>
      <p><span class="fw-bold">내 목표 거주지 :</span> {{ targetPlace }}</p>
      <p><span class="fw-bold">{{ targetPlace }}의 아파트 실거래가 :</span> {{ formatAptPrice }}</p>
      <p><span class="fw-bold">내 자산 대비 금액 :</span> {{ formatRemainingMoney }}</p>
    </div>

    <div class="d-flex justify-content-around">
      <div style="width: 45%;" class="p-3 border border-warning ">
        <h3 class="text-center">나와 유사한 고객들이 가입한 상품</h3>
        <p class="text-body-tertiary">※ 나와 같은 거주지를 희망하고 총 자산의 차이가 25% 내외의 사람들</p>
        <!-- 비슷한 사람들의 최다 가입순으로 TOP 10 추천 -->
        <div v-for="(product, index) in topTen" :key="product.fin_prdt_cd">
          <h4 class="fw-bold mb-4">{{ index + 1 }}위</h4>
          <p><span class="fw-bold">회사명 :</span> {{ product.kor_co_nm }}</p>
          <p><span class="fw-bold">상품명 :</span> {{ product.fin_prdt_nm }}</p>
          <button class="light btn btn-warning" @click="goDetail(product)">상세페이지로 이동</button>
          <hr>
        </div>
      </div>
      <div style="width: 45%;" id="carouselExampleIndicators" class="p-3 border border-warning carousel slide">
        <div>
          <h3 class="text-center">나와 가장 유사한 고객들의 정보</h3>
          <p class="text-body-tertiary">※ 나와 같은 거주지를 희망하고 총 자산의 차이의 절댓값이 가장 가까운 5명</p>
          <button style="height: 40px;" class="m-3 carousel-control-prev bg-opacity-1 bg-warning" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button style="height: 40px;" class="m-3 carousel-control-next bg-opacity-1 bg-warning" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
        <div class="carousel-inner" style="margin-top: 50px;">
          <div :class="{ 'carousel-item': true, 'active': index === 0 }" v-for="(userWithCart, index) in userWithCarts" :key="userWithCart.id">
            <div class="d-block w-100"></div>
              <div class="user-info">
                <p><span class="fw-bold">아이디 :</span> {{ userWithCart.id }}</p>
                <p><span class="fw-bold">이름 :</span> {{ userWithCart.nickname }}</p>
                <p><span class="fw-bold">성별 :</span> {{ userWithCart.gender }}</p>
                <p><span class="fw-bold">생년월일 :</span> {{ userWithCart.age }}</p>
                <p><span class="fw-bold">자산 :</span> {{ formatPrice(userWithCart.total_money) }}</p>
                <p><span class="fw-bold">입주 시기 :</span> {{ userWithCart.move_time }}</p>
              </div>
              <hr>
              <div class="user-cart" v-for="user_cart in userWithCart.user_carts" :key="user_cart.fin_prdt_cd">
                <p v-if="user_cart.length === 0">가입한 상품이 없습니다.</p>
                <p><span class="fw-bold">회사명 :</span> {{ user_cart.kor_co_nm }}</p>
                <p><span class="fw-bold">상품명 :</span> {{ user_cart.fin_prdt_nm }}</p>
                <button class="light btn btn-warning" @click="goDetail(user_cart)">상세페이지로 이동</button>
                <hr>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { onMounted, ref, watch, computed, } from 'vue'
import { MonthPickerInput } from 'vue-month-picker'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useUserStore()
const isInfoEdit = ref(false)

const toggleInfoEdit = () => {
  isInfoEdit.value = !isInfoEdit.value
}

const depositMoney = ref(store.userAddInfo['deposit_money'])
const savingMoney = ref(store.userAddInfo['saving_money'])
const totalMoney = ref(store.userAddInfo['total_money'])
const targetPlace = ref(store.userAddInfo['target_place'])
const moveTime = ref(store.userAddInfo['move_time'])
const topTen = ref(null)
const userWithCarts = ref(null)
const aptPrice = ref(null)

const formatTotalMoney = computed(() => {
  if (totalMoney.value >= 10000) {
    const billion = (totalMoney.value / 10000).toFixed(1); // 억 단위로 변환, 소수점 한 자리까지
    return billion.endsWith('.0') ? `${parseInt(billion)}억` : `${billion}억`;
  } else {
    return `${totalMoney.value}만원`;
  }
})

const formatPrice = function (money) {
  if (money >= 10000) {
    const billion = (money / 10000).toFixed(1); // 억 단위로 변환, 소수점 한 자리까지
    return billion.endsWith('.0') ? `${parseInt(billion)}억` : `${billion}억`;
  } else {
    return `${money}만원`;
  }
}

const formatAptPrice = computed(() => {
  if (aptPrice.value >= 10000) {
    const billion = (aptPrice.value / 10000).toFixed(1); // 억 단위로 변환, 소수점 한 자리까지
    return billion.endsWith('.0') ? `${parseInt(billion)}억` : `${billion}억`;
  } else {
    return `${aptPrice.value}원`;
  }
})

const formatRemainingMoney = computed(() => {
  const totalMoneyValue = totalMoney.value * 10000;
  const aptPriceValue = aptPrice.value ? parseFloat(aptPrice.value.toString().replace(/,/g, '')) : 0; // 쉼표 제거
  let remainingMoney = 0;

  console.log(totalMoneyValue, aptPriceValue)

  if (totalMoneyValue >= aptPriceValue) {
    remainingMoney = totalMoneyValue - aptPriceValue
    const formattedRemainingMoney = remainingMoney.toLocaleString(); // 천 단위 쉼표 추가
    return `+${formattedRemainingMoney}원`
  } else {
    remainingMoney = aptPriceValue - totalMoneyValue
    const formattedRemainingMoney = remainingMoney.toLocaleString(); // 천 단위 쉼표 추가
    return `-${formattedRemainingMoney}원`
  }
})

const props = defineProps({
  goRecommend: {
   Type: Boolean
  }
})
console.log(props.goRecommend)

onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/recommends/recommends_products/`,
      params: {
        totalMoney: totalMoney.value,
        targetPlace: targetPlace.value,
      },
      headers: {
        Authorization: `Token ${store.token}`
      },
    })
      .then((res) => {
        console.log(res)
        topTen.value = res.data[0]['top_10_carts']
        userWithCarts.value = res.data[0]['user_with_carts']
        aptPrice.value = res.data[0]['apt_transaction']
      })
      .catch((err) => {
        console.log(err)
      })
  
})


store.apartments()
const apartments = store.apartmentsResult

const selectApartment = (sigu) => {
  targetPlace.value = sigu;
};

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

const updateInfo = function () {
  const payload = {
    depositMoney: depositMoney.value,
    savingMoney: savingMoney.value,
    totalMoney: totalMoney.value,
    targetPlace: targetPlace.value,
    moveTime: moveTime.value,
  }
  store.saveInfo(payload)
  
  console.log(targetPlace.value)
  console.log(totalMoney.value)
  axios({
    method: 'get',
    url: `${store.API_URL}/recommends/recommends_products/`,
    params: {
      totalMoney: totalMoney.value,
      targetPlace: targetPlace.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then((res) => {
      console.log(res)
      topTen.value = res.data[0]['top_10_carts']
      userWithCarts.value = res.data[0]['user_with_carts']
      aptPrice.value = res.data[0]['apt_transaction']
    })
    .catch((err) => {
      console.log(err)
    })
  isInfoEdit.value = !isInfoEdit.value
}
</script>

<style scoped>

</style>