<!-- filename: AlertDefault.vue -->

<template>
  <div>
    <!-- Modal -->
    <div v-if="OpenClose" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-modal="true"
      role="dialog" style="display:block">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">

            <button type="button" @click="OpenCloseFun()" class="btn-close"></button>
          </div>
          <div class="modal-body">
            <slot></slot>
          </div>
          <div class="modal-footer">
            <button type="button" @click="OpenCloseFun()" :class="'btn btn-' + variant">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <button type="button" @click="OpenCloseFun()" :class="'btn btn-' + variant">Open modal</button>
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
      OpenClose: this.visible
    }
  },
  methods: {
    OpenCloseFun() {
      this.OpenClose = !this.OpenClose;
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
