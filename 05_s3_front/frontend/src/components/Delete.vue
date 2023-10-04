<template>

    <h3 class="mt-5"> Delete ~ S3のファイル消去 + RDSのデータ消去 ~ </h3>

    <!-- 画像のID入力 -->
    <div class="row g-3 align-items-center">
      <div class="col-2">
        <label for="inputPassword6" class="col-form-label"> Image ID </label>
      </div>
      <div class="col-10">
        <input v-model="image_id" type="text" class="form-control mb-2" id="inputPassword6" placeholder="image_id">
      </div>
    </div>
    
    <!-- 消去ボタン -->
    <div class="d-grid gap-2 mt-2">
            <button @click="deleteFileContent" class="btn btn-primary btn-block py-1"> Delete Image File </button>
    </div>

  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'App',
    data() {
      return {
        image_id: "",
      }
    },
    methods: {
      async deleteFileContent() {
        
        // URL作成
        const url = `${this.$store.state.api_url}?image_id=${this.image_id}`

        // 消去リクエスト
        axios
          .delete(url)
          .then(response => {
            const json_response = response.data;
            console.log(json_response)
            console.log("SUCCESS");
          })
          .catch(error => {
            this.response = error;
            console.log("FAIL: ", error);
          });
      },
    },
  };
  </script>
  