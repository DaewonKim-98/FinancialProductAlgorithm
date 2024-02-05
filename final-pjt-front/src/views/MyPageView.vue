<template>
  <div class="m-3 d-flex align-center">
    <a class="fw-bold btn btn-outline-warning" @click.prevent="go_page('cart')" href="#">가입 상품 확인</a>
    <span class="border-end border-warning m-3" style="height: 20px;"></span>
    <a class="fw-bold btn btn-outline-warning" @click.prevent="go_page('update')" href="#">개인 정보 수정</a>
    <span class="border-end border-warning m-3" style="height: 20px;"></span>
    <a class="fw-bold btn btn-outline-warning" @click.prevent="go_page('recommend')" href="#">금융 상품 추천 받기</a>
  </div>
  <div>
    <CartList v-if="showing === 'cart'" />
    <ProfileUpdate v-if="showing === 'update'"/>
    <Recommend v-if="showing === 'recommend'" 
      :go_recommend="go_recommend"
    />
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import CartList from '@/components/CartList.vue'
import ProfileUpdate from '@/components/ProfileUpdate.vue'
import Recommend from '@/components/Recommend.vue'

const store = useUserStore()
const router = useRouter()
const showing = ref('cart')
const go_recommend = ref(false)

const go_page = function (page) {
  // 상품 추천시, 추가 정보 저장이 안되어 있는 신규 고객이면
  if (page === 'recommend') {
    // 얘가 지금 이미 유저의 애드인포가 있는지 없는지 체크해서 반환하는 함수
    // 데이터가 없으면 first를 반환해서 firstRecommend에 저장해
    const data = store.getInfo()
    if ( data !== 'first') {
      showing.value = page
      go_recommend.value = true
    }
  } 
  // 이미 추가 정보가 있는 고객이면 바로 이동
  else {
    showing.value = page
  }

}
</script>

<style scoped>

</style>