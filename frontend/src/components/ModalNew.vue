<!-- filename: ModalNew.vue -->
<template>
    <div class="modal fade" id="addSetModal" tabindex="-1" aria-labelledby="addSetModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="addSetModalLabel">Add New Set</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                  <label for="title">Name of New Set</label>
                  <input type="text" class="form-control" id="title" v-model="title">
  
                  <label for="description">Description of New Set</label>
                  <textarea class="form-control" id="description" v-model="description"></textarea>
                </div>
                <div class="modal-footer">
                  <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save</button>
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
              </form>
            </div>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import {ref} from 'vue';
// const title = ref('');
// const description = ref('');

export default {
  name: 'ModalNew',
  data() {
    return {
      title: ref(''),
      description: ref(''),
    };
  },
  methods: {
    submitForm() {
      // Űrlap beküldése és adatok feldolgozása
      // ...
      // Esemény kibocsátása a fő komponens felé
      console.log(this.title)  
      console.log(this.description)  
      const formData = {
        set_name: this.title,
        set_description: this.description
        };

        // axios
        // .post('http://127.0.0.1:8000/api/create_set/', formData)
        // .then(response => {
        //     console.log(response.data);
        //     this.title = '';
        //     this.description = '';
        // })
        // .catch(error => {
        //     console.error(error);
        // });

    //   this.$emit('submit', {
    //     title: this.title,
    //     description: this.description,
    //   });
      // Modális ablak bezárása
      this.close();
    },
    close() {
      this.$emit('close');
    },
  },
};
</script>