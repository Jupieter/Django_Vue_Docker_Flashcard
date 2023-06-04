<!-- filename: AlertDefault.vue -->

<template>
  <div>
    <!-- Modal -->
    <div v-if="OpenClose" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-modal="true"
      role="dialog" style="display:block">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
              <h3>Alert:</h3>
            <button type="button" @click="CloseFun()" class="btn-close"></button>
          </div>
          <div class="modal-body">
            <slot></slot>
          </div>
          <div class="modal-footer">
            <button type="button" @click="CloseFun()" :class="'btn btn-' + variant">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- <button type="button" @click="OpenCloseFun()" :class="'btn btn-' + variant">Open modal</button> -->
</template>

<script>
export default {
  name: 'AlertDefault',
  props: {
    visible: Boolean,
    variant: String,
  },
  data() {
    return {
      OpenClose: false,
    }
  },
  methods: {
    OpenFun() {
      this.visible = true;
    },
    CloseFun() {
      this.OpenClose = false;
      this.$emit('close');
    },
  },
  watch: {
    visible: function (newVal, oldVal) { // watch it
      this.OpenClose = newVal;
      console.log('new' + newVal + '==' + oldVal)
    }
  }

}
</script>
