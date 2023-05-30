<!-- filename: TasksItem.vue -->
<template>
    <div>
      <nav class="navbar navbar-expand-sm navbar-light bg-light">
        <div class="container">
          <a class="navbar-brand" href="#">Flash Card</a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link" href="#">Card Sets</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Study</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  
      <!-- Add Set Modal -->
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
                  <button type="submit" class="btn btn-primary">Save</button>
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Card Sets -->
      <div class="container-lg">
        <div class="content">
            <h4></h4>
            <h1>Card Sets 
            <button class="btn btn-primary" href="#" data-bs-toggle="modal" data-bs-target="#addSetModal">New</button>
            </h1>
            <ul class="list-group">
                <li v-for="task in tasks" :key="task.id" class="card">
                <div class="card-header bg-gray border-sdarkgrey">
                    <div class="row">
                    <div class="col-1 d-flex justify-content-center">
                        <input type="checkbox" v-model="task.checked" @change="updateCheckedStatus(task)">
                    </div>
                    <div class="col-9 d-flex justify-content-start">
                        <h5 class="card-title">{{ task.id}} - {{ task.set_name }}</h5>
                    </div>
                    <div class="col-2 d-flex justify-content-end">
                        <button class="btn btn-danger" type="button" @click="deleteTask(task)">Del</button>
                    </div>
                    </div>
                </div>
                <div class="card-body">
                    <p>{{ task.set_description}}</p>
                </div>
                </li>
            <br>
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
    updateCheckedStatus(task) {
      const url = `http://127.0.0.1:8000/api/set_checked/${task.id}`;
      axios
        .post(url)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
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