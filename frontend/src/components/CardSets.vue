<!-- filename: CardSets.vue -->
<template>
  <ModalNew v-show="showModalNew" @submit="handleModalSubmit" @close="closeModalNew" />
      
  <!-- <AlertDefault  variant="success" :msg="msg" :visible="visible"> -->
    <!-- <p class="text-center">{{ msg }}</p> -->
  <!-- </AlertDefault> -->
  <AlertDefault  variant="success" :visible="visible">
    Test 1
  </AlertDefault>

  <!-- Card Sets -->
  <div class="container-lg">
    <div class="content">
        <h4></h4>
        <h1>Card Sets 
          <button class="btn btn-primary" href="#" @click="openModalNew()">Open Modal</button>
          <button class="btn btn-primary" href="#" data-bs-toggle="modal" data-bs-target="#addSetModal">New</button>
        </h1>
        <ul class="list-group">
            <li v-for="card_set in tasks" :key="card_set.id" 
            class="card mb-3 custom-gradient">
            <div class="card-header bg-gray border-sdarkgrey">
              <div class="row">
                <div class="col-1 text-center">
                  <div class="form-check form-switch">
                    <input class="form-check-input" 
                      type="checkbox" 
                      v-model="card_set.checked" 
                      @change="updateCheckedStatus(card_set)">
                  </div>
                </div>
                <div class="col-8">
                    <h5 class="card-title">{{ card_set.id}} - {{ card_set.set_name }}</h5>
                </div>
                <div class="col-3">
                  <div class="btn-group ">
                    <button class="btn btn-secondary me-2" type="button" @click="updateSet(card_set)">
                      <font-awesome-icon :icon="['fas', 'pen']" />
                    </button>
                    
                    <button class="btn btn-danger " type="button" @click="deleteSet(card_set)">
                      <font-awesome-icon :icon="['fas', 'trash']" /> 
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="card-body text-left">
                <p class="text-left">{{ card_set.set_description}}</p>
            </div>
            </li>
        <br>
      </ul>
    </div>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  import ModalNew from './ModalNew.vue';
  import AlertDefault from './AlertDefault.vue';
  
  export default {
    name: "CardSets",
    components: {
      AlertDefault,
      ModalNew,
    },

    data() {
      return {
        isModalVisible: false,
        showModalNew: false,
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
        openModalNew() {
          this.showModalNew = true;
          console.log("Modal open");
        },
        handleModalSubmit(data) {
          // Új adatok feldolgozása
          console.log(data);
          // ...
          // Modális ablak bezárása
          // this.closeModal();
        },
        closeModalNew() {
          this.showModalNew = false;
        },
        showModal() {
          this.isModalVisible = true;
        },
        closeModal() {
          this.isModalVisible = false;
        },
        
        deleteSet(card_set) {
            const url = `http://127.0.0.1:8000/api/delete_set/${card_set.id}`;
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
        },
        updateSet(card_set) {
            const url = `http://127.0.0.1:8000/api/set_updated/${card_set.id}`;
            console.log(card_set);

            axios
            .put(url, card_set)
            .then(response => {
                console.log(response.data);
                this.getData();
            })
            .catch(error => {
                console.error(error);
            });
        },
        updateCheckedStatus(card_set) {
            const url = `http://127.0.0.1:8000/api/set_checked/${card_set.id}`;
            axios
                .post(url)
                .then(response => {
                    console.log(response.data);
                    })
                    .catch(error => {
                        console.error(error);
                        });
            },
                
        },
        created() {
        this.getData();
        }
    };
  </script>

<style>
.card {
  padding: 0.5em;
}
.btn {
  padding: 5px;
  margin: 5px;
}
.custom-gradient {
  background: linear-gradient(to bottom right, #FFD700, #ff9900);
}
</style>