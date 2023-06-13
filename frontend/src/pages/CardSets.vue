<!-- filename: CardSets.vue -->
<template>
  <ModalCardSet v-if="isNewVisible" :cardSet="cardSetData" @close="closeModalNew" />


  <!-- <AlertDefault  variant="success" :msg="msg" :visible="visible"> -->
  <!-- <p class="text-center">{{ msg }}</p> -->
  <!-- </AlertDefault> -->
  <div class="d-flex flex-row justify-content-between">
    <div class="p-2">
      <AlertDefault variant="success" :visible="isAlertVisible" @close="closeModalAlert">
        Test 1
      </AlertDefault>
      <button class="btn btn-primary" href="#" @click="showModalAlert()" @close="closeModalAlert">
        Open Test 2
      </button>
      {{ isAlertVisible }}
    </div>
    <div class="p-2">
      <!-- <ModalTest :isVisible="isTestVisible" :data="modalData" @close="closeModalTest" /> -->
      <ModalTest v-if="isTestVisible" :data="modalData" @close="closeModalTest" />
      <button class="btn btn-secondary" @click="openModalTest('Hello')" @close="closeModalTest">
        Open Short Modal
      </button>
      {{ isTestVisible }}
    </div>
  </div>


  <!-- Card Sets -->
  <div class="container-lg">
    <div class="content">
      <h4></h4>
      <h1>Card Sets
        <button class="btn btn-primary" href="#" @click="openModalNew()">
          <font-awesome-icon :icon="['fas', 'plus']" />
        </button>
      </h1>

      <ul class="list-group">
        <li v-for="card_set in tasks" :key="card_set.id" class="card mb-3 custom-gradient">
          {{ card_set }}
          <div class="card-header bg-gray border-sdarkgrey">
            <div class="d-flex flex-row justify-content-between">
              <div class="p-2">
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" v-model="card_set.checked"
                    @change="updateCheckedStatus(card_set)">
                </div>
              </div>
              <div class="p-2">
                <h5 class="card-title">{{ card_set.id }} - {{ card_set.set_name }}</h5>
              </div>
              <div class="p-2">
                <div class="btn-group ">
                  <button class="btn btn-secondary me-2" type="button" @click="openModalSetOrNew(card_set)">
                    <font-awesome-icon :icon="['fas', 'pen']" />
                  </button>

                  <button class="btn btn-danger " type="button" @click="confirmDelete(card_set)">
                    <font-awesome-icon :icon="['fas', 'trash']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="card-body text-left">
            <p class="text-left">{{ card_set.set_description }}</p>
          </div>
        </li>
        <br>
      </ul>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
import ModalCardSet from '../components/ModalCardSet.vue';
import ModalTest from '../components//ModalTest.vue';
import AlertDefault from '../components//AlertDefault.vue';
import { useUserStore } from '../../stores/user'


export default {
  name: "CardSets",
  components: {
    AlertDefault,
    ModalCardSet,
    ModalTest,
  },
  data() {
    return {
      isAlertVisible: false,
      isNewVisible: false,
      tasks: [],
      selectedTasks: [],
      isTestVisible: false,
      modalData: null,
      cardSetData: null,
    };
  },

  methods: {
    async getData() {
      try {
        console.log("getData");
        // const response = await axios.get('http://127.0.0.1:8000/api/all_set/');
        const response = await axios.get(`${import.meta.env.VITE_APP_API_URL}all_set/`);
        this.tasks = response.data;
      } catch (error) {
        console.log(error);
      }
    },




    openModalNew() {
      console.log("New open");
      const card_set = {
        id: null,
        set_name: "",
        set_description: "",
        checked: "false"
      }
      this.openModalSetOrNew(card_set)
    },
    openModalSetOrNew(card_set) {
      console.log("Set or New open");
      this.cardSetData = card_set
      this.isNewVisible = true;
    },
    closeModalNew() {
      this.getData();
      this.isNewVisible = false;
    },


    showModalAlert() {
      console.log("Alert Modal open");
      this.isAlertVisible = true;
    },
    closeModalAlert() {
      console.log("Alert Modal open");
      this.isAlertVisible = false;
    },


    openModalTest(data) {
      console.log(data);
      this.modalData = data;
      this.isTestVisible = true;
    },
    closeModalTest() {
      console.log("Close Test");
      this.modalData = null;
      this.isTestVisible = false;
    },

    confirmDelete(card_set) {
      if (confirm('Are you sure you want to delete it?')) {
        this.deleteSet(card_set);
      }
    },

    deleteSet(card_set) {
      const url = `${import.meta.env.VITE_APP_API_URL}delete_set/${card_set.id}`;
      axios
        .delete(url)
        .then(response => {
          console.log(response.data);
          if (response) { this.getData() };
          console.log(this.selectedTasks);
        })
        .catch(error => {
          console.error(error);
        });
    },

    updateCheckedStatus(card_set) {
      const url = `${import.meta.env.VITE_APP_API_URL}set_checked/${card_set.id}`;
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