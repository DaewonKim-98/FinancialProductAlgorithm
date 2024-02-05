<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from './stores/user';

const store = useUserStore()
const logout = function () {
  store.logout()
}
</script>

<template>
  <header class="d-flex justify-content-between border-bottom" style="background-color: #FFA500">
    <!-- 내비게이션 바 -->
      <div>
      <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
          <RouterLink class="fw-bold fs-3 navbar-brand ms-3 me-5 text-white" :to="{ name: 'home' }" style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">메인 페이지</RouterLink>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse ms-5" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item me-5">
                <RouterLink class="fw-bold fs-4 nav-link active text-white" :to="{ name: 'search' }" style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">금융 상품 조회</RouterLink>
              </li>
              <li class="nav-item me-5">
                <RouterLink class="fw-bold fs-4 nav-link active text-white" :to="{ name: 'exchangeRateView' }" style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">환율 계산기</RouterLink>
              </li>
              <li class="nav-item me-5">
                <RouterLink class="fw-bold fs-4 nav-link active text-white" :to="{ name: 'maps' }" style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">주변 은행 검색</RouterLink>
              </li>
              <li class="nav-item me-5">
                <RouterLink class="fw-bold fs-4 nav-link active text-white" :to="{ name: 'article' }" style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">자유 게시판</RouterLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      </div>
      <!-- 회원관리 -->
      <div class="align-self-end m-2">
        <div v-if="!store.isLogin" class="d-flex align-center">
          <RouterLink class="fw-bold btn btn-outline-light" :to="{ name: 'login' }">로그인</RouterLink>
          <span class="border-end border-light m-3" style="height: 20px;"></span>
          <RouterLink class="fw-bold btn btn-outline-light" :to="{ name: 'signup' }">회원가입</RouterLink>
        </div>
        <div v-else class="d-flex align-center">
          <RouterLink class="fw-bold btn btn-outline-light" :to="{ name: 'mypage'}">마이페이지</RouterLink>
          <span class="border-end border-light m-3" style="height: 20px;"></span>
          <RouterLink class="fw-bold btn btn-outline-light" @click="logout" :to="{ name: 'home' }">로그아웃</RouterLink>
        </div>
      </div>
  </header>
  <RouterView />
</template>

<style>
body {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>