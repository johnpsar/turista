<template>
  <div
    class="modal"
    @click.self.stop="emit('closeModal')"
  >
    <div class="modal-window">
      <div class="modal-window-header">
        <slot name="header" />
      </div>
      <div class="modal-window-content">
        <slot name="content" />
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onBeforeUnmount } from "vue";

const emit = defineEmits<{
  (e: "closeModal"): void;
}>();

onMounted(() => {
  document.body.style.overflowY = "hidden";
});

onBeforeUnmount(() => {
  document.body.style.overflowY = "initial";
});
</script>

<style lang="scss" scoped>
.modal {
  background: rgba(18, 22, 33, 0.8);
  z-index: 999;
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  &-window {
    background: #9dd9d299;
    position: absolute;
    display: flex;
    flex-direction: column;
    height: 90%;
    width: 95%;
    overflow: hidden;
    top: 50% !important;
    transform: translateY(-50%) !important;
    z-index: 1000;
    border-radius: 12px;
    padding: 4px;

    &-header {
      position: sticky;
    }

    &-content {
      overflow-y: auto;
      overflow-x: hidden;
    }
  }
}
</style>
