<template>
  <div class="m-3">
    <h1 class="fw-bold">게시글 작성</h1>
    <div class="m-5 d-flex flex-column align-items-center mx-auto" style="width: 500px;">
      <form @submit.prevent="createArticle">
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
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useUserStore()
const router = useRouter()

const createArticle = function () {
  console.log(store.nickname)
  axios({
    method: 'post',
    url: `${store.API_URL}/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
        Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'article' })
    })
    .catch((err) => {
      console.log(err)
      Object.keys(err.response.data).forEach((item) => {
        if (err.response.data[item] === 'Invalid token.') {
          window.alert('로그인 후 작성해주세요.')
          router.push({ name: 'login'})
        } else if (err.response.data[item][0] === 'This field may not be null.') {
          window.alert('빈 칸을 채워주세요.')
        } 
      })
    })
}



</script>

<style>

</style>
