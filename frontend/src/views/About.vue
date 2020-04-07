<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>{{ info }}</p>
  </div>
</template>

<script>
  export default {
    data: () => ({
      info: null
    }),
    mounted() {
      const token = localStorage.getItem('token');
      console.log(token)
      if (token) {
        this.$http.defaults.headers.common['Authorization'] = 'JWT ' + token;
        this.$http.get('http://localhost:8000/api/users')
                  .then(result => (this.info = result))
      }
    }
  }
</script>