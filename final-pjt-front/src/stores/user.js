import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const articles = ref([])
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const userPk = ref(null)
  const cartItems = ref([])

  const signup = function (payload) {
    const { username, password1, password2, nickname, gender, age } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
        nickname,
        gender,
        age
      }
    })
      .then((res) => {
        router.push({ name: 'login' })
      })
      .catch((err) => {
        Object.keys(err.response.data).forEach((item) => {
          if (err.response.data[item][0] === 'A user with that username already exists.') {
            window.alert('이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.')
          } else if (err.response.data[item][0] === "This password is too short. It must contain at least 8 characters.") {
            window.alert('비밀번호는 최소 8자리 이상이어야 합니다.')
          } else if (err.response.data[item][0] === "The two password fields didn't match.") {
            window.alert('비밀번호가 일치하지 않습니다.')
          } else if (err.response.data[item][0] === 'This field may not be null.') {
            window.alert('빈 칸을 채워주세요')
          } else if (err.response.data[item][0] === 'This password is too common.') {
            window.alert('비밀번호를 조금 더 강력하게 해주세요.')
          }
        })
      })
  }

  const login = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      }
    })
      .then((res) => {
        router.push({ name: 'home' })
        token.value = res.data.key
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
              Authorization: `Token ${token.value}`
          }
        })
          .then((res) => {
            userPk.value = res.data.pk
          })
          .catch((err) => {
            console.log(err)
          })
      })
      .catch((err) => {
        window.alert('아이디와 비밀번호를 확인하세요.')
      })
  }

  const logout = function() {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const banks = ref(null)
  const pullBankList = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/bank-list/`,
    })
      .then((res) => {
        banks.value = ['전체 선택', ...res.data]
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const productList_deposit = ref([])
  const pullProductList_deposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/deposit-products/`,
    })
    .then((res) => {
      return res.data
    })
    .then((res) => {
      const products = ref([])
      res.forEach(product => {
        const product_cd = product.fin_prdt_cd
        // 옵션 가져오기
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/deposit-product-options/${product_cd}/`,
        })
        .then((res) => {
              product['6'] = '-'
              product['12'] = '-'
              product['24'] = '-'
              product['36'] = '-'
              res.data.forEach((item) => {
                product[item.save_trm.toString()] = item.intr_rate
              })
              
              // console.log(product)
              products.value.push(product)
            })
            .catch((err) => {
              console.log(err)
            })
          })
          productList_deposit.value = products.value
        })
        .catch((err) => {
          console.log(err)
        })
  }
  const productList_saving = ref([])
  const pullProductList_saving = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/saving-products/`,
    })
    .then((res) => {
      return res.data
    })
    .then((res) => {
      const products = ref([])
      res.forEach(product => {
        const product_cd = product.fin_prdt_cd
        // 옵션 가져오기
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/saving-product-options/${product_cd}/`,
        })
        .then((res) => {
              product['6'] = '-'
              product['12'] = '-'
              product['24'] = '-'
              product['36'] = '-'
              res.data.forEach((item) => {
                product[item.save_trm.toString()] = item.intr_rate
              })
              
              // console.log(product)
              products.value.push(product)
            })
            .catch((err) => {
              console.log(err)
            })
          })
          productList_saving.value = products.value
        })
        .catch((err) => {
          console.log(err)
        })
  }

  const nowType = ref('deposit')

  const searchProduct = ref(productList_deposit.value)
  const searchDeposit = function (bank, period, productKind) {
    nowType.value = productKind
    let productList = productList_deposit.value
    if (productKind === 'saving') {
      productList = productList_saving.value
    } else if (productKind === 'loan') {
      productList = corpersProducts.value
    } else {
      productList = productList_deposit.value
    }
    if (bank === '전체 선택' && period !== '전체 선택' && productKind !== 'loan') {
      const re_period = period.replace(/\D/g, '')
      const filteredProducts = productList.filter(product => {
        return product[re_period] !== '-' })
      searchProduct.value = filteredProducts
    } else if (period === '전체 선택' && bank !== '전체 선택' && productKind !== 'loan') {
      const filteredProducts = productList.filter(product => {
        return product.kor_co_nm === bank })
      searchProduct.value = filteredProducts
    } else if (period === '전체 선택' && bank === '전체 선택') {
      searchProduct.value = productList
    } else if (period !== '전체 선택' && bank !== '전체 선택' && productKind !== 'loan') {
      const re_period = period.replace(/\D/g, '')
      const filteredProducts = productList.filter(product => {
        return product.kor_co_nm === bank && product[re_period] !== '-' })
      searchProduct.value = filteredProducts
    } else if (period === '전체 선택' && bank !== '전체 선택') {
      const filteredProducts = productList.filter(product => {
        return product.kor_co_nm === bank })
      searchProduct.value = filteredProducts
    } else if (period !== '전체 선택' && bank === '전체 선택') {
      const filteredProducts = productList.filter(product => {
        return product[period] !== '-' })
      searchProduct.value = filteredProducts
    } else if (period !== '전체 선택' && bank !== '전체 선택') {
      const filteredProducts = productList.filter(product => {
        return product[period] !== '-' && product.kor_co_nm === bank })
      searchProduct.value = filteredProducts
    }

    }

  const countries = ref(null)
  const countries_form = ref(null)
  const saveExchangeData = function () {
    // 환율 데이터가 없는경우
    if (countries.value === null || countries_form.value === null) {
    axios({
      method: 'get',
      url: `${API_URL}/exchanges/pull-exchanges/`,
    })
    .then((res) => {
      countries.value = res.data
    })
    .then(() => {
      axios({
        method: 'get',
        url: `${API_URL}/exchanges/pull-list/`,
      })
      .then((res) => {
        countries_form.value = res.data
      })      

    })
    .catch((err) => console.log(err))
    }
  }

  const getExchangeRate = function (currency) {
    const lastThreeChars = currency.match(/\[(.*?)\]$/)[1]
    const filteredExchangeRate = countries.value.filter(exchanges => {
      return exchanges.cur_unit === lastThreeChars })[0].deal_bas_r

    const result = parseInt(filteredExchangeRate.replace(/,/g, ''))
    if ( lastThreeChars === 'JPY(100)' || lastThreeChars === 'IDR(100)' ) {
      return result * 100
    } else {
      return result
    }
    
  }

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const saveInfo = function (payload) {
    const { depositMoney, savingMoney, totalMoney, targetPlace, moveTime } = payload
    axios({
      method: 'post',
      url: `${API_URL}/recommends/save-info/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        depositMoney,
        savingMoney,
        totalMoney,
        targetPlace,
        moveTime
      }
    })
      .then((res) =>{
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const userAddInfo = ref(null)
  const getInfo = function () {
    axios({
      method: 'get',
      url: `${API_URL}/recommends/save-info/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
      .then((res) =>{
        userAddInfo.value = res.data
        if (res.data === 'first') {
          router.push({ name: 'addInfo' })
        } else {
          return res.data
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getCartItems = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/carts/`,
      headers: {
          Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        cartItems.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const corpers = ref(null)
  const pullCorperList = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/corper-list/`,
    })
      .then((res) => {
        corpers.value = ['전체 선택', ...res.data]
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const corpersProducts = ref([])
  const pullProductList_loan = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/mortgage-loan-products/`,
    })
    .then((res) => {
      return res.data
    })
    .then((res) => {
      const products = ref([])
      res.forEach(product => {
        const product_cd = product.fin_prdt_cd
        // 옵션 가져오기
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/mortgage-loan-product-options/${product_cd}/`,
        })
        .then((res) => {
          product['고정금리'] = '-'
          product['변동금리'] = '-'

          res.data.forEach((item) => {
            product[item.lend_rate_type_nm] = item.lend_rate_min
          })
          
          products.value.push(product)
        })
        .catch((err) => {
          console.log(err)
        })
      })
      corpersProducts.value = products.value
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const apartmentsResult = ref(null)
  const apartments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/recommends/apart`,
    })
    .then((res) => {
      console.log(res)
      apartmentsResult.value = res.data
      console.log(apartmentsResult)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const saveData = ref(false)

  return { API_URL, signup, login, token, isLogin, logout, 
    pullBankList, banks, productList_deposit, pullProductList_deposit,
    productList_saving, pullProductList_saving, searchDeposit, searchProduct,
    countries_form, saveExchangeData, getExchangeRate, getArticles, articles,
    saveInfo, getInfo, userPk, cartItems, getCartItems, userAddInfo, pullCorperList, 
    corpers, corpersProducts, pullProductList_loan, apartments, nowType,
    apartmentsResult, saveData
  }
}, { persist: true })
