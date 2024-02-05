<template>
  <div class="m-3">
    <h1 class="fw-bold">근처 은행 찾기</h1>
    <KakaoMap />
  </div>
</template>

<script>
import KakaoMap from '@/components/KakaoMap.vue';

export default {
  components: {
    KakaoMap,
  },
};
</script>

<style scoped>
/* Add your styling here */
</style>
