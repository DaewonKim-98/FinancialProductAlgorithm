<template>
  <div class="m-3">
    <h1 class="fw-bold">게시글 수정</h1>
    <div class="m-5 d-flex flex-column align-items-center mx-auto" style="width: 500px;">
      <form @submit.prevent="updateArticle">
        <div class="input-group flex-nowrap d-flex flex-column mb-2">
          <span class="mb-2">제목 </span>
          <input v-model.trim="title" type="text" style="width: 500px;" class="rounded-3 form-control" placeholder="제목">
        </div>
        <div class="input-group flex-nowrap d-flex flex-column mb-5" style="height: 200px;">
          <span class="mb-2">내용 </span>
          <input v-model.trim="content" style="width: 500px;" type="text" class="rounded-3 form-control" placeholder="내용">
        </div>
        <div class="d-grid gap-2 mt-3">
          <button class="btn btn-warning" type="submit">작성</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useRouter, useRoute } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useUserStore()
const router = useRouter()
const route = useRoute()

axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`,
  })
    .then((res) => {
      // console.log(res.data)
      title.value = res.data.title
      content.value = res.data.content})
    .catch((err) => {
      console.log(err)
    })

const updateArticle = function () {
  axios({
    method: 'put', 
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
    },
    data: {
      title: title.value,
      content: content.value,
      // Add other fields if necessary
    }
  })
    .then(() => {
      // Redirect to the article detail page or article list page after successful update
      router.push({ name: 'article_detail', params: { id: route.params.id } })
    })
    .catch((err) => {
      console.log(err);
      Object.keys(err.response.data).forEach((item) => {
      if (err.response.data[item] === 'Invalid token.') {
        window.alert('로그인 후 작성해주세요.')
        router.push({ name: 'login'})
      } else if (err.response.data[item][0] === 'This field may not be blank.') {
        window.alert('빈 칸을 채워주세요.')
      } else {
        window.alert('이 게시물에 대한 수정 권한이 없습니다.')
      }
      })
    })
}


</script>

<style>

</style>
