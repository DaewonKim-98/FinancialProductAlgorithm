<template>
  <div>
    <p>글 번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>작성자 : {{ article.nickname }}</p>
    <RouterLink :to="{ name: 'article_detail', params: { id: article.id }}">
      상세보기
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
const props = defineProps({
  article: Object
})
console.log(props.article)
</script>
