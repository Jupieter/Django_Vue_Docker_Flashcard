<!-- filename: TasksItem.vue -->
<template>
    <div class="container">
        <div class="form">
            <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                    <label for="title">Title</label>
                    <input type="text" class="form-control" id="title" v-model="title">
                </div>
                <div class="form-group">
                    <label for="description">Description</label>
                    <textarea class="form-control" id="description" v-model="description"></textarea>
                </div>
                <div class="form-group">
                    <button class= "button submit_button" type="submit">Add New Set</button>
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
</template>

<script>
    import axios from 'axios';
    
    export default {
        data() {
            return {
                // tasks
                tasks: [],
                title: '',
                description: ''
            }
        },
        methods: {
            async getData() {
                try {
                    console.log("Try to get data:");
                    // fetch tasks
                    const response = await axios.get('http://127.0.0.1:8000/api/all_set/');
                    // set the data returned as tasks
                    console.log(response);
                    this.tasks = response.data; 
                    console.log(this.tasks);

                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },

            submitForm() {
                // Form adatok elküldése a szerverre
                const formData = {
                    set_name: this.title,
                    set_description: this.description,
                };

                // AJAX kérés küldése a szerverre
                console.log(formData);
                axios
                    .post('http://127.0.0.1:8000/api/create_set/', formData)
                    .then(response => {
                    // Sikeres válasz esetén itt dolgozhatod fel a választ
                    console.log(response.data);
                    })
                    .catch(error => {
                    // Hiba esetén itt kezelheted a hibát
                    console.error(error);
                    });
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>

<style>
.container {
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
</style>