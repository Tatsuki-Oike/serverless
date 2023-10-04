<template>

  <h3 class="mt-5"> Home ~ RDSの内容 ~ </h3>
  <div>
    <h3 class="mt-5"> Images </h3>
    <table class="table">
      <thead>
        <tr>
          <th> ID </th>
          <th> Name </th>
          <th> URL </th>
          <th> Image </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="image in image_list" :key="image.image_id">
          <td class="align-middle"> {{ image.image_id }} </td>
          <td class="align-middle"> {{ image.image_name }} </td>
          <td class="align-middle"> {{ image.image_url }} </td>
          <td class="align-middle">
            <img class="img-fluid" :src="image.image_url" alt="Image" style="width: 100px;" />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      image_list: {}
    }
  },
  mounted() {
    axios
      .get(this.$store.state.api_url)
      .then(response => {
        const json_response = response.data;
        this.image_list = json_response["items"]
        console.log("SUCCESS");
      })
      .catch(error => {
        this.response = error;
        console.log("FAIL: ", error);
      });
  },
}
</script>