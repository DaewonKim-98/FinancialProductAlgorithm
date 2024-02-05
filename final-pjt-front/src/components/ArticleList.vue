<template>
  <div class="mt-5">
    <table class="table table-hover">
      <thead class="border-warning table-warning">
        <tr>
          <th>글 번호</th>
          <th>제목</th>
          <th>작성자</th>
          <th>가입상품 개수</th>
        </tr>
      </thead>
      <tbody class="table-group-divider">
        <tr class="" v-for="article in store.articles" :key="article.id" @click="goToDetail(article.id)">
          <td style="width: 10px;">{{ article.id }}</td>
          <td style="width: 50px;">{{ article.title }}</td>
          <td style="width: 10px;">{{ article.nickname }}</td>
          <td style="width: 10px;">{{ article.carts.length }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const goToDetail = (id) => {
  router.push({ name: 'article_detail', params: { id: id } })
}
</script>

<style scoped>

</style>