<!-- filename: TasksItem.vue -->
<template>
    <div class="add_task">
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
                <button type="submit">Add Task</button>
            </div>
        </form>
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
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>