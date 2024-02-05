<template>
  <div class="m-3">
    <h1 class="fw-bold">자유 게시판</h1>
    <RouterLink class="fw-bold btn btn-outline-warning" :to="{ name: 'article_create' }">
      게시글 작성하기
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useUserStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
