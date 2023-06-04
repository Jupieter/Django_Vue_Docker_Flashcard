<template>
    <!-- <div v-if="localVisible" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-modal="true" -->
    <div class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-modal="true"
        role="dialog" style="display:block">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1>Modal Content</h1>
                </div>
                <div class="modal-body">
                    <p>{{ data }}</p>
                </div>
              <div class="modal-footer">
                  <button @click="closeModal">Close</button>
              </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ModalTest',
    props: {
        data: String,

    },
    data() {
        return {
        };
    },
    methods: {
        closeModal() {
            console.log("Close");
            this.$emit('close');
        },
    },

}
</script>