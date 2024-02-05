<template>
  <div class="m-3">
    <h1 class="fw-bold">게시글 상세</h1>
    <div v-if="article" class="mt-5 card border border-warning">
      <div class="card-body pb-0">
        <p class="fs-4"><span class="fw-bold">제목 : </span> {{ article.title }}</p>
        <p class="fs-4"><span class="fw-bold">작성자 : </span> {{ article.nickname }}</p>
        <p class="fs-4"><span class="fw-bold">내용 :</span> {{ article.content }}</p>
      </div>
      <div class="card-body py-0">
        <hr class="border-warning">
        <h5 class="fw-bold pb-3">{{ article.nickname }}님의 가입 상품 리스트</h5>
        <div class="d-flex flex-wrap">
          <div v-for="product in article.carts" :key="product.id" class="card m-2 border-warning" style="width: 500px;">
            <div class="card-body">
              <p class="card-text"><span class="fw-bold me-2">회사명 :</span> {{ product.kor_co_nm }}</p>
              <p class="card-text"><span class="fw-bold me-2">상품명 :</span> {{ product.fin_prdt_nm }}</p>
              <p class="card-text"><span class="fw-bold me-2">가입시기 :</span> {{ product.created_at.slice(0, 10) }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="mt-3 d-flex align-center">
      <a class="fw-bold btn btn-outline-warning" @click.prevent="updateArticle()" href="#">게시물 수정하기</a>
      <span class="border-end border-warning m-3" style="height: 20px;"></span>
      <a class="fw-bold btn btn-outline-warning" @click.prevent="deleteArticle()" href="#">게시물 삭제하기</a>
      <span class="border-end border-warning m-3" style="height: 20px;"></span>
      <a class="fw-bold btn btn-outline-warning" @click.prevent="goArticleList()" href="#">게시물 목록으로</a>
    </div>

      <form @submit.prevent="createComment" class="mt-5">
        <label for="comment" class="mb-1 fs-4">댓글 작성</label>
        <input v-model="newComment" type="text" id="comment" class="rounded-3 form-control border border-warning"/>
        <button class="btn btn-warning mt-3" type="submit">작성하기</button>
      </form>

      <div v-if="comments" class="mt-5">
        <h2>댓글 리스트</h2>
        <ul>
          <li v-for="comment in comments" :key="comment.id">
            <p class="fs-5 m-1">{{ comment.content }} </p>
            <button @click="deleteComment(comment.id)" class="btn btn-warning">삭제하기</button>
          </li>
        </ul>
      </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const store = useUserStore()
const route = useRoute()
const article = ref(null)
const newComment = ref('')
const comments = ref(null)

const getArticlesComments = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`,
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
      article.value.created_at = article.value.created_at.substr(0, 10)
      article.value.updated_at = article.value.updated_at.substr(0, 10)
    })
    .catch((err) => {
      console.log(err)
    })

  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/comments/`,
  })
    .then((res) => {
      // console.log(res.data)
      comments.value = res.data
    })
    .catch((err) => {
      if (err.response.data.detail === 'Not found.') {
        comments.value = null
      }
    })
}

onMounted(() => {
  getArticlesComments()
})

const deleteArticle = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/${article.value.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      router.push({name: 'article'})
      console.log(res.data)
    })
    .catch((err) => {
      console.log(err)
      Object.keys(err.response.data).forEach((item) => {
        if (err.response.data[item] === '이 게시물에 대한 삭제 권한이 없습니다.') {
          window.alert("이 게시물에 대한 삭제 권한이 없습니다.")
          router.push({ name: 'article'})
        }
      })
    })
}

const updateArticle = function () {
  router.push({ name: 'article_update',
    params: { id: article.value.id },
  })
}


const goArticleList = function () {
  router.push({ name: 'article' })
}

const createComment = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/articles/${article.value.id}/comments/`,
      headers: {
          Authorization: `Token ${store.token}`
      },
      data: {
        content: newComment.value
      }
    })
      .then(() => {
        getArticlesComments()
        newComment.value = ''
      })
      .catch((err) => {
        console.log(err)
      })
  }

const deleteComment = function (commentId) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/${article.value.id}/comments/${commentId}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      getArticlesComments()
    })
    .catch((err) => {
      console.log(err)
      window.alert("이 댓글에 대한 삭제 권한이 없습니다.")
    })
}

</script>

<style>

</style>
