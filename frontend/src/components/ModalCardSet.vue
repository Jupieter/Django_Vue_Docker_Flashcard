<!-- filename: ModalCardSet.vue -->
<template>
  <div class="modal fade show" id="addSetModal" tabindex="-1" aria-modal="true" aria-labelledby="addSetModalLabel"
    style="display:block">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="addSetModalLabel">{{ cardSet.id ? 'Edit Set' : 'Add New Set' }}</h5>
          <button type="button" class="btn-close" @click="close()" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form v-on:submit.prevent="cardSet.id ? submitSetForm() : submitNewForm()">
            <div class="form-group">
              <label for="title">Name of Set</label>
              <input type="text" class="form-control" id="title" v-model="cardSet.set_name">

              <label for="description">Description of Set</label>
              <textarea class="form-control" id="description" v-model="cardSet.set_description"></textarea>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-primary">{{ cardSet.id ? 'Update' : 'Add New' }}</button>
              <button type="button" class="btn btn-secondary" @click="close()">Close</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: 'ModalCardSet',
  props: {
    cardSet: Object,
  },
  // data() {
  //   return {
  //     title: ref(''),
  //     description: ref(''),
  //   };
  // },
  methods: {
    submitNewForm() {
      const formData = {
        set_name: this.cardSet.set_name,
        set_description: this.cardSet.set_description
      };
      axios
        .post(`${import.meta.env.VITE_APP_API_URL}create_set/`, formData)
        .then(response => {
          console.log(response.data.message);
          this.cardSet.set_name = '';
          this.cardSet.description = '';
          if (response) { this.close() };
        })
        .catch(error => {
          console.error(error);
        });
      // Modális ablak bezárása
      // this.close();
    },

    submitSetForm() {
      let formData = {
        set_name: this.cardSet.set_name,
        set_description: this.cardSet.set_description
      };
      let url = `${import.meta.env.VITE_APP_API_URL}set_updated/${this.cardSet.id}`;
      axios
        .post(url, formData)
        .then(response => {
          console.log(response.data.message);
          if (response) { this.close() };
        })
        .catch(error => {
          console.error(error);
        });
    },

    close() {
      this.$emit('close');
    },
  },
};
</script>