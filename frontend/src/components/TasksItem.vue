<!-- filename: TasksItem.vue -->
<template>
    <div class="container">
        <div class="form">
            <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                  <label for="title">Name of New Set</label>
                  <input type="text" class="form-control" id="title" v-model="title">
  
                  <label for="description">Description of New Set</label>
                  <textarea class="form-control" id="description" v-model="description"></textarea>
                </div>
                <div class="modal-footer">
                  <button type="submit" class="btn btn-primary">Save</button>
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </form>
        </div>
    </div>

    <div class="tasks_container">
        <div class="tasks_content">
            <h1>Cards</h1>
            <ul class="tasks_list">
                <li v-for="task in tasks" :key="task.id" class="card">
                    <h2>{{ task.id}} - {{ task.set_name }}</h2>
                    <p>{{ task.set_description}}</p>
                    <button @click="toggleTask(task)">
                        {{ task.completed ? 'Undo' : 'Complete' }}
                    </button>
                    <p></p>
                    <!-- <button @click="deleteTask(task)">Delete</button> -->
                </li>
            </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        tasks: [],
        selectedTasks: [],
        title: '',
        description: ''
      };
    },
    methods: {
      async getData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/all_set/');
          this.tasks = response.data;
        } catch (error) {
          console.log(error);
        }
      },
      submitForm() {
        const formData = {
          set_name: this.title,
          set_description: this.description
        };
  
        axios
          .post('http://127.0.0.1:8000/api/create_set/', formData)
          .then(response => {
            console.log(response.data);
            this.title = '';
            this.description = '';
            this.getData();
          })
          .catch(error => {
            console.error(error);
          });
      },
      deleteTask(task) {
        const url = `http://127.0.0.1:8000/api/delete_set/${task.id}`;
        axios
          .delete(url)
          .then(response => {
            console.log(response.data);
            this.getData();
            console.log(this.selectedTasks);
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    created() {
      this.getData();
    }
  };
  </script>

<style>
.container-form {
  display: flex;
  justify-content: center;
}

.form {
  width: 33%;
  max-width: 1024px;
}



@media (max-width: 1024px) {
  .form {
    width: 80%;
  }
}

.submit_button {
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
}
</style>