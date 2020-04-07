import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueSession from 'vue-session'
import axios from 'axios'

Vue.use(VueSession)

Vue.config.productionTip = false
Vue.prototype.$http = axios

let token = localStorage.getItem('token')
if(token){
  Vue.prototype.$http.defaults.headers.common['Authorization'] = 'JWT ' + token;
}

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
